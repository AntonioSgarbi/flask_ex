# coding: utf-8
from flask import Flask, render_template

app = Flask("projeto")


@app.route("/")
def ola_mundo():
    name= "Flask"
    products = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]

    return render_template("ola.html", name=name, products=products), 200


app.run()
