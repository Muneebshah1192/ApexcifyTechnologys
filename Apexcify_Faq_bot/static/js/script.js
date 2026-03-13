// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendMessage');
const clearButton = document.getElementById('clearChat');
const soundButton = document.getElementById('toggleSound');
const suggestionChips = document.querySelectorAll('.suggestion-chip');
const typingIndicator = document.getElementById('typingIndicator');
const toast = document.getElementById('toast');
const applyModal = document.getElementById('applyModal');
const applyForm = document.getElementById('applyForm');

// State
let isSoundEnabled = true;
let messageHistory = [];
let sessionId = generateSessionId();

// Professional responses
const GREETINGS = [
    "Hello! I'm Syed Muneeb Haider's AI assistant. How can I help you today?",
    "Welcome! Feel free to ask me about Muneeb's work, AI projects, or internship opportunities.",
    "Hi there! I'm here to assist you with any questions about AI and the internship program."
];

// Generate session ID
function generateSessionId() {
    return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

// Send message
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;
    
    addMessage(message, 'user');
    messageHistory.push({ text: message, sender: 'user', time: getCurrentTime() });
    userInput.value = '';
    
    typingIndicator.classList.add('active');
    if (isSoundEnabled) playSound('send');
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                message, 
                session_id: sessionId 
            })
        });
        
        const data = await response.json();
        
        typingIndicator.classList.remove('active');
        
        setTimeout(() => {
            addMessage(data.response, 'bot', data.timestamp);
            messageHistory.push({ 
                text: data.response, 
                sender: 'bot', 
                time: data.timestamp 
            });
            
            if (isSoundEnabled) playSound('receive');
            
            // Update suggestions
            updateSuggestions(data.suggested || []);
        }, 500);
        
    } catch (error) {
        console.error('Error:', error);
        typingIndicator.classList.remove('active');
        addMessage("I encountered an error. Please try again.", 'bot');
    }
}

// Add message
function addMessage(text, sender, timestamp = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    const time = timestamp || getCurrentTime();
    
    // Format message (bold text)
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/\n/g, '<br>');
    
    messageDiv.innerHTML = `
        <div class="message-content">
            <i class="fas fa-${sender === 'user' ? 'user' : 'robot'}"></i>
            <div class="message-text">
                ${text}
                <span class="timestamp">${time}</span>
            </div>
        </div>
    `;
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Get current time
function getCurrentTime() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// Update suggestions
function updateSuggestions(suggestions) {
    const container = document.getElementById('suggestionChips');
    if (!container) return;
    
    container.innerHTML = '';
    
    suggestions.forEach(suggestion => {
        const chip = document.createElement('button');
        chip.className = 'suggestion-chip';
        chip.textContent = suggestion;
        chip.onclick = () => {
            userInput.value = suggestion;
            sendMessage();
        };
        container.appendChild(chip);
    });
}

// Quick command
function quickCommand(command) {
    const commands = {
        'about': "Tell me about Syed Muneeb Haider",
        'ai': "What AI technologies do you work with?",
        'internship': "Tell me about the AI internship",
        'projects': "What projects have you worked on?",
        'skills': "What are your technical skills?",
        'contact': "How can I contact Syed Muneeb Haider?"
    };
    
    userInput.value = commands[command] || command;
    sendMessage();
}

// Clear chat
function clearChat() {
    if (confirm('Clear chat history?')) {
        chatMessages.innerHTML = `
            <div class="message bot">
                <div class="message-content">
                    <i class="fas fa-robot"></i>
                    <div class="message-text">
                        <p>Hello! I'm Syed Muneeb Haider's AI assistant. How can I help you today?</p>
                        <p>Try typing: <strong>"about"</strong>, <strong>"ai"</strong>, or <strong>"internship"</strong></p>
                        <span class="timestamp">${getCurrentTime()}</span>
                    </div>
                </div>
            </div>
        `;
        messageHistory = [];
        showToast('Chat cleared');
    }
}

// Toggle sound
function toggleSound() {
    isSoundEnabled = !isSoundEnabled;
    soundButton.innerHTML = `<i class="fas fa-volume-${isSoundEnabled ? 'up' : 'mute'}"></i>`;
    showToast(`Sound ${isSoundEnabled ? 'on' : 'off'}`);
}

// Show apply modal
function showApplyModal() {
    applyModal.classList.add('active');
}

// Handle apply form
if (applyForm) {
    applyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            city: document.getElementById('city').value,
            internship: document.getElementById('internshipSelect').value
        };
        
        try {
            const response = await fetch('/api/quick-apply', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (data.success) {
                showToast('Application submitted successfully!');
                applyModal.classList.remove('active');
                applyForm.reset();
                addMessage(data.message, 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error submitting application', 'error');
        }
    });
}

// Show toast
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.querySelector('span').textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Play sound
function playSound(type) {
    if (!isSoundEnabled) return;
    
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    if (type === 'send') {
        oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
    } else {
        oscillator.frequency.setValueAtTime(600, audioContext.currentTime);
    }
    
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
    
    oscillator.start();
    oscillator.stop(audioContext.currentTime + 0.1);
}

// Scroll to chat
function scrollToChat() {
    document.getElementById('chat').scrollIntoView({ behavior: 'smooth' });
}

// Event listeners
sendButton.addEventListener('click', sendMessage);
clearButton.addEventListener('click', clearChat);
soundButton.addEventListener('click', toggleSound);

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Suggestion chips
document.querySelectorAll('.suggestion-chip').forEach(chip => {
    chip.addEventListener('click', () => {
        const question = chip.dataset.question || chip.textContent;
        userInput.value = question;
        sendMessage();
    });
});

// Close modal when clicking outside
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
        e.target.classList.remove('active');
    }
});

// Close modal with close button
document.querySelectorAll('.close-modal').forEach(btn => {
    btn.addEventListener('click', () => {
        btn.closest('.modal').classList.remove('active');
    });
});

// Navigation active state
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-links a');
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K to focus input
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        userInput.focus();
    }
    
    // Escape to close modals
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal.active').forEach(modal => {
            modal.classList.remove('active');
        });
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    console.log('Welcome to Syed Muneeb Haider\'s AI Assistant');
});