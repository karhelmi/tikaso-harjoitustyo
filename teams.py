from database import database
from flask import session
import users

def get_employed():
    sql = "SELECT id, first_name, last_name FROM employees"
    result = database.session.execute(sql)
    list = result.fetchall()
    return list

def add_team(team_name):
    user_id = users.user_id()
    if user_id == 0:
        return False    
    try:
        sql = "INSERT INTO teams (team_name, visible) VALUES (:team_name, :visible)"
        database.session.execute(sql, {"team_name":team_name, "visible": True})
        database.session.commit()
    except: 
        return False
    return True

def get_team_id(team_name):
    sql = "SELECT id FROM teams WHERE team_name=:team_name"
    result = database.session.execute(sql, {"team_name":team_name})
    team_id = result.fetchone()
    return team_id[0]

def add_team_members(team_id, employee_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO team_members (team_id, employee_id) VALUES (:team_id, :employee_id)"
    database.session.execute(sql, {"team_id":team_id, "employee_id":employee_id})
    database.session.commit()
    return True

def team_members(team_id):
    sql = "SELECT T.team_name, E.first_name, E.last_name FROM teams T, employees E, team_members TM WHERE T.id=:team_id AND TM.team_id=T.id AND TM.employee_id=E.id"
    result = database.session.execute(sql, {"team_id":team_id})
    team_members = result.fetchall()
    return team_members

def retrieve_employees_involv_data():
    sql = """SELECT E.first_name, E.last_name, T.team_name, I.idea, P.product
             FROM teams T, employees E, team_members TM, projects R, ideas I, products P 
             WHERE E.id=TM.employee_id AND TM.team_id=T.id AND T.id=R.project_team_id
             AND R.idea_id=I.id AND P.id=I.product_id ORDER BY E.last_name, E.first_name"""
    result = database.session.execute(sql)
    employee_involv_data = result.fetchall()
    return employee_involv_data