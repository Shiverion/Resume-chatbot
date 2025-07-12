---
title: career_conversations
app_file: app.py
sdk: gradio
sdk_version: 5.34.2
---

# 🤖 AI-Powered Personal Chatbot

An intelligent chatbot that represents me (Muhammad Iqbal Hilmy Izzulhaq) using RAG (Retrieval-Augmented Generation) technology. The chatbot can answer questions about my career, background, skills, and experience by leveraging a knowledge base built from my documents.

## ✨ Features

- **RAG-Powered Responses**: Uses vector embeddings to retrieve relevant information from your knowledge base
- **Document Processing**: Automatically processes PDF, TXT, and MD files from the `me/` folder
- **Real-time Chat Interface**: Beautiful Gradio web interface for seamless conversations
- **Smart Caching**: Optimized performance with intelligent caching of embeddings and responses
- **Tool Integration**: Built-in tools for recording user interactions and unknown questions
- **Push Notifications**: Optional integration with Pushover for monitoring interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Chatbot
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
   
   Create a `.env` file in the project root with **one** of the following API keys:
   ```env
   # Choose ONE of these options:
   
   # Option 1: OpenAI
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Option 2: Google Gemini
   GEMINI_API_KEY=your_gemini_api_key_here
   
   # Option 3: Anthropic Claude
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Option 4: Ollama (local)
   OLLAMA_BASE_URL=http://localhost:11434/v1
   
   # Optional: Pushover for notifications
   PUSHOVER_TOKEN=your_pushover_token_here
   PUSHOVER_USER=your_pushover_user_key_here
   ```

   **Get your API keys:**
   - **OpenAI**: Visit [OpenAI Platform](https://platform.openai.com/) for API keys
   - **Google Gemini**: Visit [Google AI Studio](https://aistudio.google.com/) for API keys
   - **Anthropic Claude**: Visit [Anthropic Console](https://console.anthropic.com/) for API keys
   - **Ollama**: Install locally from [Ollama.ai](https://ollama.ai/) (free, runs locally)
   - **Pushover** (optional): Visit [Pushover](https://pushover.net/) for notification tokens

5. **Add your documents**
   
   Place your PDF, TXT, or MD files in the `me/` folder. The chatbot will automatically process them to build its knowledge base.

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the chatbot**
   
   Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:7860`).

## 📁 Project Structure

```
Chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # Environment variables (create this)
├── me/                   # Your documents folder
│   ├── CV.pdf
│   ├── linkedin.pdf
│   ├── summary.txt
│   └── ...              # Add more documents here
└── vector_db/           # Vector database (auto-generated)
    └── ...
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | One Required | Your OpenAI API key |
| `GEMINI_API_KEY` | One Required | Your Google Gemini API key |
| `ANTHROPIC_API_KEY` | One Required | Your Anthropic Claude API key |
| `OLLAMA_BASE_URL` | One Required | Your Ollama base URL (e.g., `http://localhost:11434/v1`) |
| `PUSHOVER_TOKEN` | No | Pushover app token for notifications |
| `PUSHOVER_USER` | No | Pushover user key for notifications |

**Note**: You only need to set **one** of the LLM API keys. The application will automatically detect which one you've configured.

### Adding Documents

1. **Supported formats**: PDF, TXT, MD
2. **Place files** in the `me/` folder
3. **Restart the app** to process new documents
4. **Force reprocessing**: Use `force_reprocess=True` in the code if needed

## 🛠️ Technical Details

### Architecture

- **RAG System**: Uses ChromaDB for vector storage and similarity search
- **Embeddings**: OpenAI-compatible embeddings via multiple providers
- **Caching**: LRU cache for embeddings and context retrieval
- **Chunking**: Intelligent text chunking with overlap for better context

### Performance Optimizations

- **Embedding Caching**: Reduces API calls with intelligent caching
- **Context Caching**: Caches retrieved context for similar queries
- **Fast Startup**: Pre-loads static content for immediate responses
- **Background Processing**: Documents are processed in the background

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Gradio](https://gradio.app/) for the web interface
- Uses [ChromaDB](https://www.trychroma.com/) for vector storage
- Powered by multiple LLM providers (OpenAI, Google Gemini, Anthropic Claude, Ollama)

## 📞 Contact

- **LinkedIn**: [Muhammad Iqbal Hilmy Izzulhaq](https://linkedin.com/in/izzulhaq-iqbal)
- **Email**: miqbal.izzulhaq@gmail.com
- **GitHub**: [@Shiverion](https://github.com/Shiverion)

---

**Note**: This chatbot is designed to represent me professionally. It uses RAG technology to provide accurate, contextual responses based on my actual documents and experience.
