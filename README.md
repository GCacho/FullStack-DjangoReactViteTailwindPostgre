# FullStack System for Product Management
## BackEnd build with Django and PostgreSQL - FrontEnd build with React, ViteJs and Tailwind.

## BackEnd Installation (Django, PostgreSQL and Virtual Envirioment)
### Install and Configure PostgreSQL
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```
- Verify Installation
```
sudo service postgresql status
```
- Log in PostgreSQL
```
sudo -u postgres psql
```
- Create Database and User
```
CREATE DATABASE mydb;
```
- Create User:
```
CREATE USER myuser WITH PASSWORD 'mypassword';
```
- Assign privileges and configure access.
```
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```
- Exit PostgreSQL:
```
\q
CTRL+D
```
- View Databases and Users
```
sudo -u postgres psql -- (sudo -u user psql)
\l -- DataBases
\du -- User
```
- Connect with the new User
```
psql -h localhost -U myuser -d mydb
```
- Run and verify PostgreSQL
```
sudo service postgresql start
sudo service postgresql stop
sudo service postgresql status
sudo service postgresql restart
```
### Create Virtual Environment and Install Dependencies
```
python3 -m venv venv
source venv/bin/activate
cd backend
```
- Install dependencies and save them on a requirements.txt
```
pip install django 
pip install djangorestframework
pip install django-cors-headers
pip install psycopg2
```
- Verify dependencies Versions
```
pip freeze
```
- Verify correct Installation of all dependencies
```
pip install -r requirements.txt
```
### Create Django Project
- Create the project
```
django-admin startproject core
mv core backend
cd backend
ls (might show core and manage.py)
```
- Connect Django with PostgreSQL (config settings.py need to be running PosgreSQL services)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'nombre_de_tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',  # Set to the address of your PostgreSQL.
        'PORT': '5432',       # Default port of PostgreSQL.
    }
}
```
- Make DB Migrations
```
python3 manage.py migrate
```
- Create SuperUser for Django
```
python3 manage.py createsuperuser
```
- Create an App for Django
```
python3 manage.py startapp posts
```
- Config settings.py
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'posts',
]

CORS_ALLOWED_ORIGINS = ['http://localhost:5173']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
- Create a Model on posts app
``` python
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"Posts: {self.title}"
    
```
- Link your model to de admin.py
``` python
from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
```
- Create the API folder on the posts app and create the serializers.py, urls.py and views.py files
```
mkdir api
touch serializers.py
touch views.py
touch urls.py
```
- Create the API folder on the core section too but just with the urls.py file.
```
mkdir api
touch urls
```
- Config the urls.py on the core folder
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
]
```
- Make migrations when you finish
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- Run the server
```
python3 manage.py runserver
```
## FrontEnd Installation (React, ViteJs and Tailwind)
### Install ViteJs + React
- Update Packages.
```
sudo apt update && sudo apt upgrade
```
- Install NVM
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```
- Install Node.js y NPM:
```
nvm install node
```
- Verify Installation
```
node -v
npm -v
```
- On the root directory run
```
npm create vite@latest
✔ Project name: … frontend
✔ Select a framework: › React
✔ Select a variant: › JavaScript
cd frontend
npm install
npm run dev
```
- Create the .env file on frontend and add:
```
VITE_API_URL=http://127.0.0.1:8000/api/
```
- Give access to the app on React config src/App.jsx
``` jsx
import { useState, useEffect } from 'react'

function App() {
  useEffect(()=> {
    console.log(import.meta.env.VITE_API_URL)
  }, [])

  return (
    <>
     Hello
    </>
  )
}

export default App
```
- Dissable the React Strict mode on the main.jsx file
``` jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>
    <App />
  // </React.StrictMode>,
)
```

