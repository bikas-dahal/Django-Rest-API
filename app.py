import requests 
import json

URL = 'http://127.0.0.1:8000/student/'

def getStudent(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
    

# getStudent(1)

def postStudent():
    data = {
        'name':'Hari',
        'roll': 102,
        'city':'KTM',
        'grade': 11
    }
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    

# postStudent()

def updateStudent():
    data = {
        'id': 1,
        'name':'Syamm',
        'roll': 102,
        'city':'KTM',
        'grade': 11
    }
    
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# updateStudent()

def deleteStudent():
    data = {
        'id': 1
    }
    
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

deleteStudent()
    