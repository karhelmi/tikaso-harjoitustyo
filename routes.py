from app import app
from flask import render_template, request, redirect, url_for
from database import database
import users, products

#as instructed in course material
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/frontpage")
        else:
            return render_template("error_message.html", name="/", message="Incorrect username or password. Please try again.")
        
@app.route("/create_username", methods=["GET", "POST"])
def create_username():
    if request.method == "GET":
        return render_template("create_username.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error_message.html", message="The passwords do not match.")
        if users.create_username(username, password1):
            return redirect("/logout")
        else:
            return render_template("error_message.html", message="The operation of creating a new username was not successful. Please try again.")

@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():
    if request.method == "GET":
        products = products.get_list()
        return render_template("frontpage.html", products=products)
    if request.method == "POST":
        return redirect("/logout") ## VAIHDA TÄMÄ

@app.route("/error_message", methods=["GET", "POST"])
def error_message():
    if request.method == "GET":
        return render_template("error_message.html")
    if request.method == "POST":
        return redirect(name)

@app.route("/logout", methods=["GET", "POST"])
def logout():   
    if request.method == "GET":
        users.logout()
        return render_template("logout.html")
    if request.method == "POST":
        return redirect("/")