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
            return redirect("/navigator")
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
        if len(username) < 4 or len(password1) < 4:
            return render_template("error_message.html", message="Username or password must include at least 4 characters.")
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
        number_of_ideas = products.number_of_ideas()
        number_of_projects = products.number_of_projects()
        return render_template("frontpage.html", products=p, number_of_ideas=number_of_ideas, number_of_projects=number_of_projects)
    if request.method == "POST":
        users.csrf()
        selected_prod_id = request.form["product"]
        if request.form["action"] == "Share your improvement idea":
            return redirect("/idea/" + str(selected_prod_id))
        elif request.form["action"] == "View raised ideas for the selected product":
            return redirect("/summary/" + str(selected_prod_id))
        else:
            return render_template("error_message.html", message="Something weird happened. Please use navigation buttons to return.")

@app.route("/idea/<int:selected_prod_id>", methods=["GET", "POST"])
def idea(selected_prod_id):
    if request.method == "GET":
        selected_product = products.selected_product(selected_prod_id)
        return render_template("idea.html", selected_prod_id=selected_prod_id, sel=selected_product)
    if request.method == "POST":
        users.csrf()
        idea = request.form["idea"]
        visible=request.form["visible"]
        if len(idea) > 300 or len(idea) < 3:
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
        users.csrf()
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
        users.csrf()
        idea_id = request.form["idea"]
        return redirect("/team_selection/" + str(idea_id))

@app.route("/team_selection/<int:idea_id>", methods=["GET", "POST"])
def team_selection(idea_id):
    if request.method == "GET":
        employed = teams.get_employed()
        return render_template("team_selection.html", idea_id=idea_id, empl=employed)
    if request.method == "POST":
        users.csrf()
        employee_id_list = request.form.getlist("employee_list")
        if len(employee_id_list) > 0:
            team_name = request.form["team_name"]
            add_name = teams.add_team(team_name)
            if add_name:
                team_id = teams.get_team_id(team_name)
                for employee_id in employee_id_list:
                    teams.add_team_members(team_id, employee_id)
                products.new_project(idea_id, team_id)
                return redirect("/projects")
            else:
                return render_template("error_message.html", message="Team name already exists; please choose another name.")
        else:
            return render_template("error_message.html", message="Please select at least one team member to the team.")
        
@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "GET":
        projects = products.get_projects2()
        return render_template("projects.html", projects=projects)
    if request.method == "POST":
        users.csrf()
        return redirect("/employees_involv")

@app.route("/summary/<int:selected_prod_id>", methods=["GET", "POST"])
def summary(selected_prod_id):
    if request.method == "GET":
        selected_product = products.selected_product(selected_prod_id)
        product_information = products.retrieve_product_info(selected_prod_id)
        return render_template("summary.html", selected_prod_id=selected_prod_id, sel=selected_product, product_info=product_information)
    if request.method == "POST":
        users.csrf()
        return redirect("/frontpage")

@app.route("/team_members/<int:selected_team_id>", methods=["GET", "POST"])
def team_members(selected_team_id):
    if request.method == "GET":
        selected_team_members = teams.team_members(selected_team_id)
        return render_template("team_members.html", selected_team_id=selected_team_id, team_members=selected_team_members)
    if request.method == "POST":
        users.csrf()
        return redirect("/projects")
            
@app.route("/employees_involv", methods=["GET"])
def employees_involv():
    if request.method == "GET":
        employees_involv_data = teams.retrieve_employees_involv_data()
        return render_template("employees_involv.html", employees_involv=employees_involv_data)

@app.route("/navigator", methods=["GET"])
def navigator():
    if request.method == "GET":
        return render_template("navigator.html")

@app.route("/error_message", methods=["GET", "POST"])
def error_message():
    if request.method == "GET":
        return render_template("error_message.html")
    
@app.route("/logout", methods=["GET", "POST"])
def logout():   
    if request.method == "GET":
        users.logout()
        return render_template("logout.html")
    if request.method == "POST":
        users.csrf()
        return redirect("/")