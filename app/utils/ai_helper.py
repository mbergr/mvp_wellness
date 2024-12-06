import os
from datetime import datetime

def get_static_response(mood_category, mood_score):
    """Get a static response based on mood category and score."""
    responses = {
        'happy': [
            "It's wonderful to see you're feeling happy! Keep engaging in activities that bring you joy.",
            "Your positive mood is great to see. Consider sharing your happiness with others today.",
            "Excellent mood! Take a moment to appreciate what's going well in your life."
        ],
        'calm': [
            "Being calm is a great state of mind. Perfect for reflection and mindfulness.",
            "Your peaceful state can help you make balanced decisions today.",
            "Maintaining this sense of calm can really benefit your overall well-being."
        ],
        'neutral': [
            "A balanced mood is a good foundation. What small thing could brighten your day?",
            "Sometimes a neutral mood is just what we need to think clearly.",
            "Consider this a clean slate - what would you like to accomplish today?"
        ],
        'anxious': [
            "Remember to take deep breaths. Anxiety is temporary and will pass.",
            "Try grounding yourself by focusing on five things you can see right now.",
            "Consider talking to someone you trust about what's making you anxious."
        ],
        'sad': [
            "It's okay to feel sad. Be gentle with yourself today.",
            "Remember that all feelings are temporary. Consider doing something kind for yourself.",
            "Reach out to someone you trust - sharing feelings often helps lighten the load."
        ]
    }
    
    # Default to neutral if category not found
    category_responses = responses.get(mood_category.lower(), responses['neutral'])
    
    # Use mood score to select different variations (higher scores get more positive variations)
    index = min(int(mood_score / 4), len(category_responses) - 1)
    return category_responses[index]

def get_coping_strategies(mood_category):
    """Get static coping strategies based on mood category."""
    strategies = {
        'happy': [
            "- Write down what made you happy today",
            "- Share your joy with a friend or family member",
            "- Plan something fun for tomorrow",
            "- Express gratitude for three things in your life"
        ],
        'calm': [
            "- Practice mindful breathing for 5 minutes",
            "- Take a peaceful walk outside",
            "- Listen to calming music",
            "- Write in your journal"
        ],
        'neutral': [
            "- Try a new hobby or activity",
            "- Set a small goal for today",
            "- Organize your space",
            "- Connect with a friend"
        ],
        'anxious': [
            "- Try the 5-4-3-2-1 grounding exercise",
            "- Take slow, deep breaths",
            "- Go for a walk or exercise",
            "- Write down your worries and possible solutions"
        ],
        'sad': [
            "- Be kind to yourself today",
            "- Listen to uplifting music",
            "- Reach out to a supportive friend",
            "- Do something that usually makes you smile"
        ]
    }
    
    return strategies.get(mood_category.lower(), strategies['neutral'])

def generate_insight(mood_data):
    """Generate insight with fallback to static responses"""
    return get_static_response(mood_data['mood_category'], int(mood_data['mood_score']))

def get_static_response_for_mood_category(mood_category, mood_score):
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
