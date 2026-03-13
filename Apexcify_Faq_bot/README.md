# 🚀 Syed Muneeb Haider - AI Assistant Chatbot

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/AI-Chatbot-purple.svg" alt="AI Chatbot">
  <img src="https://img.shields.io/badge/Pakistan-Developer-brightgreen.svg" alt="Pakistan">
</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=Syed%20Muneeb%20Haider&fontSize=50&fontAlignY=35&animation=twinkling&fontColor=white" alt="header"/>
</p>

## 📋 Overview

A professional AI-powered chatbot and portfolio website for **Syed Muneeb Haider**, an Artificial Intelligence specialist from Pakistan. This application features an intelligent FAQ chatbot that provides information about AI, machine learning, internship opportunities, and technical expertise.

### ✨ Key Features

- 🤖 **AI-Powered Chatbot** - Intelligent responses to user queries
- 🎨 **Modern UI/UX** - Sleek, responsive design with gradient animations
- 📱 **Mobile Friendly** - Fully responsive across all devices
- 🎓 **AI Internship Program** - Detailed information about available programs
- 💼 **Professional Portfolio** - Showcase of skills, projects, and expertise
- 📧 **Quick Apply** - Easy application system for internships
- 🌐 **GitHub Integration** - Direct links to developer's GitHub profile

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask** - Web framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning utilities (optional)

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern features
- **JavaScript** - Interactive elements
- **Font Awesome 6** - Icons
- **Google Fonts (Inter)** - Typography

## 📁 Project Structure

```
apexcify-chatbot/
│
├── app.py                          # Main Flask application
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
│
├── templates/
│   └── index.html                   # Main HTML template
│
├── static/
│   ├── css/
│   │   └── style.css                # CSS styles
│   └── js/
│       └── script.js                 # JavaScript functionality
│
├── models/                           # (Optional - for ML features)
│   ├── vectorizer.pkl
│   ├── tfidf_matrix.pkl
│   └── faq_data.pkl
│
└── data/
    └── apexcify_faqs.csv             # FAQ dataset
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Muneebshah1192/apexcify-chatbot.git
cd apexcify-chatbot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Website
Open your browser and navigate to:
```
http://localhost:5000
```

## 📦 Dependencies

Create a `requirements.txt` file with:

```txt
Flask==2.3.3
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
```

## 💬 Chatbot Commands

The AI assistant responds to various commands:

| Command | Description |
|---------|-------------|
| `about` | Information about Syed Muneeb Haider |
| `ai` | Details about AI expertise and technologies |
| `internship` | Information about AI internship program |
| `projects` | List of AI projects and work |
| `skills` | Technical skills and expertise |
| `contact` | Contact information |
| `apply` | How to apply for internship |
| `help` | List all available commands |

## 🎨 Features in Detail

### 1. **AI Chatbot Interface**
- Real-time conversation
- Typing indicators
- Message history
- Sound effects (toggleable)
- Suggested questions
- Quick command chips

### 2. **Professional Portfolio**
- Hero section with personal info
- Skills and expertise showcase
- Project cards with technologies
- Contact information
- Social media links

### 3. **Internship Program**
- Program details and duration
- Curriculum overview
- Project-based learning
- Application form
- Success stories

### 4. **Responsive Design**
- Mobile-optimized layout
- Tablet-friendly interface
- Desktop enhancements
- Smooth animations
- Gradient backgrounds

## 🎯 Customization

### Personal Information
Edit the `INTERNEE_INFO` dictionary in `app.py`:

```python
INTERNEE_INFO = {
    'name': 'Syed Muneeb Haider',
    'country': 'Pakistan',
    'email': 'muneebshah1192@gmail.com',
    'internship': 'Artificial Intelligence',
    'join_date': 'March 2024',
    'website': 'https://github.com/Muneebshah1192',
    'quote': 'Your custom quote here'
}
```

### Adding New Commands
Edit the `COMMANDS` dictionary in `app.py`:

```python
COMMANDS = {
    'new_command': ['trigger', 'words', 'here'],
    # Add more commands...
}
```

### Modifying Responses
Update the `handle_command` function in `app.py` to customize responses.

## 🌐 Deployment

### Deploy on Render
1. Create a `render.yaml`:
```yaml
services:
  - type: web
    name: apexcify-chatbot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

### Deploy on PythonAnywhere
1. Upload files to PythonAnywhere
2. Set up a virtual environment
3. Configure WSGI file
4. Reload web app

### Deploy on Heroku
```bash
heroku create your-app-name
git push heroku main
heroku open
```

## 📱 Mobile Responsiveness

The website is fully optimized for:
- **Mobile phones** (320px - 480px)
- **Tablets** (481px - 768px)
- **Laptops** (769px - 1024px)
- **Desktops** (1025px and above)

## ⚡ Performance Optimizations

- Lazy loading for images
- Minified CSS/JS
- Optimized animations
- Caching headers
- Compressed assets

## 🔒 Security Features

- CSRF protection
- XSS prevention
- Secure headers
- Input sanitization
- Session management

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Syed Muneeb Haider**
- 📧 Email: muneebshah1192@gmail.com
- 🐙 GitHub: [@Muneebshah1192](https://github.com/Muneebshah1192)
- 📍 Location: Pakistan
- 🎓 Specialization: Artificial Intelligence

## 🙏 Acknowledgments

- Apexcify Technologys for the opportunity
- Flask community for excellent documentation
- Font Awesome for amazing icons
- Google Fonts for Inter typeface
- All contributors and supporters

## 📊 Project Status

🚧 **Current Version:** 1.0.0 (Stable)
✅ Production Ready
✅ Fully Tested
✅ Documentation Complete

## 🎯 Future Enhancements

- [ ] Machine learning integration for better responses
- [ ] Multi-language support
- [ ] User authentication system
- [ ] Admin dashboard
- [ ] Analytics integration
- [ ] Blog/Articles section
- [ ] Video tutorials
- [ ] Community forum

## 🐛 Known Issues

- None at this time. Please report any issues on GitHub.

## 📞 Support

For support, email muneebshah1192@gmail.com or create an issue on GitHub.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="footer"/>
  
  **Made with ❤️ in Pakistan** 🇵🇰
  
  *© 2024 Syed Muneeb Haider. All Rights Reserved.*
</div>
```