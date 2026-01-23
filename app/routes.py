from flask import Blueprint, request, jsonify  
from .models import db, Post, User  
from flask_jwt_extended import jwt_required, create_access_token  
from flask_login import login_user, logout_user, login_required  
  
main = Blueprint('main', __name__)  
  
# Route to save an entry  
@main.route('/save_entry', methods=['POST'])  
@jwt_required()  # Protect this route with JWT authentication  
def save_entry():  
    data = request.get_json()  
  
    project = data.get('project')  
    what_i_did = data.get('what_i_did')  
    what_i_learned = data.get('what_i_learned')  
    next_steps = data.get('next_steps')  
    mood = data.get('mood')  
    date = data.get('date')  # Ensure the date is passed  
  
    user_id = 1  # Replace with actual user_id after authentication (JWT-based or Flask-Login)  
  
    new_entry = Post(  
        date=date,  
        project=project,  
        what_i_did=what_i_did,  
        what_i_learned=what_i_learned,  
        next_steps=next_steps,  
        mood=mood,  
        user_id=user_id  
    )  
  
    db.session.add(new_entry)  
    db.session.commit()  
  
    return jsonify({'message': 'Entry saved successfully!'}), 201  
  
# Route to get all entries of the logged-in user  
@main.route('/get_entries', methods=['GET'])  
@jwt_required()  # Protect this route with JWT authentication  
def get_entries():  
    user_id = 1  # Replace with actual user_id after authentication (JWT-based or Flask-Login)  
  
    entries = Post.query.filter_by(user_id=user_id).all()  
    entries_list = []  
  
    for entry in entries:  
        entries_list.append({  
            'date': entry.date,  
            'project': entry.project,  
            'what_i_did': entry.what_i_did,  
            'what_i_learned': entry.what_i_learned,  
            'next_steps': entry.next_steps,  
            'mood': entry.mood,  
            'created_at': entry.created_at  
        })  
  
    return jsonify(entries_list)