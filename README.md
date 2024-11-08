**Setup Instructions**
1. Clone repository
2. Create virtual env using `python3 -m venv venv`
4. Run `pip3 install -r requirements.txt`; all site packages used should install.
7. Run `python3 manage.py runserver` to run server and check localhost.
8. If localhost does not run, check:
   * Migrations should not have to be updated as both the database `db.sqlite3` and migrations folder are included, but in case server does not load run `python3 ./manage.py makemigrations`. If there are migrations to be made, run `python3 manage.py migrate`. __DO NOT PUSH UP CHANGES WITH MIGRATIONS!__as this will cause an alignment issue with existing migrations and the database. Running migrations terminal commands should be used only to get the localhost site to run for previewing/testing.
10. Site should be up and running!