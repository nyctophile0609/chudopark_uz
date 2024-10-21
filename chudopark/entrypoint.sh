#!/bin/sh

# while ! mysqladmin ping -h"mysql" --silent; do
#     echo "Waiting for MySQL..."
#     sleep 2
# done

echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Creating superuser"
python3 manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="$DJANGO_SUPERUSER_USERNAME").exists():
    User.objects.create_superuser(
        username="$DJANGO_SUPERUSER_USERNAME", 
        email="$DJANGO_SUPERUSER_EMAIL", 
        password="$DJANGO_SUPERUSER_PASSWORD"
    )
    print("Superuser created successfully")
else:
    print("Superuser already exists")
END

exec "$@"
