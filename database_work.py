__author__ = 'lyndsay.beaver'
import sqlite3

db = sqlite3.connect('database.db')
#db.execute('create table person(firstname text, secondname text, age int) values ("lyndsay', "beaver", 46)
db.execute('insert into person (firstname , secondname , age) values ("lyndsay", "beaver", 46)')
db.commit()
