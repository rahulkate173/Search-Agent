import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (.env file with TAVILY_API_KEY and MISTRAL_API_KEY)
load_dotenv()

# Set up page configuration
st.set_page_config(page_title="Search Agent", page_icon="🔍")

# Initialize tools and chain only once to optimize performance
@st.cache_resource
def setup_agent():
    # Creating the Tavily search tool 
    tavily_search_tool = TavilySearch(max_results=5)
    
    # Creating prompt templates 
    prompt = ChatPromptTemplate.from_messages([
        ("system", "your work is to summarize and generate detailed message comming from and search agent"),
        ("human", "message is {message}")
    ])
    
    # Creating LLM 
    llm = ChatMistralAI(model="mistral-small-latest")
    
    # Creating the chain
    chain = prompt | llm 
    return tavily_search_tool, chain

tavily_search_tool, chain = setup_agent()

# --- Streamlit UI ---

st.title("🔍 Web Search & Summarizer")
st.markdown("Enter a query below. The agent will fetch search results and use Mistral AI to summarize them.")

# Create a form-like layout for the input
user_input = st.text_input("User:", placeholder="e.g., What are the latest updates on space exploration?")

# Add a button to trigger the run
if st.button("Generate Summary"):
    if user_input.strip():
        # Display a loading spinner while the tools are running
        with st.spinner("Searching the web and generating summary..."):
            try:
                # 1. Fetch search results
                search_results = tavily_search_tool.invoke(user_input)
                
                # 2. Pass results to the LLM chain
                outputs = chain.invoke({"message": search_results})
                
                # 3. Display the final response
                st.markdown("### Summary")
                st.write(outputs.content)
                
                # Optional: Add an expander to let the user see the raw search data
                with st.expander("View Raw Search Data"):
                    st.write(search_results)
                    
            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
    else:
        st.warning("Please enter a query before submitting.")