# AI Voice Booking System – Multilingual Event Assistant

## Overview

This project implements a **voice-first AI assistant** that allows users to browse and book event tickets using natural speech. The assistant supports **multilingual voice interaction (English, Telugu, Hindi)** and performs event booking, availability checking, and smart recommendations.

The system demonstrates how **speech recognition, natural language processing, and database systems** can be integrated to create a fully voice-driven application.

Users can speak naturally such as:

> “Book two tickets for the photography workshop tomorrow”

The assistant will:

1. Convert speech to text
2. Extract booking intent
3. Check event availability
4. Confirm booking or suggest alternatives
5. Respond using synthesized speech

---

# Task Chosen

### Task 03 – AI Voice Booking System

I chose this task because it integrates multiple AI components such as speech recognition, natural language processing, and recommendation systems. I am familiar with these technologies and wanted to demonstrate my ability to build a practical project using them. The tech stack used in this project includes Python, SpeechRecognition, gTTS (Text-to-Speech), SQLite, and basic NLP for intent extraction.

This project allowed me to demonstrate:

* Real-time voice interaction
* Multilingual speech processing
* AI-based intent extraction
* Database-driven booking systems
* Smart recommendation logic

It closely resembles **real-world voice assistants such as Alexa or Google Assistant**, making it an interesting applied AI project.

---

# System Architecture

The system follows a modular pipeline architecture.

```
User Voice
   ↓
Speech Recognition (SpeechRecognition / Whisper-ready)
   ↓
Intent Extraction (NLP Parser)
   ↓
Event Database (SQLite)
   ↓
Booking Engine
   ↓
Recommendation System
   ↓
Text-to-Speech (gTTS)
   ↓
Voice Response
```

### Components

**Speech Recognition**

* Converts spoken audio into text
* Uses microphone input
* Supports multilingual speech

**Intent Extraction**

* Extracts structured information from user commands
* Identifies:

  * event name
  * number of tickets

**Event Database**

Stores event information including:

* event name
* category
* date
* time
* total seats
* booked seats

**Booking Engine**

Handles ticket booking and prevents overbooking.

**Recommendation System**

If an event is full, the assistant suggests **alternative events from the same category**.

**Text-to-Speech**

Converts the system response into voice output for a conversational experience.

---

# Project Structure

```
AI-Voice-Event-Booking
│
├── main.py
├── requirements.txt
├── README.md
│
├── database
│   ├── events.db
│   └── seed_events.py
│
├── speech
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── nlp
│   └── intent_parser.py
│
├── booking
│   ├── check_availability.py
│   ├── book_event.py
│   └── recommend_events.py
```

---

# Setup Instructions

---

## 1. Install Dependencies

```
pip install -r requirements.txt
```

Required libraries include:

* SpeechRecognition
* PyAudio
* gTTS
* langdetect
* sqlite3
* googletrans

---

## 2. Seed the Event Database

Initialize the database with sample events.

```
python database/seed_events.py
```

This creates **10–15 sample events** across different categories.

---

## 3. Run the Assistant

Start the voice assistant:

```
python main.py
```

The assistant will start listening for voice commands.

---

# Example Commands

Users can interact with the assistant using natural speech.

### English

```
Book 2 tickets for photography workshop
```

### Telugu

```
Photography workshop ki rendu tickets book cheyyi
```

### Hindi

```
Photography workshop ke liye 2 ticket book karo
```

---

# Example Interaction

```
🎤 Listening...

User: Book two tickets for photography workshop

Assistant:
Booking confirmed for Photography Workshop.
2 tickets booked.
Reference number BOOK-48231
```

If the event is full:

```
Assistant:
Sorry, Photography Workshop is full.
You can try Photography Advanced on 14 June at 5 PM.
```

---

# Screenshots / Demo Video

A demo video showing the assistant working end-to-end can be found here:

https://drive.google.com/file/d/1KvkTsS1VrMOlc8qrf1MDxUD-vtBDoV0z/view

The video demonstrates:

* Voice input
* Intent extraction
* Booking confirmation
* Recommendation system

---

# AI Components Used

### Speech Recognition

The system converts voice commands into text using a speech recognition model.

### Natural Language Understanding

The NLP module analyzes user commands to extract booking intent.

### Recommendation System

If an event is full, the assistant searches for similar events within the same category and suggests alternatives.

### Text-to-Speech

The assistant converts responses into audio, creating a fully voice-driven experience.

---

# Known Limitations

* Language detection is heuristic and may occasionally misclassify mixed-language input.
* Intent extraction currently uses rule-based parsing instead of a full LLM.
* The recommendation system is based on category similarity only.
* Background noise may affect speech recognition accuracy.

---

# Future Improvements

With more time, the system could be improved by:

* Integrating **OpenAI Whisper for speech recognition**
* Using **GPT-4 or Gemini for intent extraction**
* Adding **conversation memory**
* Implementing **real-time event updates**
* Adding a **web interface or mobile app**
* Improving multilingual understanding

---

# Conclusion

This project demonstrates how AI techniques can be combined to build a **voice-driven event booking assistant**. The system provides a natural conversational interface for event discovery and booking while ensuring that users are offered helpful alternatives when events are fully booked.

The project highlights the potential of **AI-powered voice interfaces in real-world applications** such as event management, customer support, and ticket booking systems.

