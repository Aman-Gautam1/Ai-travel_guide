# AI Travel Guide

## 🌍 Overview
The **AI Travel Guide** is a smart itinerary planner that helps users create personalized travel plans based on their budget, travel style, and preferences. It leverages **LangChain, Groq's Gemma2-9b-It, and Tavily Search API** to provide structured travel plans, including **accommodation, restaurants, transportation, attractions, and event recommendations.**

---
## 🚀 Features
✅ **Personalized Itinerary Generation** (Day-by-day activities, events, and transport options)
✅ **Budget-Based Hotel & Restaurant Suggestions** (Recommends places based on selected budget)
✅ **Real-Time Event Fetching** (Uses Tavily Search API to find ongoing events at the destination)
✅ **Estimated Travel Costs** (Summarized budget breakdown for the entire trip)
✅ **Easy-to-Use Web Interface** (Built with Streamlit)

---
## 🛠️ Tech Stack
- **Python** (Main programming language)
- **Streamlit** (Web UI framework)
- **LangChain** (Orchestrating AI responses)
- **Groq AI (Gemma2-9b-It)** (LLM for generating travel plans)
- **Tavily Search API** (Fetching real-time events & info)
- **GitHub + Streamlit Community Cloud** (Hosting & Deployment)


---
## 📜 Example Prompts & Outputs
### **System Prompt:**
```plaintext
You are an expert AI travel guide. Generate a structured itinerary with:
- Morning, Afternoon, Evening, and Night activities
- Budget estimates for accommodation, food, transport, and activities
- Travel times between locations
- Top-rated restaurants based on user preference
- Any ongoing festivals or events
- Alternative options based on different budgets
- Provide an estimated budget required to visit key attractions.
```
### **User Input:**
```plaintext
Plan a budget-friendly cultural trip to Mumbai from 2024-05-10 to 2024-05-15. I prefer public transport. Also, provide an estimated budget required to visit key attractions in Mumbai.
```
### **Generated Itinerary (Example Output):**
```plaintext
Mumbai Adventure Trip: Mid-Range Budget
Here's a sample itinerary for a mid-range adventure trip to Mumbai from 2024-05-10 to 2024-05-15, focusing on public transportation and exciting activities:

Day 1: Arrival & South Mumbai Charm

Morning: Arrive at Chhatrapati Shivaji Maharaj International Airport (BOM). Take the Airport Express Metro to reach your hotel in South Mumbai (approx. INR 50).
Afternoon: Check in to your hotel, like The Asiatic (approx. INR 3,500 per night). Explore the iconic Gateway of India and indulge in local street food (approx. INR 200).
Evening: Take a ferry to Elephanta Caves (approx. INR 250), marvel at the UNESCO World Heritage Site, and enjoy a traditional Indian dinner at Leopold Cafe (approx. INR 500).
Day 2: Dabbawalas & Bollywood Magic

Morning: Witness the fascinating Dabbawala system, Mumbai's iconic lunchbox delivery service (free, but tip recommended).
Afternoon: Visit the bustling Crawford Market for a sensory overload of spices, fruits, and local crafts (INR 100).
Evening: Immerse yourself in Bollywood at the iconic Gaiety-Galaxy Theatre (approx. INR 200) and enjoy dinner at a nearby restaurant (approx. INR 300).
Day 3: Art & Culture Exploration

Morning: Explore the Chhatrapati Shivaji Maharaj Vastu Sangrahalaya (CSMVS) museum, showcasing Mumbai's history and art (approx. INR 500).
Afternoon: Discover the vibrant street art scene in Bandra, capturing Instagram-worthy moments (free).
Evening: Enjoy a sunset stroll along Marine Drive, known as the "Queen's Necklace," and savor delicious snacks from street vendors (approx. INR 100).
Day 4: Coastal Beauty & Local Delights

Morning: Take a local train to Juhu Beach, relax by the Arabian Sea, and try some local chaat (approx. INR 100).
Afternoon: Explore the charismatic Bandra Fort, offering panoramic city views (free).
Evening: Indulge in a delicious seafood dinner at a restaurant in Bandra (approx. INR 500) and enjoy the lively nightlife.
Day 5: Farewell & Departure

Morning: Enjoy a leisurely breakfast at your hotel and check out.
Afternoon: Depending on your flight schedule, explore more of South Mumbai or head to the airport for your departure.
Estimated Budget:

Accommodation: INR 17,500 (5 nights at INR 3,500)
Food: INR 3,000 (approx. INR 600 per day)
Transportation: INR 2,000 (local trains, auto-rickshaws, ferries)
Activities & Attractions: INR 3,000 (approx. INR 600 per day)
Total: INR 25,500 (approx. USD 300)

Note: This budget is an estimate and can vary depending on your personal spending habits and preferences.

Let me know if you'd like me to elaborate on a specific aspect of the trip or if you have any other questions!
```

---


---
🔹 **Contributions Welcome!** Feel free to fork the repo and suggest improvements. 😊

