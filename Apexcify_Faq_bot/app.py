from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import re
import random
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'muneeb_apexify_secret_2024'

# Professional Information
INTERNEE_INFO = {
    'name': 'Syed Muneeb Haider',
    'country': 'Pakistan',
    'email': 'muneebshah1192@gmail.com',
    'internship': 'Artificial Intelligence',
    'join_date': 'March 2024',
    'website': 'https://github.com/Muneebshah1192',
    'quote': 'Transforming data into intelligent solutions, building Pakistan\'s AI community.'
}

# Load the pre-trained models and data
try:
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)
    with open('faq_data.pkl', 'rb') as f:
        faq_df = pickle.load(f)
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"⚠️ Error loading models: {e}")
    vectorizer = None
    tfidf_matrix = None
    # Create sample data if files don't exist
    faq_data = {
        'questions': [
            "Who is Syed Muneeb Haider?",
            "What is your background?",
            "Tell me about your AI experience",
            "What projects have you worked on?",
            "How can I contact you?",
            "What is your email?",
            "Tell me about Pakistan",
            "What is the AI internship about?",
            "How do I apply for internship?",
            "What technologies do you use?"
        ],
        'answers': [
            "Syed Muneeb Haider is an AI enthusiast and developer from Pakistan, specializing in Machine Learning and Neural Networks.",
            "I'm an Artificial Intelligence intern at Apexcify Technologys, working on building intelligent solutions and contributing to Pakistan's AI community.",
            "I have experience in Python, Machine Learning, Deep Learning, and Natural Language Processing. I've built several AI projects including chatbots and prediction models.",
            "I've worked on various AI projects including chatbots, image classification systems, sentiment analysis tools, and predictive models using TensorFlow and PyTorch.",
            "You can contact me via email at muneebshah1192@gmail.com or visit my website: https://muneebhaid1192.github.io/",
            "My email is muneebshah1192@gmail.com. Feel free to reach out for any inquiries about AI or internship opportunities.",
            "Pakistan is a beautiful country with rich culture, amazing food (especially biryani!), and a growing tech community. It's home to K2, the world's second-highest mountain.",
            "The AI internship covers Python programming, Machine Learning algorithms, Neural Networks, Deep Learning, NLP, and Computer Vision with hands-on projects.",
            "To apply, send your resume to muneebshah1192@gmail.com with the subject 'AI Internship Application'. You'll hear back within 48 hours.",
            "I work with Python, TensorFlow, PyTorch, Scikit-learn, OpenCV, and various ML/NLP libraries to build AI solutions."
        ]
    }
    faq_df = pd.DataFrame(faq_data)

# Professional greetings
GREETINGS = [
    "Hello! I'm Syed Muneeb Haider's AI assistant. How can I help you today?",
    "Welcome! I'm here to assist you with information about AI, internships, and more.",
    "Hi there! Feel free to ask me about Syed Muneeb Haider, AI projects, or internship opportunities.",
    "Greetings! I'm your AI assistant. What would you like to know?"
]

# Commands list
COMMANDS = {
    'help': ['help', 'commands', 'what can you do'],
    'about': ['about', 'who is', 'tell me about', 'background'],
    'muneeb': ['muneeb', 'syed muneeb haider', 'creator', 'developer'],
    'ai': ['ai', 'artificial intelligence', 'machine learning', 'ml'],
    'internship': ['internship', 'intern', 'program', 'training'],
    'projects': ['projects', 'work', 'portfolio'],
    'contact': ['contact', 'email', 'reach', 'website'],
    'apply': ['apply', 'application', 'how to join'],
    'pakistan': ['pakistan', 'country'],
    'skills': ['skills', 'technologies', 'tools', 'tech stack']
}

def preprocess_text(text):
    """Clean and preprocess text"""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join(text.split())
    return text

def detect_command(user_message):
    """Detect if user message matches any command patterns"""
    message_lower = user_message.lower()
    
    for command, patterns in COMMANDS.items():
        for pattern in patterns:
            if pattern in message_lower:
                return command
    return None

def handle_command(command):
    """Handle special commands"""
    
    responses = {
        'help': """🔍 **Available Commands:**

• **about** - Learn about Syed Muneeb Haider
• **ai** - Information about AI expertise
• **internship** - Details about AI internship program
• **projects** - View AI projects and work
• **skills** - Technologies and tools used
• **contact** - Get contact information
• **apply** - How to apply for internship
• **pakistan** - About Pakistan

Type any command to get detailed information!""",
        
        'about': f"""👨‍💻 **About Syed Muneeb Haider**

**Name:** {INTERNEE_INFO['name']}
**Country:** {INTERNEE_INFO['country']}
**Specialization:** {INTERNEE_INFO['internship']}
**Joined:** {INTERNEE_INFO['join_date']}
**Website:** {INTERNEE_INFO['website']}

_{INTERNEE_INFO['quote']}_

Muneeb is passionate about creating intelligent solutions and building Pakistan's AI community through education and mentorship.""",
        
        'muneeb': f"""🌟 **Syed Muneeb Haider**

📍 **Location:** {INTERNEE_INFO['country']}
📧 **Email:** {INTERNEE_INFO['email']}
🌐 **Website:** {INTERNEE_INFO['website']}
🎓 **Focus:** {INTERNEE_INFO['internship']}

**Expertise:**
• Machine Learning & Deep Learning
• Neural Networks
• Natural Language Processing
• Computer Vision
• Python Development

**Mission:** Building intelligent solutions and nurturing Pakistan's AI talent.""",
        
        'ai': """🤖 **Artificial Intelligence Expertise**

**Core Competencies:**
• **Machine Learning** - Supervised & Unsupervised Learning
• **Deep Learning** - Neural Networks, CNNs, RNNs
• **Natural Language Processing** - Text Analysis, Chatbots
• **Computer Vision** - Image Recognition, Object Detection

**Tools & Frameworks:**
• Python, TensorFlow, PyTorch
• Scikit-learn, Keras, OpenCV
• Pandas, NumPy, Matplotlib
• Jupyter, VS Code, Git

**Applications:**
• Predictive Modeling
• Sentiment Analysis
• Image Classification
• Conversational AI""",
        
        'internship': """🎓 **AI Internship Program**

**Duration:** 6 months
**Level:** Beginner to Advanced
**Mentor:** Syed Muneeb Haider

**Curriculum:**
• **Month 1-2:** Python Fundamentals & Data Structures
• **Month 3-4:** Machine Learning Algorithms
• **Month 5-6:** Deep Learning & Specialized Projects

**Hands-on Projects:**
• Build a Chatbot (like me!)
• Image Classification System
• Sentiment Analysis Tool
• Predictive Model
• AI-Powered Recommendation Engine

**Benefits:**
• Real-world project experience
• One-on-one mentorship
• Portfolio development
• Certificate upon completion
• Job placement assistance

Type **'apply'** to learn how to join!""",
        
        'projects': """💻 **Featured AI Projects**

**1. Intelligent Chatbot**
   - NLP-powered conversational AI
   - Context-aware responses
   - Built with Python & TensorFlow

**2. Image Classifier**
   - CNN-based image recognition
   - 90%+ accuracy on test data
   - Real-time classification

**3. Sentiment Analyzer**
   - Social media sentiment analysis
   - Real-time emotion detection
   - Business intelligence tool

**4. Predictive Model**
   - Sales forecasting system
   - Time series analysis
   - 95% prediction accuracy

**5. AI Assistant**
   - Personal productivity assistant
   - Task automation
   - Voice-enabled interface

All projects available on request!""",
        
        'skills': """🛠️ **Technical Skills**

**Programming Languages:**
• Python (Advanced)
• JavaScript (Intermediate)
• SQL (Intermediate)

**AI/ML Frameworks:**
• TensorFlow
• PyTorch
• Scikit-learn
• Keras
• OpenCV

**Data Science:**
• Pandas
• NumPy
• Matplotlib
• Seaborn
• Jupyter

**Development Tools:**
• Git/GitHub
• VS Code
• Docker
• Flask
• AWS Basics

**Soft Skills:**
• Problem Solving
• Technical Writing
• Mentoring
• Project Management""",
        
        'contact': f"""📬 **Contact Information**

📧 **Email:** {INTERNEE_INFO['email']}
🌐 **Website:** {INTERNEE_INFO['website']}
📍 **Location:** {INTERNEE_INFO['country']}
💼 **Role:** {INTERNEE_INFO['internship']} Intern

**Response Time:** Within 24-48 hours

Feel free to reach out for:
• Collaboration opportunities
• Mentorship inquiries
• Project discussions
• Internship applications""",
        
        'apply': f"""📝 **Application Process**

**Step 1:** Prepare your resume/CV
**Step 2:** Email to: {INTERNEE_INFO['email']}
**Step 3:** Use subject line: "AI Internship Application - [Your Name]"
**Step 4:** Wait for response (24-48 hours)

**What to include in your email:**
• Updated resume
• Brief introduction
• Why you're interested in AI
• Any prior experience (optional)

**Selection Process:**
1. Resume screening
2. Online interview
3. Technical assessment
4. Final selection

Start your AI journey today! 🚀""",
        
        'pakistan': """🇵🇰 **About Pakistan**

**Capital:** Islamabad
**Population:** 220+ million
**Language:** English, Urdu
**Known for:**
• K2 - World's 2nd highest peak
• Rich cultural heritage
• Delicious cuisine (Biryani!)
• Growing tech industry
• Hospitality

**Tech Scene:**
• Rapidly growing startup ecosystem
• Increasing AI adoption
• Young, talented workforce
• Active developer community

Pakistan is proud to be home to many talented developers and AI enthusiasts like Syed Muneeb Haider!"""
    }
    
    return responses.get(command, "I didn't understand that command. Type **'help'** to see available commands.")

def get_best_answer(user_question):
    """Get the best answer for user question"""
    try:
        # Check for commands
        command = detect_command(user_question)
        if command:
            return handle_command(command)
        
        # Check for greetings
        message_lower = user_question.lower()
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(GREETINGS)
        
        # Check for thanks
        if any(word in message_lower for word in ['thanks', 'thank you']):
            return "You're welcome! Feel free to ask if you have more questions."
        
        # Check for goodbye
        if any(word in message_lower for word in ['bye', 'goodbye', 'see you']):
            return "Goodbye! Feel free to return anytime you have questions."
        
        # Default response
        return handle_command('help')
        
    except Exception as e:
        print(f"Error: {e}")
        return "I'm here to help! Try asking about Syed Muneeb Haider, AI internship, projects, or type 'help' for commands."

@app.route('/')
def home():
    return render_template('index.html', internee=INTERNEE_INFO)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        bot_response = get_best_answer(user_message)
        
        # Get suggestions based on context
        suggestions = get_suggestions(user_message)
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.now().strftime('%H:%M'),
            'suggested': suggestions
        })
        
    except Exception as e:
        return jsonify({
            'response': "I encountered an error. Please try again.",
            'timestamp': datetime.now().strftime('%H:%M'),
            'suggested': ["Tell me about Syed Muneeb Haider", "What is the AI internship?", "How to apply?"]
        })

def get_suggestions(message):
    """Get suggested questions based on context"""
    message_lower = message.lower()
    
    if 'muneeb' in message_lower:
        return [
            "What are Muneeb's skills?",
            "Tell me about his projects",
            "How can I contact him?",
            "What is his background?"
        ]
    elif 'internship' in message_lower:
        return [
            "What do I learn in AI internship?",
            "How long is the program?",
            "What projects will I work on?",
            "How do I apply?"
        ]
    elif 'ai' in message_lower or 'machine learning' in message_lower:
        return [
            "What AI projects have been built?",
            "What technologies are used?",
            "Can beginners learn AI?",
            "Tell me about neural networks"
        ]
    else:
        return [
            "Who is Syed Muneeb Haider?",
            "Tell me about the AI internship",
            "What projects have you worked on?",
            "How can I contact you?"
        ]

@app.route('/api/quick-apply', methods=['POST'])
def quick_apply():
    """Handle quick application"""
    try:
        data = request.json
        name = data.get('name', '')
        email = data.get('email', '')
        city = data.get('city', '')
        internship = data.get('internship', '')
        
        # Generate application ID
        app_id = f"AI{random.randint(1000, 9999)}"
        
        return jsonify({
            'success': True,
            'message': f"""✅ **Application Submitted Successfully!**

Thank you {name} for applying to the {internship} program.

**Application ID:** {app_id}
**Email:** {email}
**Location:** {city}

You will receive a confirmation email at {email} within 24 hours.

For immediate questions, contact: {INTERNEE_INFO['email']}""",
            'app_id': app_id
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f"Error submitting application: {str(e)}"
        })

@app.route('/api/commands')
def get_commands():
    """Get all available commands"""
    return jsonify({
        'commands': list(COMMANDS.keys()),
        'help_text': "Type any command to get detailed information"
    })

if __name__ == '__main__':


    app.run(debug=True, host='0.0.0.0', port=5000)