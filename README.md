

setting up the project steps:
0.
use mySQL workbench to create the database
    DATABASE NAME / SCHEMA NAME = test_schema

on the terminal, visual studio code, run these commands
python manage.py -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 

1.first create a superuser:

python manage.py create_superuser :
        email = 'admin@gmail.com'  
        password = 'adminpassword'   
2.LOGIN as ADMIN to create a voucher
* after a successfull creation of the admin, login
* login,Admin/Superuser will be redirected to admin and will be able to generate a generate voucher

TO VIEW A VOUCHER : 

    3. REGISTER as an external user 
    * Register as a user , 
    * login then click view voucher




