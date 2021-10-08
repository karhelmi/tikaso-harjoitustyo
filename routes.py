from app import app
from flask import render_template, request, redirect
from database import database
import users, products, teams

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
            return render_template(
                "error_message.html", name="/", 
                message="Incorrect username or password. Please try again.")
        
@app.route("/create_username", methods=["GET", "POST"])
def create_username():
    if request.method == "GET":
        return render_template("create_username.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if len(username) == 0 or len(password1) == 0:
            return render_template("error_message.html", message="Username or password cannot be empty.")
        if password1 != password2:
            return render_template("error_message.html", message="The passwords do not match.")
        if users.create_username(username, password1):
            return redirect("/")
        else:
            return render_template(
                "error_message.html", 
                message="The operation of creating a new username was not successful. Please try again. Maybe the username already exists.")

@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():
    if request.method == "GET":
        p = products.get_list()
        return render_template("frontpage.html", products=p)
    if request.method == "POST":
        selected_prod_id = request.form["product"]
        return redirect("/idea/" + str(selected_prod_id))

@app.route("/idea/<int:selected_prod_id>", methods=["GET", "POST"])
def idea(selected_prod_id):
    if request.method == "GET":
        selected_product = products.selected_product(selected_prod_id)
        return render_template("idea.html", selected_prod_id=selected_prod_id, sel=selected_product)
    if request.method == "POST":
        idea = request.form["idea"]
        visible=request.form["visible"]
        if len(idea) > 500:
            return render_template("error_message.html", message="The text is too long. Max. 500 letters.")
        else:
            if products.add_idea(int(selected_prod_id), idea, visible):
                return redirect("/list_of_ideas")
            else:
                return render_template("error_message.html", message="Pieleen meni idean lisääminen...")

@app.route("/list_of_ideas", methods=["GET", "POST"])
def list_of_ideas():
    if request.method == "GET":
        idealist = products.retrieve_ideas()
        corr_idealist = []
        for idea in idealist:
            id = idea[0]
            product = products.selected_product(idea[1])
            idea_text = idea[2]
            datum = idea[3]
            corr_idealist.append([id, product, idea_text, datum])
        return render_template("list_of_ideas.html", list_of_ideas=corr_idealist) #idealist)
    if request.method == "POST":
        return redirect("/ideas_project")

@app.route("/ideas_project", methods=["GET", "POST"])
def ideas_project():
    if request.method == "GET":
        idealist = products.retrieve_ideas()
        corr_idealist = []
        for idea in idealist:
            id = idea[0]
            product = products.selected_product(idea[1])
            idea_text = idea[2]
            datum = idea[3]
            corr_idealist.append([id, product, idea_text, datum])
        return render_template("ideas_project.html", list_of_ideas=corr_idealist)
    if request.method == "POST":
        idea_id = request.form["idea"]
        return redirect("/team_selection/" + str(idea_id)) ##Tulee Server error, jos yhtäkään ei ole valittu.

@app.route("/team_selection/<int:idea_id>", methods=["GET", "POST"])
def team_selection(idea_id):
    if request.method == "GET":
        employed = teams.get_employed()
        return render_template("team_selection.html", idea_id=idea_id, empl=employed)
    if request.method == "POST":
        team_name = request.form["team_name"]
        teams.add_team(team_name)
        team_id = teams.get_team_id(team_name)
        employee_id_list = request.form.getlist("employee_list") ##("employee_list[]")
        for employee_id in employee_id_list:
            teams.add_team_members(team_id, employee_id)
        products.new_project(idea_id, team_id)
        return redirect("/projects")
        #else:
         #   return render_template("error_message.html", message="Pieleen meni idean lisääminen...")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "GET":
        #employed = teams.get_employed()
        projects = products.get_projects2()
        return render_template("projects.html", projects=projects)
    if request.method == "POST":
        return redirect("/list_of_ideas")

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