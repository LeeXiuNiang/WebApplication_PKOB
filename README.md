## Requirements for Group Project
[Read the instruction](https://github.com/STIW3054-A211/e-sulam/blob/main/Assignment-1.md)

## Your Info: 

| Photo                          |Matric Number  | Name                | Phone Number     |
| ------------------------------ | ------------- | --------------------|----------------- |
| ![272033](/images/272033.png)  | 272033        | Lee Xiu Niang       | 012-5223989      |

## Introduction
In this assignment, a small Web Application for Pusat Kawalan Operasi Bencana (PKOB) system is developed using Python programming language. PKOB system assist in managing victim list and tasks regarding disaster such as handling welfare and financial help to the victims. The landing page which welcomes the users is the homepage of PKOB where briefly introduce about PKOB system. The user may register or add new user by entering details like IC number, name , and phone number. The system will validate whether the information inputted is valid. Besides that, the user details can be edited. However, only phone number can be edited as the IC number and name of an individual won’t normally. Hence, the restriction is to prevent the details been changed accidentally. Next, user also can be deleted. A confirmation will be done to ensure the user not deleted as mistake. Lastly, the age of users will be calculated by using birthday retrieved from the IC number.

## Link on Heroku
https://pkob272033.herokuapp.com/

## Result/Output (Screenshot of the output)
HomePage of PKOB  
![PKOB_Homepage](/images/PKOB_Homepage.png)  

Manage User List  
![PKOB_ManageUser](/images/PKOB_ManageUser.png)  

Add New User  
![PKOB_NewUserForm](/images/PKOB_NewUserForm.png)  

Validate New User Form 1  
![PKOB_Validation1](/images/PKOB_Validation1.png)  

Validate New User Form 2  
![PKOB_Validation2](/images/PKOB_Validation2.png)  

Validate New User Form 3  
![PKOB_Validation3](/images/PKOB_Validation3.png) 

Edit User Details  
![PKOB_EditUserDetail](/images/PKOB_EditUserDetail.png)

Delete User  
![PKOB_DeleteUser](/images/PKOB_DeleteUser.png)  

## Youtube Presentation
https://youtu.be/8tIXDoSMEpo

## List of Python packages (including the version) used for this system
asgiref==3.4.1  
Django==3.2.8  
gunicorn==20.1.0  
python-dateutil==2.8.2  
pytz==2021.3  
six==1.16.0  
sqlparse==0.4.2  

## References (Not less than 10)
Codemy.com (2021, March 4). How To Add Database Forms To A Web Page - Django Wednesdays #7 [Video]. YouTube.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=CVEKe39VFu8

Codemy.com (2021, March 24). Update and Edit Venues - Django Wednesdays #10 [Video]. YouTube.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=jCM-m_3Ysqk

Dennis Ivy (2019, December 11). Create Update & Delete (CRUD) with Model Forms | Django (3.0) Crash Course Tutorials (pt 10) [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=EX6Tt-ZW0so&t=814s

Django admin get_readonly_fields inconsistent behavior. (2011, November 9). StackOverflow.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://stackoverflow.com/questions/69903099/django-admin-get-readonly-fields-inconsistent-behavior?noredirect=1

Django CRUD (Create Read Update Delete) Example. (n.d.). Javatpoint.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.javatpoint.com/django-crud-application

Django CRUD Tutorial – Operations and Application Development. (n.d.). Data Flairs.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://data-flair.training/blogs/django-crud-example/ 

Django overwrite form clean method. (2010, March). StackOverflow.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://stackoverflow.com/questions/2432489/django-overwrite-form-clean-method/48580561 

Form and field validation. (n.d.). Django.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://docs.djangoproject.com/en/3.2/ref/forms/validation/

GoDjango (2019, May 10). Form Field Validation with Clean Methods [Video]. YouTube.     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=MUtc0pAF6b8

Read-Only Field in Django Form (n.d.). Newbedev.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://newbedev.com/read-only-field-in-django-form 
