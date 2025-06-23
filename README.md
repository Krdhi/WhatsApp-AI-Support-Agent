# WhatsApp AI Support Agent – WhatsApp Chatbot using LangChain + OpenAI + Flask

Build a fully functional AI-powered WhatsApp Support Bot in Python. This project connects Twilio WhatsApp API with LangChain, OpenAI GPT, FAISS vector search, and Flask backend — no ngrok wrapper required.

---

## 🌎 Project Description

This project allows businesses to automate customer support on WhatsApp using AI. It reads a JSON-based FAQ file, embeds it using OpenAI embeddings, indexes it with FAISS, and answers customer queries through WhatsApp using natural language understanding.

---

## 📄 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## ✨ Features

* AI-based response generation with LangChain and GPT
* FAISS vector store for fast semantic search
* Flask backend with WhatsApp webhook via Twilio
* JSON FAQ loader with JQ schema parsing
* Custom prompt template for friendly support tone
* Easily adaptable for other businesses and domains

---

## 🚀 Installation

### 1. Clone this repository:

```bash
git clone https://github.com/yourusername/whatsapp-ai-support-agent.git
cd whatsapp-ai-support-agent
```

### 2. Setup virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

*If requirements.txt is not present, refer to the top of `app.py` for installation commands.*

### 4. Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Add your FAQ JSON file:

Save your FAQ document as `JustAnotherSampleBrew_FAQ.json` in the root folder.

### 6. Start your Flask app:

```bash
sudo python app.py
```

### 7. Start Ngrok tunnel in another terminal:

```bash
ngrok http 80
```

---

## 💪 Usage

* Link the Ngrok HTTPS URL to your Twilio WhatsApp webhook
* Send a message to your WhatsApp number
* The bot will respond with AI-generated answers from your FAQ file

---

## 🗂️ Project Structure

```
whatsapp-ai-support-agent/
├── app.py
├── .env
├── requirements.txt
├── JustAnotherSampleBrew_FAQ.json
```

---

## 🌐 License

This project is licensed under the MIT License.

---

## 👍 Acknowledgements

* [LangChain](https://www.langchain.com/)
* [OpenAI GPT](https://platform.openai.com/)
* [Twilio WhatsApp API](https://www.twilio.com/whatsapp)
* [FAISS Vector Search](https://github.com/facebookresearch/faiss)

---

## ✨ Notes

* Tested on Python 3.13 with PyCharm IDE
* There may be slight differences from Colab version mentioned elsewhere unless explicitly stated
* No Flask-Ngrok dependency used — ngrok tunnel must be started manually

---
