from database import database
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

#as instructed in course material

def create_username(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUE (:username, :password)"
        database.session.execute(sql, {"username":username, "password":hash_value})
        database.session.commit()
    except:
        return False
    return "Onnistuit!" #login(username, password) # muuta tämä login-sivuksi myöhemmin