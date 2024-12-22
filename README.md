# friends
My take on a social media platform built with Django
It has user authentication, profile management, and the ability to create posts
---
Create a virtual environment and install dependencies using "pip install -r requirements.txt"
Place your environment variables in the ".env-sample" and rename it to ".env"
---
Run migrations using "python manage.py makemigrations" and "python manage.py migrate"
Start the development server using "python manage.py runserver"
---
You can run tests using "python manage.py test users/tests" and "python manage.py test posts/tests"