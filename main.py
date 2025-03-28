import streamlit as st  # type: ignore
import random
import time
import requests as req  # type: ignore

SECRET_PASSWORD = "Ubaid Is Real Aura"

st.title("💰 Money Making Machine 💰")

user_password = st.text_input("🔑 Enter Your Password (for Generate Money)", type="password")

# ✅ Random Money Generator Function
def generate_random_number():
    return random.randint(1, 1000)

user_name = st.text_input("👤 Enter your name:")

st.subheader("💸 Money Generator")

# ✅ Generate Money Button 
if st.button("💵 Generate Money"):
    if user_password == SECRET_PASSWORD: 
        if user_name.strip():  
            st.write("Generating Money... 💸")
            time.sleep(2)
            money = generate_random_number()
            st.success(f"🎉 {user_name} has won {money}$ dollars! 🤑")
        else:
            st.warning("⚠ Please enter your name to generate money!")
    else:
        st.error("❌ Incorrect Password! Please enter the correct password.")

# ✅ Side Hustle Ideas
def fetch_side_hustle():
    try:
        response = req.get("https://my-first-fast-api-bnw4.vercel.app/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing", "Side Hustling")
    except:
        return ("Something Went Wrong")

st.subheader("💼 Side Hustles Ideas")
if st.button("💡 Get an Idea"):
    idea = fetch_side_hustle()
    st.success(idea)

# ✅ Money Making Quotes
def fetch_money_making_quotes():
    try:
        res = req.get("https://my-first-fast-api-bnw4.vercel.app/money_making_quotes")
        if res.status_code == 200:
            quotes = res.json()
            if "money_making_quote" in quotes:
                return quotes["money_making_quote"]
            else:
                return "Invalid response format"
        else:
            return f"Error: Received status code {res.status_code}"
    except Exception as e:
        return f"Error: {e}"

st.subheader("💬 Money Making Quotes")
if st.button("📜 Get a Quote"):
    quote = fetch_money_making_quotes()
    st.success(quote)
