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
            return redirect("/")
        else:
            return render_template("error_message.html", message="The operation of creating a new username was not successful. Please try again.")

@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():
    if request.method == "GET":
        p = products.get_list()
        return render_template("frontpage.html", products=p)
    if request.method == "POST":
        return redirect("/idea") #Miten tähän saa lisättyä, että mikä tuote valittu?

@app.route("/idea", methods=["GET", "POST"])
def idea():
    if request.method == "GET":
        return render_template("idea.html") ##sulkujen sisään vielä , mikä rivi valittu
    if request.method == "POST":
        idea = request.form["idea"]
        datum=request.form["datum"]
        short_list=request.form["short_list"]
        visible=request.form["visible"]
        if products.add_idea(idea, datum, short_list, visible):
            return redirect("/list_of_ideas")
        else:
            return render_template("error_message.html", message="Pieleen meni idean lisääminen...")

@app.route("/list_of_ideas", methods=["GET", "POST"])
def list_of_ideas():
    if request.method == "GET":
        idealist = products.retrieve_ideas()
        return render_template("list_of_ideas.html", list_of_ideas=idealist)
    if request.method == "POST":
    #    idea = request.form["idea"]
     #   datum=request.form["datum"]
      #  short_list=request.form["short_list"]
      #  visible=request.form["visible"]
      #  if products.add_idea(idea, datum, short_list, visible):
        return redirect("/frontpage")

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