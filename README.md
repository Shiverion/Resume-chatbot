---
title: DPR-Chatbot
app_file: app.py
sdk: gradio
sdk_version: 5.36.2
---

# 🏛️ DPR RI Agenda Chatbot

An AI-powered chatbot for retrieving and answering questions about the agenda, meetings, and activities of the Indonesian House of Representatives (DPR RI). This chatbot uses Retrieval-Augmented Generation (RAG) with OpenAI and ChromaDB to provide accurate, context-based responses from a structured agenda dataset.

## ✨ Features

- **RAG-Powered Responses**: Retrieves relevant agenda information using vector embeddings and similarity search
- **Agenda Knowledge Base**: Uses a preprocessed CSV file (`me/agenda_clean.csv`) as the main data source
- **Real-time Chat Interface**: Simple Gradio web interface for interactive Q&A
- **Smart Embedding Cache**: Optimized performance with LRU caching for embeddings

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Resume-chatbot-with-RAG
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Prepare the agenda data**
   
   Ensure `me/agenda_clean.csv` exists and contains the agenda data. The chatbot will use this file to build its knowledge base.

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the chatbot**
   
   Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:7860`).

## 📁 Project Structure

```
Resume-chatbot-with-RAG/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .env                   # Environment variables (create this)
├── me/
│   └── agenda_clean.csv   # Preprocessed agenda data
└── vector_db/             # Vector database (auto-generated)
```

## ⚙️ Configuration

### Environment Variables

| Variable           | Required | Description              |
|--------------------|----------|--------------------------|
| `OPENAI_API_KEY`   | Yes      | Your OpenAI API key      |

## 🛠️ Technical Details

- **RAG System**: Uses ChromaDB for vector storage and similarity search
- **Embeddings**: OpenAI text-embedding-3-small model
- **Interface**: Gradio ChatInterface
- **Data Source**: agenda_clean.csv (CSV format)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This chatbot is designed for informational purposes to assist with DPR RI agenda queries. Ensure your agenda data is up to date for best results.
