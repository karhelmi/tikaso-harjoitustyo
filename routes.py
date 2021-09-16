from app import app
from flask import render_template, request, redirect
import users #and other tables later as well

#as instructed in course material

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
