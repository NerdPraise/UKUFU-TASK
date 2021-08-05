# Colonization Service architecture UKUFU
A microservice model of a simple RESTful API for managing 

### Requirements :
```
python == 3.9.1
Django >= 3.0.0
```
 
API References
### Usage
1. Clone project and cd into it
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
    "user_one": {
        "name": "Elsie Giles",
        "age": 28,
        "address": "937 Moffat Street, Dowling, Kansas, 578",
        "phone": "+18775333748"
    },
    "user_two": {
        "name": "Maribel Cruz",
        "age": 23,
        "address": "171 Krier Place, Deseret, South Carolina, 3117",
        "phone": "+18065953921"
    },
    "common_friends": [
        "Grace Kelly",
        "Bonnie Bass",
        "Cote Booth",
        "Carmella Lambert",
        "Decker Mckenzie",
        "Rosemary Hayes",
        "Mindy Beasley"
    ]
}
```
NB: This project was made with some assumptions in mind
1. Friendship were not symmetrical
2. Person's relationship with food is not symmetrical
3. Some info like 'tags' and '_id' were ignored 
4. Person guid is unique