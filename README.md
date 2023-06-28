
# Django Ecommerce Project

Ecommerce website built with Django 4.2, Python 3.10.7

# Project Description

This Django project is an online store for selling nuts and dried fruits. It provides a user-friendly interface for customers to browse through a wide range of products, make purchases, and have them delivered to their doorstep. The project incorporates essential e-commerce functionalities such as product catalog, shopping cart and order management.






## Demo

HafezAghiliNuts.pythonanywhere.com

### Test Accounts:
```bash
- Admin account
Username : admin
Password : admin@1234

- Customer account located Tehran
Username : tehran
Password : user@1234
```  
## Screenshots
home page:
![App Screenshot](https://www.linkpicture.com/q/1_48.png)


product page:
![App Screenshot](https://www.linkpicture.com/q/4_769.png)

cart page:
![App Screenshot](https://www.linkpicture.com/q/5_588.png)

admin panel page:
![App Screenshot](https://www.linkpicture.com/q/6_79.png)



## Installation

Make sure you have python installed.

- Clone the project:
```bash
> git clone https://github.com/HafezAghili/django-ecommerce-project.git
```

- Make a virtual enviroment with desired name and active it:
```bash
> py -m venv venv_name
> venv_name\Scripts\activate
```   

- Install requirements:
```bash
> pip install django
> pip install Pillow
``` 

- run the project:
```bash
> py manage.py runserver
``` 

project should be accessible locally at http://127.0.0.1:8000
## Features

- Admin panel for controlling inventories, products and orders
- loading purchasable products for users based on their city
- tracking order processing for customers
- change password

