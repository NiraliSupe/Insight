from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework             import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework             import mixins, schemas
from rest_framework.response    import Response
from django.http import HttpResponse
from rest_framework.views       import APIView
from django.contrib.auth        import login, authenticate
from django.core                import serializers
from rest_framework             import generics
from rest_framework.decorators  import api_view, renderer_classes
from rest_framework             import exceptions, status
from django.conf                import settings
from rest_framework             import permissions
from django.core.exceptions     import PermissionDenied
from django.db.models           import Prefetch
from django.utils.decorators    import method_decorator
from django.views.decorators.cache  import cache_control
from django.views.decorators.cache  import never_cache
from django.contrib.auth.decorators import login_required
from api.models.user      import User
from api.serializers         import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ReadOnlyListView(mixins.ListModelMixin, generics.GenericAPIView):
    '''
    Parent class which allows to retrieve all the records
    '''
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # make this an uninstanceable class
    class Meta:
        abstract = True

class ListView(ReadOnlyListView, mixins.CreateModelMixin):
    '''
    Allows create new record
    '''
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # make this an uninstanceable class
    class Meta:
        abstract = True

class DetailView(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    '''
    Parent class which allows update, get or delete (set deleted field to True) specific record
    '''
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # make this an uninstanceable class
    class Meta:
        abstract = True
      
class UserList(ListView):
    """
    List all Entries, or create a new one.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name', 'gender', 'age')

class UserDetail(DetailView):
    """
    Get one User and show, modify or delete it
    """
    queryset         = User.objects.all()    
    serializer_class = UserSerializer
    lookup_field     = 'id'
