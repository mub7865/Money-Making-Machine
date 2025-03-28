import streamlit as st # type: ignore
import random 
import time 
import requests as req  # type: ignore


st.title("Money Making Machine")

def generate_random_number():
    return random.randint(1, 1000)

st.subheader("Random Number Generator")

if st.button("Generate Money"):
    st.write("Generating Money...")
    time.sleep(5)
    money = generate_random_number()
    st.success(f"You have won {money}$ dollars!")

def fetch_side_hustle():
    try:
        response = req.get("http://127.0.0.1:8000/side_hustles")
        if  response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing", "Side Hustling")
    except:
        return ("Something Went Wrong")
    
st.subheader("Side Hustles Ideas")
if st.button("Get an Idea"):
    idea= fetch_side_hustle()
    st.success(idea)


def fetch_money_making_quotes():
    try:
        res = req.get("http://127.0.0.1:8000/money_making_quotes")  # ✅ Corrected API URL
        if res.status_code == 200:
            quotes = res.json()
            if "money_making_quote" in quotes:  # ✅ Corrected key name
                return quotes["money_making_quote"]
            else:
                return "Invalid response format"
        else:
            return f"Error: Received status code {res.status_code}"
    except Exception as e:
        return f"Error: {e}"

    
st.subheader("Money Making Quotes")
if st.button("Get a Quote"):
    quote = fetch_money_making_quotes()
    st.success(quote)
