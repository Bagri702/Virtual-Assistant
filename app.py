# app.py
from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

# Initialize speech recognition and text-to-speech engines
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    query = request.form['query']
    # Call the AI assistant functionality here
    result = process_query(query)
    return result

def process_query(query):
    # Implement the AI assistant functionality here
    # For now, just return the query
    return query

if __name__ == '__main__':
    app.run(debug=True)