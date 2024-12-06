import openai
from typing import Dict, Any
import os
from datetime import datetime

def get_static_response(mood_category: str, mood_score: int) -> str:
    """Provide a static response when AI is unavailable"""
    responses = {
        'Happy': [
            "It's wonderful to see you're feeling positive! Consider what's contributing to your good mood and how you can maintain these positive elements in your life.",
            "What specific moments or activities brought joy to your day?",
            "Remember this feeling and consider sharing your positivity with others."
        ],
        'Sad': [
            "I hear you're having a difficult time. Remember that it's okay to not be okay, and your feelings are valid.",
            "Consider reaching out to someone you trust or trying a gentle self-care activity.",
            "What small step could you take right now to care for yourself?"
        ],
        'Anxious': [
            "When feeling anxious, try taking a few deep breaths. Remember that this feeling will pass.",
            "Consider writing down your worries and identifying what's in your control.",
            "What helps you feel grounded when anxiety rises?"
        ],
        'Neutral': [
            "A neutral state can be a good time for reflection and planning.",
            "Consider what would make today more meaningful for you.",
            "Sometimes neutral moments are perfect for trying something new."
        ]
    }
    
    base_response = responses.get(mood_category, responses['Neutral'])[0]
    
    if mood_score <= 3:
        support = "\n\nRemember: If you're consistently feeling low, consider reaching out to a mental health professional. You don't have to face this alone."
        return base_response + support
    elif mood_score >= 8:
        celebration = "\n\nThis is wonderful! Consider noting down what's working well so you can reference it in the future."
        return base_response + celebration
    else:
        return base_response

def generate_insight(mood_data: Dict[str, Any]) -> str:
    """Generate insight with fallback to static responses"""
    try:
        if not os.getenv('OPENAI_API_KEY'):
            return get_static_response(mood_data['mood_category'], int(mood_data['mood_score']))
            
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a supportive wellness companion focused on mental health and emotional well-being."},
                {"role": "user", "content": f"Based on the user's current mood ({mood_data['mood_category']}, score: {mood_data['mood_score']}/10) and their reflection: '{mood_data.get('reflection', '')}', provide a supportive and insightful response with: 1. A reflection on their current state, 2. A gentle suggestion for self-care, 3. A thought-provoking question for further reflection. Keep the response compassionate and non-judgmental."}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        # Log the error if needed
        print(f"AI generation error: {str(e)}")
        return get_static_response(mood_data['mood_category'], int(mood_data['mood_score']))

def get_coping_strategies(mood_category: str) -> list:
    """Return relevant coping strategies based on mood"""
    strategies = {
        'Sad': [
            "Take a gentle walk outside",
            "Reach out to a friend or family member",
            "Practice self-compassion meditation",
            "Listen to uplifting music"
        ],
        'Anxious': [
            "Try deep breathing exercises",
            "Practice progressive muscle relaxation",
            "Write down your worries",
            "Focus on what you can control"
        ],
        'Happy': [
            "Express gratitude",
            "Share your joy with others",
            "Engage in creative activities",
            "Plan something you look forward to"
        ],
        'Neutral': [
            "Set a small goal for the day",
            "Try something new",
            "Connect with nature",
            "Practice mindfulness"
        ]
    }
    
    return strategies.get(mood_category, strategies['Neutral'])
