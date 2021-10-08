from database import database
from flask import session
import users

def get_list():
    sql = "SELECT id, product, since, until FROM products"
    result = database.session.execute(sql)
    list = result.fetchall()
    return list

def selected_product(id):
    sql = "SELECT product FROM products WHERE id=:id"
    result = database.session.execute(sql, {"id":id})
    selected_product = result.fetchone()
    return selected_product

def add_idea(product_id, idea, visible):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO ideas (userid, product_id, idea, datum, visible) VALUES (:userid, :product_id, :idea, CURRENT_DATE, :visible)"
    database.session.execute(sql, {"userid":user_id, "product_id":product_id, "idea":idea, "visible":visible})
    database.session.commit()
    return True

def retrieve_ideas():
    sql = "SELECT id, product_id, idea, datum FROM ideas"
    result = database.session.execute(sql)
    idea_list = result.fetchall()
    return idea_list

def new_project(idea_id, team_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO projects (idea_id, project_team_id, start_datum, target_datum, completed, visible) VALUES (:idea_id, :project_team_id, CURRENT_DATE, CURRENT_DATE, :completed, :visible)"
    database.session.execute(sql, {"idea_id":idea_id, "project_team_id":team_id, "completed":"No", "visible":True})
    database.session.commit()
    return True

def get_projects():
    sql = "SELECT id, idea_id, project_team_id, start_datum, target_datum, completed, visible FROM projects"
    result = database.session.execute(sql)
    project_list = result.fetchall()
    return project_list


def get_projects2():
    sql = "SELECT P.id, R.product, I.idea, T.team_name, P.start_datum, P.target_datum, P.completed, P.visible FROM projects P, teams T, ideas I, products R WHERE I.id = P.idea_id AND T.id = P.project_team_id AND I.product_id = R.id"
    result = database.session.execute(sql)
    project_list = result.fetchall()
    return project_list