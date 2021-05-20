#!/usr/bin/env python3

'''
Main backend application
To run: python3 main.py
'''

from flask import Flask
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column('id', sa.Integer, primary_key=True)
    username = sa.Column('username', sa.String, unique=True)


engine = sa.create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)


@app.route('/')
def home():
    return 'OK'


@app.route('/login')
def login():
    return 'TODO'


if __name__ == '__main__':
    app.run(debug=True)
