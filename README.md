# friends
My take on a social media platform built with Django and React
It has user authentication, profile management, and the ability to create posts
---
Create a virtual environment and install dependencies using "pip install -r requirements.txt"
Place your environment variables in the ".env-sample" and rename it to ".env"
---
Run migrations using "python manage.py makemigrations" and "python manage.py migrate"
Start the backend development server using "python manage.py runserver"
Start the frontend development server by cd frontend/ and using "npm start"
---
You can run tests using "python manage.py test users/tests" and "python manage.py test posts/tests"