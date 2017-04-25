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
                      
1. **Get All records for customer by field:** requests.get('https://host/api/user?gender=Female', auth=auth)                     
2. **Create record:** requests.post('https://host/api/user/',   headers=auth, data={field : value})                                 
3. **Get specific record:** requests.get('https://host/api/user/id/', auth=auth)                
4. **Update record:** requests.put('https://host/api/user/id/', auth=auth, data={field : value})               
5. **Delete record:** requests.get('https://host/api/user/id/', auth=auth)                           
