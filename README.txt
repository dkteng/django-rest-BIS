# BIS(Book Inventory System) RESTful API


## Introduction
This is a RESTful API to manage books. It is built using restframework in django


## Getting Started
To get started with this API, you will need to pip install django, djangorestframework 


## API References

### Get all books
retrieve json object of all books in db
#### Request
GET /books/
#### Response
json object


### Get single book
retrieve json object of specified book in db
#### Request
GET /books/<int:id>/
#### Response
json object


###Create single book
create book object in db
#### Request
POST /books/create/
#### Response
json object


###Update single book
update values of specified book object in db
#### Request
PATCH /books/update/<int:id>/
Request body:
{           "borrowed": <True/False>,
            "borrow_date": "<DateTime eg.2023-11-04T10:00:00Z>",
            "due_date": "<DateTime>",
            "borrowed_by": <id>,
            "title": "<Book title>",
            "author": "<Book author>",
            "genre": "<genre>"
} 
#### Response
json object


###Delete single book
delete book object from db
#### Request
DELETE /books/delete/<int:id>/
#### Response
string


###Get all borrowed books
retrieve all book objects from db with "borrowed" field = True
#### Request
GET /books/borrowed/
#### Response
json object


###Get all available books
retrieve all book objects from db with "borrowed" field = False
#### Request
GET /books/available/
#### Response
json object


###Get all users
retrieve all user objects from db
#### Request
GET /users/
#### Response
json object


###Get single user
retrieve single specified user object from db
#### Request
GET /users/<int:id>
#### Response
json object


###Signup
creates user object in db and returns API token for created user
#### Request
POST /signup
Request body:
{
    "username": "<username>",
    "password": "<password>",
    "first_name": "<firstname>",
    "last_name": "<lastname>",
    "email": "<email>"
}
#### Response
json object


###Login
returns API token for specified user object in db
#### Request
POST /login
Request body:
{
    "username": "<username>",
    "password": "<password>"
}
#### Response
json object


###Test token
returns string with 'username' value of user if token is correct for any user in db
#### Request
GET /login
API Key/Authorization: Token <token>
#### Response
string


## Conclusion
Thank you for using my API.


## NB (Problems):
1. if "borrowed" field is set to True, then "borrowed_by", "borrow_date" and "due_date" fields should now be required fields
but they are not.

2. response from "BorrowedBooks" view not serialized.

3. no check to make sure date submitted for "borrow_date" field is not earlier than "created" field date and "due_date" field date.

4. only "username" field is a required field in django User model. User model must be customized to require all fields when creating
instance of object.
