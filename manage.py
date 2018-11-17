#encoding: utf-8
import sqlite3
import pandas

from flask4 import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def init_database():
    conn = sqlite3.connect("database.db")
    df = pandas.read_csv('database.csv')
    #df = pandas.read_excel('database.csv')
    df.to_sql('database', conn, if_exists='append', index=False)
    print('ok')

# , if_exists='append'

if __name__ == '__main__':
    manager.run()