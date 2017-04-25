# Insight   

      
**Available objects through API:**         
1. User            

API documentation available at : http://host:port/api/docs/                 
                      
**Requirements:**         
Python 3.4.+         
Django 1.10.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: pip install django                            
djangorestframework&nbsp;&nbsp;: pip install djangorestframework      
                   

**Installation instructions:**              
1.  Install virtual  environment for Python 3.4.+               
2.  Install Django, Djangorest framework in virtual env            
3.  Pull the github content             
  											   
**Python commands to access user api:**     
auth = HTTPBasicAuth(username, password)                                          
Get All records for customer by field        | requests.get('https://host/api/user?gender=Female', auth=auth)   
Create record                                | requests.post('https://host/api/user/',   headers=auth, data={field : value})   
Get specific record                          | requests.get('https://host/api/user/id/', auth=auth)      
Update record                                | requests.put('https://host/api/user/id/', auth=auth, data={field : value})   
Delete record                                | requests.get('https://host/api/user/id/', auth=auth)    
