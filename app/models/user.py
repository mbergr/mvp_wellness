from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    # Personal Information
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(20))
    occupation = db.Column(db.String(100))
    bio = db.Column(db.Text)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Preferences
    notification_enabled = db.Column(db.Boolean, default=True)
    daily_reminder_time = db.Column(db.Time)
    timezone = db.Column(db.String(50))
    
    # Relationships
    moods = db.relationship('MoodEntry', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)
    mood_category = db.Column(db.String(20), nullable=False)
    reflection = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'mood_score': self.mood_score,
            'mood_category': self.mood_category,
            'reflection': self.reflection,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }
