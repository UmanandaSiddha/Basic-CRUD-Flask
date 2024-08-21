from models.user import User
from __init__ import db

def get_all_users():
    users = User.query.all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return {"id": user.id, "name": user.name, "email": user.email}
    else:
        return None

def create_new_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "name": user.name, "email": user.email}

def update_user(user_id, name):
    user = User.query.get(user_id)
    if user:
        user.name = name
        db.session.commit()
        return {"id": user.id, "name": user.name, "email": user.email}
    else:
        return None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
    else:
        return None