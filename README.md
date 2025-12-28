# AI Text Summarization App

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → https://ai-text-summarization-5om7ljglhdcpuu7yz5zgmz.streamlit.app/

## Overview
This project is a simple AI-based text summarization application that converts long pieces of text into concise, easy-to-understand summaries using Natural Language Processing (NLP). The application provides a clean web interface where users can paste or upload text and instantly receive a summarized version.

## Features
- Input long text for summarization
- Generate concise and human-readable summaries
- Adjustable summary length (optional enhancement)
- Clean and minimal user interface built using Streamlit

## Tech Stack
- Python  
- Streamlit  
- TransformersHugging Face Transformers 

## Project Structure

```text
AI-Speech-Recognition/
│
├── app.py # Streamlit UI and application logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── ai_engine/
│   ├── init.py
│   └── summary.py # Text summarization model logic
│
└── screenshots/ # Application screenshots
    ├── home.png
    ├── input.png
    └── output.png
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-23 080103.png>)

### Text Input
![Text Input](<screenshots/Screenshot 2025-12-23 080129.png>)

### Summarization Output
![Summary Output](<screenshots/Screenshot 2025-12-23 080153.png>)

## How It Works
First, all required dependencies are installed and the application is launched using Streamlit. Once the app is running, the user is presented with a simple interface where they can paste a long piece of text. When the Summarize button is clicked, the text is processed using a pre-trained NLP summarization model. The model analyzes the content, extracts key information, and generates a concise summary, which is then displayed on the screen.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application is useful for students, researchers, content creators, and professionals who need to quickly understand long documents, articles, or reports. Instead of reading lengthy text, users can obtain a short and meaningful summary within seconds.

## Future Improvements
Support for document uploads (PDF, DOCX, TXT)
Improved summarization for very long texts using chunking
Multiple summary styles (short, detailed, bullet points)
Enhanced UI with better text formatting

## Learning Outcomes
Building this project helped me understand how NLP models can be integrated into real-world applications. I learned how to use pre-trained transformer models, handle long text inputs, and deploy AI functionality through a user-friendly interface. This project strengthened my confidence in building practical AI tools by learning through experimentation and implementation.
