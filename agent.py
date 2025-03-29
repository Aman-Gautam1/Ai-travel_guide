import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import Tool

import datetime

import os
from dotenv import load_dotenv

st.set_page_config(page_title="AI Agentic Travel Guide")

# Load environment variables
load_dotenv()

api_key = st.secrets['GROQ_API']

tavily_api =  st.secrets['TAVILY_API_KEY']
#os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')

# Initialize Groq Model
llm = ChatGroq(model_name="Gemma2-9b-It", groq_api_key=api_key, streaming=True)
search_tool = TavilySearchResults(api_key = tavily_api)

# Streamlit UI
st.title("🗺️ AI Travel Guide")
st.subheader("Plan your perfect trip with AI-powered recommendations!")

# User Input Form
with st.form("travel_form"):
    destination = st.text_input("Enter your destination:")
    start_date = st.date_input("Start Date", min_value=datetime.date.today())
    end_date = st.date_input("End Date", min_value=start_date)
    budget = st.selectbox("Choose your budget:", ["Budget", "Mid-range", "Luxury"])
    travel_style = st.selectbox("What do you enjoy?", ["Adventure", "Relaxation", "Cultural", "Nightlife", "Food Tour", "Shopping"])
    transport = st.selectbox("Preferred Transport:", ["Public Transport", "Private Car", "Walking Tour"])
    submit_button = st.form_submit_button("Generate Itinerary")

if submit_button:
    if not destination:
        st.error("Please enter a destination!")
    else:
        # Generate real-time insights
        events_info = search_tool.invoke(f"Events happening in {destination} during {start_date} to {end_date}")
        if budget == "Budget":
            hotels_info = search_tool.invoke(f"Best budget hotels in {destination}")
            restaurants_info = search_tool.invoke(f"Cheap restaurants in {destination}")
        elif budget == "Mid-range":
            hotels_info = search_tool.invoke(f"Best mid-range hotels in {destination}")
            restaurants_info = search_tool.invoke(f"Mid-range restaurants in {destination}")
        else:
            hotels_info = search_tool.invoke(f"Best luxury hotels in {destination}")
            restaurants_info = search_tool.invoke(f"Fine dining restaurants in {destination}")
        
        # Construct AI Prompt
        system_prompt = SystemMessage(
            content=f"""
            -You are an expert AI travel guide. Generate a structured itinerary with:
            - Morning, Afternoon, Evening, and Night activities
            - Budget estimates for accommodation, food, transport, and activities
            - Travel times between locations
            - Top-rated restaurants based on user preference ({travel_style}) and budget ({budget}): {restaurants_info}
            - Best hotels based on selected budget ({budget}): {hotels_info}
            - Any ongoing festivals or events ({events_info})
            - Alternative options based on different budgets
            - Provide an estimated budget required to visit key attractions in {destination}
            - Summing up the total amount required for the journey with descriptions.
            """
        )
        user_prompt = HumanMessage(
        content=f"""
        Plan a {budget}-friendly {travel_style} trip to {destination} from {start_date} to {end_date}.
        I prefer {transport}.
        Also, provide an estimated budget required to visit key attractions in {destination}.
        """
        )   
        response = llm.invoke([system_prompt, user_prompt])
        st.subheader("Your Personalized Itinerary:")
        st.write(response.content)

        
        
        
        st.success("Itinerary generated successfully! Thanks")
