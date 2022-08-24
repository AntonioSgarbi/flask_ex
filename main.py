# coding: utf-8
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask("projeto")
db = SQLAlchemy(app)
engine = sqlalchemy.create_engine('sqlite:///firstdb.db')


@app.route("/")
def ola_mundo():
    name= "Flask"
    products = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]

    return render_template("ola.html", name=name, products=products), 200


class Estudante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    registro = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


app.run()
