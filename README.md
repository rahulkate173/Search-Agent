# 🔍 Web Search & Summarizer Agent

A lightweight, powerful Streamlit web application that leverages **Tavily Search** to scour the web for the latest information and uses **Mistral AI** to synthesize and present a comprehensive, clean summary.

## 🔗 Live Application

Check out the live deployment here:  
👉 **[Live Demo on Streamlit Sharing](https://search-agent-zguoojaeprjbqu9dbmn4if.streamlit.app/)**

---

## 🚀 Features

- **Real-Time Web Search:** Utilizes `TavilySearch` to fetch the top 5 most relevant and up-to-date web results for any query.
- **Intelligent Summarization:** Passes search results through `Mistral AI` (`mistral-small-latest`) to generate highly coherent, detailed, and structured summaries.
- **Resource Caching:** Optimizes performance by utilizing Streamlit's `@st.cache_resource` for initializing LLM chains and search tools once.
- **Interactive UI:** A modern, clean user interface featuring interactive loading states (spinners), error handling, and collapsible sections to inspect raw search data.

---

## 🛠️ Prerequisites & Requirements

Ensure you have the following installed:
- **Python 3.8+**

### Required API Keys
To run this application locally, you will need:
1. **Tavily API Key:** Get one at [Tavily AI](https://tavily.com/).
2. **Mistral API Key:** Get one at [Mistral AI Console](https://console.mistral.ai/).

---

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and populate it with your credentials:
   ```env
   TAVILY_API_KEY=your_tavily_api_key_here
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

---

## 💻 Running the Application

Launch the Streamlit server locally with the following command:

```bash
streamlit run SearchTool.py
```

Once running, the application will automatically open in your default browser at `http://localhost:8501`.

---

## 🧠 How It Works

1. **User Query:** The user enters a topic or question in the text input box (e.g., *"What are the latest updates on space exploration?"*).
2. **Web Crawl:** The application triggers `TavilySearch` to retrieve 5 rich search results contextually matching the prompt.
3. **AI Synthesis:** The results are structured and piped into a `ChatPromptTemplate` along with a system instruction instructing Mistral AI to act as a summary agent.
4. **Result Delivery:** The finalized output is rendered beautifully using Markdown, and the user is given the option to inspect the raw search payloads returned by the Tavily API.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
