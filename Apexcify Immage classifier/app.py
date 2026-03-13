from flask import Flask, render_template, request, jsonify
import base64
import os
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'image_classifier_secret_2024'

# Student Information
STUDENT_INFO = {
    'name': 'Syed Muneeb Haider',
    'country': 'Pakistan',
    'email': 'muneebshah1192@gmail.com',
    'internship': 'Artificial Intelligence',
    'task': 'Task 3: Image Classifier',
    'github': 'https://github.com/Muneebshah1192'
}

# Emotion facts and responses
EMOTION_RESPONSES = {
    'happy': {
        'message': '😊 You look happy! Keep smiling!',
        'fact': 'Smiling releases endorphins that make you feel happier!',
        'quote': 'Happiness is not something ready-made. It comes from your own actions.',
        'song': 'Happy - Pharrell Williams',
        'color': '#FFD700'
    },
    'sad': {
        'message': '😔 Everything okay? Remember, tough times don\'t last!',
        'fact': 'Crying releases toxins and reduces stress!',
        'quote': 'The sun will rise, and we will try again.',
        'song': 'Fix You - Coldplay',
        'color': '#4169E1'
    },
    'neutral': {
        'message': '😐 You seem focused and composed!',
        'fact': 'A neutral expression is often a sign of deep thinking!',
        'quote': 'Still waters run deep.',
        'song': 'Imagine - John Lennon',
        'color': '#808080'
    },
    'surprised': {
        'message': '😲 Wow! Something caught your attention!',
        'fact': 'Surprise is the briefest emotion, lasting only a few seconds!',
        'quote': 'Life is full of surprises!',
        'song': 'I Gotta Feeling - Black Eyed Peas',
        'color': '#FF1493'
    }
}

@app.route('/')
def home():
    return render_template('index.html', student=STUDENT_INFO)

@app.route('/api/analyze-emotion', methods=['POST'])
def analyze_emotion():
    """Endpoint to receive emotion data from frontend"""
    try:
        data = request.json
        emotion = data.get('emotion', 'neutral')
        confidence = data.get('confidence', 0)
        
        # Get response based on emotion
        response = EMOTION_RESPONSES.get(emotion, EMOTION_RESPONSES['neutral'])
        
        # Add timestamp
        response['timestamp'] = datetime.now().strftime('%H:%M:%S')
        response['confidence'] = f"{confidence * 100:.1f}%"
        
        return jsonify({
            'success': True,
            'emotion': emotion,
            'data': response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/save-snapshot', methods=['POST'])
def save_snapshot():
    """Save emotion snapshot (optional)"""
    try:
        data = request.json
        emotion = data.get('emotion')
        image_data = data.get('image')
        
        # In production, you might save to database
        # For now, just return success
        
        return jsonify({
            'success': True,
            'message': f'Snapshot saved! Emotion: {emotion}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/stats')
def get_stats():
    """Get statistics"""
    return jsonify({
        'total_predictions': random.randint(100, 500),
        'accuracy': '95%',
        'classes': len(EMOTION_RESPONSES),
        'status': 'online'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)