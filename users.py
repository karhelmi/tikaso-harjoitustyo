from database import database
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

def create_username(username, password):
    hash_value = generate_password_hash(password)
    try:
        if len(username) > 0 and len(password) > 0:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            database.session.execute(sql, {"username":username, "password":hash_value})
            database.session.commit()
    except:
        return False
    return True

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = database.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def logout():
    del session["user_id"]

def user_id():
    return session.get("user_id", 0)