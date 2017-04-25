from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')
urlpatterns = [

    url(r'^user/$',                 views.UserList.as_view()),           # List all customers or create new
    url(r'user/(?P<id>.+)/$',       views.UserDetail.as_view()),         # Get, update or delete 
    url(r'docs/$',                  schema_view, name='docs'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
