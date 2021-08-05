# Colonization Service architecture UKUFU
A microservice model of a simple RESTful API for managing 

### Requirements :
```
python == 3.9.1
Django >= 3.0.0
```
 
API References
### Usage
1. Clone project
2. Create .env file and add a key value pair with the key DJANGO_SECRET_KEY `DJANGO_SECRET_KEY="<soome value>"`
3. Run `python -m venv venv` to create a virtual environment
4. Run `pip install -r requirements.txt` to install all the necessary required packages
5. Run `python manage.py create_companies`
6. Run `python manage.py create_persons`
7. Run `python manage.py update_user_friends`
8. Run `python manage.py update_persons_food`
9. Run `python manage.py runserver` to start server and follow code snippet
10. Using any request simulator of your choice, perform the following actions

```python
base_url = 'http://localhost:8000/v1/'
routes = [
    'person/' # post to this route to get person info
    'company/<int:company_index>' # Get a company's detail
  ]
```
### Authentication
No Authentication

### Requests and Responses
1. Given a company, the API needs to return all their employees.
```python
url = "company/<int:company_index>" # run a GET request
response = {
    "id": 30,
    "employee": [
        "Karina Waller",
        "Jean Solomon",
        "Shields Cash",
        "Villarreal Shields",
        "Marissa Merritt",
        "Hudson Byers",
        "Sally Hunter",
        "Paul Long",
        "Singleton Conner",
        "Rosa Cox",
        "Willa Tyler"
    ],
    "name": "PROVIDCO",
    "index": 29
}
```

2. Given 1 people, provide a list of fruits and vegetables they like 
```python
url = "person/" # POST request
request = {
    "user_one": <person_index>,
}
response = {
    "username": "Maribel Cruz",
    "age": 23,
    "fruits": [
        "apple"
    ],
    "vegetable": [
        "cucumber",
        "carrot",
        "celery"
    ]
}
```
3. Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common who have brown eyes and 
are still alive
```python
url = "person/"  # POST request
request = {
    "user_one": <person_index>,
    "user_two": <person_index>,
}
response = {
    "username": "Maribel Cruz",
    "age": 23,
    "fruits": [
        "apple"
    ],
    "vegetable": [
        "cucumber",
        "carrot",
        "celery"
    ]
}
```
NB: This project was made with some assumptions in mind