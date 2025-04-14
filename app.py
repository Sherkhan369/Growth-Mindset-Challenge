
import streamlit as st

st.set_page_config(page_title="Growth mindset project", layout="wide")
st.title("Growth Mindset Project: web app with Streamlit")

st.header("Welcome to the Growth Mindset Project")
st.write("This is a web app built with Streamlit to demonstrate the growth mindset project.")

st.header("what is a growth mindset?")
user_input = st.text_input("Enter your definition of a growth mindset:")
if user_input:
    st.success(f"your are facing: {user_input}.keep pushing forword towords your goal")

else:
    st.warning("Tell us about your challenge: to get start!")

# reflexing
st.header("Reflexing on your challenge")
reflection = st.text_area("write your your reflections here:")

if reflection:
    st.success("Great job reflecting on your challenge!")
else:
    st.info("Reflection on your past experiences help you grow! Share your thoughts here:")

# Acheivements
st.header("Celebrating your achievements")
achievements = st.text_area("List your achievements here:")

if achievements:
    st.success(f"Great job celebrating your achievements! {achievements}")
else:
    st.info("Big or small, every achievement counts! Share your achievements here:")

# footer
st.write("----")
st.write("Thank you for using the Growth Mindset Project web app!")
st.write("Created by Sher Baz")



