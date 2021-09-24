from database import database
from flask import session

def get_list():
    sql = "SELECT * FROM products"
    result = database.session.execute(sql)
    list = result.fetchall()
    return list

def add_idea(idea, datum, short_list, visible):
    sql = "INSERT INTO ideas (idea, datum, short_list, visible) VALUES (:idea, :datum, :short_list, :visible)"
    database.session.execute(sql, {"idea":idea, "datum":datum, "short_list":short_list, "visible":visible})
    database.session.commit()
    return True

def retrieve_ideas():
    sql = "SELECT id, idea, datum, short_list FROM ideas"
    result = database.session.execute(sql)
    idea_list = result.fetchall()
    return idea_list