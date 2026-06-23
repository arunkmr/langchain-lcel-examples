📌 Overview

This project demonstrates the implementation of LangChain Expression Language (LCEL) for building modular LLM-based applications.

It includes a simple client-server setup, test scripts, and a Jupyter notebook for experimentation and understanding LLM pipelines.

📁 Project Structure
LCEL/
├── client.py              # Client script to send requests
├── serve.py               # Server handling LLM/API requests
├── test.py                # Testing script
├── simplellmLCEL.ipynb    # Notebook for experimentation
├── requirements.txt       # Dependencies
├── .env                   # API keys (NOT pushed to GitHub)
├── venv/                  # Virtual environment (NOT pushed to GitHub)
├── .gitignore             # Ignored files list
├── README.md              # Project documentation
⚙️ Features
LangChain Expression Language (LCEL) workflow
Client-server communication setup
Modular Python scripts
Testing support for validation
Notebook-based experimentation
Secure API key handling using .env
🚀 Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/LCEL.git
cd LCEL
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here
▶️ How to Run
Start Server
python serve.py
Run Client
python client.py
Run Tests
python test.py
🧪 Notebook

Open and run:

simplellmLCEL.ipynb

for experimentation with LCEL concepts.

## 📸 API Demo

Below is the running FastAPI Swagger UI showing LCEL chain execution:

![LCEL API Demo](assets/api-demo.png)