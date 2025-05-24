from django.apps import AppConfig
from django.db import connection
import threading
import requests

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        if not hasattr(self, 'already_loaded'):
            self.already_loaded = True
            # Запускаем загрузку в фоновом режиме
            threading.Thread(target=self.delayed_init).start()

    def delayed_init(self):
        from .models import User
        if 'users_user' in connection.introspection.table_names():
            self.load_initial_data()

    def load_initial_data(self):
        from .models import User
        if not User.objects.exists():
            print("Loading initial data...")
            try:
                response = requests.get('https://randomuser.me/api/?results=1000')
                data = response.json()['results']
                for user_data in data:
                    User.objects.create(
                        gender=user_data['gender'],
                        first_name=user_data['name']['first'],
                        last_name=user_data['name']['last'],
                        phone=user_data['phone'],
                        email=user_data['email'],
                        city=user_data['location']['city'],
                        country=user_data['location']['country'],
                        photo_url=user_data['picture']['medium'],
                    )
                print("Data loaded successfully!")
            except Exception as e:
                print(f"Error loading data: {e}")