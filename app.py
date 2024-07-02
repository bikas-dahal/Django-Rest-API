import requests 
import json

URL = 'http://127.0.0.1:8000/students/'

def getStudent(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
    

# getStudent(3)

def postStudent():
    data = {
        'name':'ozo3de',
        'roll': 22,
        'city':'KM',
        'grade': 11
    }
    
    headers = {'Content-Type': 'application/json'}
    
    json_data = json.dumps(data) 
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
    

# postStudent()

def updateStudent():
    data = {
        'id': 3,
        'name':'SSMB9',
        'roll': 22,
        'city':'KTM',
        'grade': 11
    }
    headers = {'Content-Type': 'application/json'}
    
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

# updateStudent()

def deleteStudent():
    data = {
        'id': 15
    }
    
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.delete(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

deleteStudent()
    