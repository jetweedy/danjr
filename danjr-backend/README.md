
## Set up MongoDB Atlas:

https://www.mongodb.com/products/platform/atlas-database




## Set up Python Virtual Environment and Django:

## Unneeded:
```
django-admin startproject taskpilot . 
```

## Setup from this Repo:
``` 
mkdir danjr
cd danjr
mkdir danjr-backend
python -m venv venv
venv\Scripts\activate			<--
pip install django djangorestframework mongoengine configparser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver		<--
http://localhost:8000/tasks/
http://localhost:8000/admin/

...

cd ../
npx create-react-app danjr-frontend
cd danjr-frontend
npm start 						<--

...



``` 


