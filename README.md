# Bookstore
It is a online shop which provide API to manipulate with book shop objects. Get to `http://{domain_name}/swagger/` to see an API documentation.
# Local launch
1. Clone this repository
2. Install requirements by following command: `pip install -r requirements.txt`
3. Apply all database migrations by following command: `python3 manage.py migrate`
4. Run server by following command: `python3 manage.py runserver`
# Environment setup:
1. Create at cloned directory file `.env` by following command: `touch .env`
2. Open `.env` file and set such variables:
    1. SECRET_KEY(Your Django secret key)
    2. DEBUG (True or False)
    3. ALLOWED_HOSTS (Values which are separated by comma)
    4. ENGINE=django.db.backends.postgresql_psycopg2
    5. NAME (Database name)
    6. USER (Postgres user)
    7. PASSWORD (Postgres password)
    8. HOST (domain of database or its ip)
    9. PORT (port of host db)
# Technological stack:
1. Python 3.9
2. Django
3. Django Rest Framework
4. PostgresSQL