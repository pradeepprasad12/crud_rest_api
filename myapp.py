

import requests
import json

URL = "http://127.0.0.1:8000/api/enrollcreate/"
'''
data = {
    'name': 'raju',
    'email':'raju@gmail.com',
    'password':'raju'
}

json_data = json.dumps(data)
r = requests.post(url= URL,data= json_data)
data = r.json()
print(data)

def get_data(id=None):
    data={}
    if data is not None:
        data= {'id':id}
        json_data = json.dumps(data)
        r = requests.get(url= URL,data= json_data)
        data= r.json()
        print(data)
get_data(2)

def update_data():
    data= {'id':1,'name':'rupa','email':'pp@gmail.com','password':'rupa123'}
    json_data = json.dumps(data)
    r = requests.put(url= URL,data= json_data)
    data= r.json()
    print(data)

update_data()
'''
def delete_data():
    data= {'id':35}
    json_data = json.dumps(data)
    r = requests.delete(url= URL,data= json_data)
    data= r.json()
    print(data)

#delete_data()