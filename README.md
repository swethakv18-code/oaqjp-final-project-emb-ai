Final project
# NLP Emotion Detection – Final Project

A Flask-based web application that detects emotions in text using IBM Watson NLP API.  
This project was developed as part of the **Applied AI with Deep Learning Specialization (Coursera)** final assignment.

---

## 🚀 Features
- Input text via a simple web interface
- Detects five emotions: **anger, disgust, fear, joy, sadness**
- Highlights the dominant emotion in the response
- Error handling for empty input
- REST API endpoint `/emotionDetector` for programmatic access

---

## 📂 Project Structure
final_project/
│── EmotionDetection/
│   ├── init.py
│   ├── emotion_detection.py
│   └── templates/index.html
│── static/
│   └── mywebscript.js
│── templates/ (legacy folder)
│   └── index.html (deprecated)
│── server.py
│── test_emotion_detection.py
│── requirements.txt
│── README.md

Code

---

## ⚙️ Setup Instructions
Clone the repository:
```bash
git clone git@github.com:swethakv18-code/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
Install dependencies:

bash
pip install -r requirements.txt
Run the Flask server:

bash
python3 server.py
Open in browser:

Code
http://127.0.0.1:5000/
🧪 Example Usage
Input:

Code
I love to study
Output:

json
{
  "anger": 0.01,
  "disgust": 0.00,
  "fear": 0.02,
  "joy": 0.95,
  "sadness": 0.02,
  "dominant_emotion": "joy"
}
📸 Screenshots
Screenshots of the interface and error handling are available in the screenshots/ folder.

🧑‍💻 Author
Swetha KV

Former Assistant Professor, now transitioning into AI/ML engineering

Skills: Python, Flask, scikit-learn, Docker basics, FastAPI fundamentals

Exploring AI/ML Specialist roles in startups

📜 License
This project is licensed under the MIT License.

Code

---

