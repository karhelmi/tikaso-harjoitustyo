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
    sql = "INSERT INTO teams (team_name, visible) VALUES (:team_name, :visible)"
    database.session.execute(sql, {"team_name":team_name, "visible": True})
    database.session.commit()
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