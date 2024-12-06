from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app.models.user import MoodEntry
from app import db
from datetime import datetime
from app.utils.ai_helper import get_static_response, get_coping_strategies

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    # Get user's recent mood entries in ascending order for the chart
    recent_moods = MoodEntry.query.filter_by(user_id=current_user.id)\
        .order_by(MoodEntry.created_at.asc())\
        .limit(7)\
        .all()
    
    # Prepare mood data for the chart
    mood_data = [{
        'id': mood.id,
        'user_id': mood.user_id,
        'mood_score': mood.mood_score,
        'mood_category': mood.mood_category,
        'reflection': mood.reflection,
        'created_at': mood.created_at.strftime('%Y-%m-%d')
    } for mood in recent_moods]
    
    # Get the most recent entry for today's stats (in descending order)
    latest_moods = MoodEntry.query.filter_by(user_id=current_user.id)\
        .order_by(MoodEntry.created_at.desc())\
        .limit(7)\
        .all()
    
    return render_template('dashboard.html', 
                         moods=latest_moods,
                         mood_data=mood_data,
                         today=datetime.utcnow().date())

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Update user information
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        
        # Handle date of birth
        date_of_birth = request.form.get('date_of_birth')
        if date_of_birth:
            try:
                current_user.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid date format', 'error')
        
        current_user.gender = request.form.get('gender')
        current_user.occupation = request.form.get('occupation')
        current_user.bio = request.form.get('bio')
        
        # Handle preferences
        current_user.notification_enabled = bool(request.form.get('notification_enabled'))
        
        # Handle reminder time
        reminder_time = request.form.get('daily_reminder_time')
        if reminder_time:
            try:
                current_user.daily_reminder_time = datetime.strptime(reminder_time, '%H:%M').time()
            except ValueError:
                flash('Invalid time format', 'error')
        
        current_user.timezone = request.form.get('timezone')
        
        try:
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while updating your profile.', 'error')
            
        return redirect(url_for('main.profile'))
    
    return render_template('profile.html')

@main.route('/mood/new', methods=['GET', 'POST'])
@login_required
def new_mood():
    if request.method == 'POST':
        mood_score = request.form.get('mood_score')
        mood_category = request.form.get('mood_category')
        reflection = request.form.get('reflection')
        
        if not all([mood_score, mood_category]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('main.new_mood'))
        
        # Check if entry already exists for today
        today = datetime.utcnow().date()
        existing_entry = MoodEntry.query.filter_by(
            user_id=current_user.id,
            created_at=today
        ).first()
        
        if existing_entry:
            existing_entry.mood_score = mood_score
            existing_entry.mood_category = mood_category
            existing_entry.reflection = reflection
        else:
            entry = MoodEntry(
                user_id=current_user.id,
                mood_score=mood_score,
                mood_category=mood_category,
                reflection=reflection
            )
            db.session.add(entry)
        
        db.session.commit()
        
        # Get static response based on mood
        response = get_static_response(mood_category, int(mood_score))
        flash(response, 'success')
        
        return redirect(url_for('main.dashboard'))
    
    return render_template('mood/new.html')
