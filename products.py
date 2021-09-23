from database import database
from flask import session

def get_list():
    sql = "SELECT * FROM products"
    result = database.session.execute(sql)
    list = result.fetchall()
    return list