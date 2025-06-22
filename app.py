# 🎯 WhatsApp AI Support Agent — LangChain + OpenAI + FAISS + Flask (No flask-ngrok)

import os
from flask import Flask, request, abort
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain.chains import RetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.prompts import PromptTemplate
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv  # 📦 Load environment variables from .env file

# 🔐 Load OpenAI API key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 📄 Load and embed FAQ document
faq_file = "JustAnotherSampleBrew_FAQ.json"  # Upload this JSON file to your environment
loader = JSONLoader(file_path=faq_file, jq_schema=".[]", text_content=False)
docs = loader.load()

# 🧠 Create embeddings and FAISS vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# 💬 Define a more helpful, friendly system prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a friendly and knowledgeable customer support assistant for JustAnotherSampleBrew.
Use the following context to answer customer queries as helpfully and politely as possible.
If the answer is not known or not found, say: 'I'm not sure about that. You can reach out to our team for further help.'

Context:
{context}

Question:
{question}
"""
)

# 🔗 Create a RetrievalQA chain with a custom prompt
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        temperature=0.3,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    ),
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt_template}
)

# 🚀 Initialize Flask app (ngrok tunnel must be started manually)
app = Flask(__name__)

# 📥 WhatsApp webhook endpoint
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    print("📨 Raw request data:", request.form)  # Debug print

    if not request.form or 'Body' not in request.form:
        print("❌ Missing 'Body' in request.form")
        abort(403)

    user_msg = request.form.get("Body")
    print(f"📩 Received: {user_msg}")

    try:
        result = qa_chain.invoke(user_msg)
        answer = result['result']
        if answer.lower().startswith("answer:"):
            answer = answer[len("answer:"):].strip()
    except Exception as e:
        answer = f"Sorry, I encountered an error: {str(e)}"

    # 📤 Send response back to WhatsApp
    resp = MessagingResponse()
    resp.message(answer)
    return str(resp), 200  # ✅ Explicitly return HTTP 200

# ➕ Optional root route to avoid 403 errors on base URL
@app.route("/", methods=["GET"])
def home():
    return "✅ WhatsApp AI Support Agent is running.", 200

# 🔁 Start Flask app (start ngrok manually via terminal)
if __name__ == "__main__":
    print("📲 Starting WhatsApp AI Support Agent...")
    print("👉 Now run 'ngrok http 80' in a separate terminal and update the webhook URL in Twilio.")
    app.run(host="0.0.0.0", port=80)
