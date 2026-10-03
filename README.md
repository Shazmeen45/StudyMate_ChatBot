# StudyMate

StudyMate is a conversational AI study assistant built to help students understand academic topics through simple explanations and follow-up questions.

## About the Project

StudyMate was developed as an educational chatbot project. It provides students with a simple interface where they can ask questions about different study topics and receive clear and easy-to-understand responses.

The chatbot uses the Gemini API to generate responses and maintains the conversation during the current session, allowing users to ask follow-up questions.

## Purpose and Use Case

StudyMate is designed as an educational study assistant for students.

It can be used to:

- Ask questions about study topics
- Understand difficult concepts in simple language
- Get explanations and examples
- Ask follow-up questions
- Continue a topic within the same conversation

## Features

- Conversational AI chatbot
- Simple explanations of study topics
- Follow-up question support
- Conversation history during the current session
- Clear Chat option
- Streamlit-based web interface
- Gemini API integration

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## How It Works

StudyMate uses Python and Streamlit for the application and Gemini API for generating chatbot responses.

The basic flow is:

1. The user enters a question through the Streamlit interface.
2. The question is passed to the Python backend.
3. The backend sends the question to the Gemini API.
4. Gemini generates a response using the conversation context and system instructions.
5. The response is displayed in the chatbot interface.
6. The conversation is maintained during the current session.

A system prompt is used to guide the chatbot to provide clear, simple, and study-focused responses.

## Setup

## 1. Clone the Repository 

```bash
git clone https://github.com/Shazmeen45/StudyMate-Chatbot.git
```
## 2. Navigate to the Project Directory 
```bash 
cd StudyMate-Chatbot 
```
## 3. Create a Virtual Environment 
```bash
python -m venv venv
```
## 4. Activate the Virtual Environment 

For Windows PowerShell:
```bash
venv\Scripts\activate
```
## 5. Install Dependencies 
```bash
pip install -r requirements.txt
```
## 6. Configure the Gemini API Key

Create a file named .env in the project directory.

Add your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```
Do not upload the .env file to GitHub.

## 7. Run the Application 
```bash
python -m streamlit run app.py


The application will open in your browser.

## Testing

The chatbot was tested with different study-related questions, including:

Artificial Intelligence
Machine Learning
Difference between AI and Machine Learning
Python functions

Response time was also checked using two test questions:

Test 1: approximately 6 seconds
Test 2: approximately 4 seconds
Average response time: approximately 5 seconds

The chatbot was also tested with follow-up questions to check whether conversation context was maintained during the same session.

## Limitations

StudyMate relies on the Gemini API to generate responses. Therefore, its availability and response generation depend on the API and its usage limits.

StudyMate is intended as a study aid. When accuracy is important, information should be checked against reliable academic resources.

Future Improvements

Possible improvements for the project include:

Quiz and practice-question generation
Subject-specific study modes
PDF and document-based question answering
Improved conversation history
User feedback on responses
Further improvements to the user interface

## Author

Shazmeen Irshad