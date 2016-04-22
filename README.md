INSTALLATION:

1. virtualenv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. create database with user: postgres, password: postgres, dbname: montenegro2 

createdb.py
creates table and loads data
Usage:
python createdb.py

index.py
delete rows
Usage:
python index.py - (runs deletion from minimal date to minimal date +  5 years)
python index.py -s 2014-01-01 (runs deletion from 2014-01-01 to 2018-12-31)
python index.py -s 2014-01-01 -c 2 (runs deletion from 2014-01-01 to 2015-12-31)