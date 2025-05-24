# Random User API Project

Проект для взаимодействия с API randomuser.me с возможностью просмотра и пагинации данных.

## 🛠 Технологии
- Python 3.10+
- Django 5.2
- PostgreSQL
- Bootstrap 5

## 🚀 Запуск проекта

### Вариант 1: Локальный запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ВАШ_ЛОГИН/ApiProjectYadro.git
   cd ApiProjectYadro
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Настройте базу данных:
   - Установите PostgreSQL
   - Создайте БД `impulse2025`
   - Настройте доступ в `ApiProjectYadro/settings.py`

5. Примените миграции:
   ```bash
   python manage.py migrate
   ```

6. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

7. Откройте в браузере:
   ```
   http://localhost:8000/
   ```
```