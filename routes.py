from app import app
from flask import render_template, request, redirect
from database import database ##
import users #and other tables later as well

#as instructed in course material
@app.route("/", methods=["GET", "POST"]) ##TESTIIN METODIT LISÄTTY
def frontpage():
    if request.method == "GET": #TESTI
        return render_template("frontpage.html")
    if request.method == "POST":
        sana = request.form["sana"]
        sql = "INSERT INTO testi (sana) VALUES (:sana)" ##
        database.session.execute(sql, {"sana":sana})##
        database.session.commit()##
        #if users.testi(sana):
         #   return redirect("/create_username")
        #else:
         #   return render_template("error_message.html", message="The operation of creating a new username was not successful. Please try again.")

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