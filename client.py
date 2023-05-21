import json
import requests
BASE_URL = "http://localhost:8000/"
END_POINT = "api/"


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    res = requests.get(BASE_URL+END_POINT, data=json.dumps(data))
    print(res.status_code)
    print(res.json())

def create_resource():
    no = input("Enter no.: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    address = input("Enter address: ")
    new_emp = {'no': no, 'name': name, 'age': age, 'salary': salary, 'address': address}
    res = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(res.status_code)
    print(res.json())

def update_resource():
    id = input('Enter id: ')
    eno = input('Enter eno: ')
    ename = input('Enter ename: ')
    eage = input('Enter eage: ')
    esal = input('Enter esal: ')
    eaddr = input('Enter eaddr: ')
    new_emp = {'id': id}
    if eno != '':
        new_emp['eno'] = eno
    if ename != '':
        new_emp['ename'] = ename
    if eage != '':
        new_emp['eage'] = eage
    if esal != '':
        new_emp['esal'] = esal
    if eaddr != '':
        new_emp['eaddr'] = eaddr
    print(new_emp)
    res = requests.put(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(res.status_code)
    print(res.json())

def delete_resource():
    id = input('Enter id: ')
    data = {"id": id}
    res = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
    print(res.status_code)
    print(res.json())


def rest_operations():
    while True:
        print('1 : Get list of all emp')
        print('2 : Get single emp')
        print('3 : Create emp')
        print('4 : Update emp')
        print('5 : delete emp')
        print('0 : Exit')
        print('Press key to perform operation.')
        key = input('Enter key: ')
        if key == '1':
            get_resource()
        elif key == '2':
            id = input('Enter id: ')
            get_resource(id)
        elif key == '3':
            create_resource()
        elif key == '4':
            print('Press enter button to skip')
            update_resource()
        elif key == '5':
            delete_resource()
        elif key == '0':
            break
        else:
            print('Enter valid key.')


rest_operations()
