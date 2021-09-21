from database import database
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

#as instructed in course material

def create_username(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        database.session.execute(sql, {"username":username, "password":hash_value})
        database.session.commit()
    except:
        return False
    return True #login(username, password) # muuta tämä login-sivuksi myöhemmin

def testi(sana):
    #try:
    sql = "INSERT INTO testi (sana) VALUES (:sana)"
    database.session.execute(sql, {"sana":sana})
    database.session.commit()
    #except:
    #    return False
    return True