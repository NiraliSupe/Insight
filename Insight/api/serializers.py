from rest_framework          import serializers
from api.models.user         import User

'''
User Serializer starts here 
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model  =  User
         fields =  '__all__'
