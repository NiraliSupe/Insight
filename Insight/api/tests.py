from django.test         import TestCase
from django.contrib      import auth
from requests.auth       import HTTPBasicAuth
from rest_framework.test import APIClient
from api.models.user     import User
from rest_framework.test import APIClient
from requests import Session
import requests, re, ast
import unittest as unittest
import warnings
warnings.filterwarnings("ignore")
auth   = HTTPBasicAuth('admin', 'qazwsxedc')
url    = 'http://174.36.207.70:8000/api/user'
'''
Command to run:  python manage.py test api 
'''

class getByFieldTestCase(unittest.TestCase):

    def setUp(self):
        pass 

    def test_01_getByGender(self):
        '''
        Find users based on gender
        '''
        response = requests.get(url+'?gender=Female', auth=auth)
        self.assertEqual(response.status_code, 200)
        result   =  ast.literal_eval(response.text)
        for row in result:
            self.assertEqual(row['gender'], "Female")

    def test_02_getByName(self):
        '''
        Find users based on first name
        '''
        response = requests.get(url+'?first_name=Bobbette', auth=auth)
        self.assertEqual(response.status_code, 200)
        result   =  ast.literal_eval(response.text)[0].get("first_name")
        self.assertEqual(result, "Bobbette")

class userTestCase(unittest.TestCase):
    '''
    Covers CURD operations for customer
    '''
    user_id    = None
        
    def setUp(self):
        pass 

    def test_01_create(self):
        '''
        Create customer.
        '''
        payload  = {"first_name":"Nirali","last_name":"phalak","gender":"Male","age":"30"}
        response = requests.post(url+'/', auth=auth, data=payload)
        self.assertEqual(response.status_code, 201)
        name     = ast.literal_eval(response.text).get("first_name")
        user_id  = 1003 #ast.literal_eval(response.text).get("id")
        self.__class__.user_id = user_id
        self.assertEqual(name, 'Nirali') 
    
    def test_02_get(self):
        '''
        Get detailed user API testing
        '''
        user_id    = self.__class__.user_id
        response   = requests.get(url+'/'+str(user_id), auth=auth)
        self.assertEqual(response.status_code, 200)
        first_name = ast.literal_eval(response.text).get("first_name")
        self.assertEqual(first_name, 'Nirali')
   
    def test_03_update(self):
        '''
        Update API testing
        '''
        user_id  = self.__class__.user_id
        response = requests.get(url+'/'+str(user_id), auth=auth)
        payload  = ast.literal_eval(response.text)
        payload['gender'] = "Female"
        response = requests.put(url+'/'+str(user_id)+'/', auth=auth, data=payload)
        self.assertEqual(response.status_code, 200)
        updatedFieldValue = ast.literal_eval(response.text).get('gender')
        self.assertEqual(updatedFieldValue, 'Female')
   
    def test_04_delete(self):
        '''
        Delete API testing
        '''
        user_id  = self.__class__.user_id
        response = requests.delete(url+'/'+str(user_id)+'/', auth=auth)
        self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()

