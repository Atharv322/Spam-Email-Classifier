import streamlit as st
import pickle

model = pickle.load(open("final_model.sav", "rb"))
feature_extraction = pickle.load(open("feature_extraction.pkl", "rb"))

# Streamlit UI

st.title("Spam Email Detector")
st.write("Enter a message to see that if its **SPAM** or **HAM**.")

input_text = st.text_area("Type your message: ")

if st.button("Predict"):
    if not input_text.strip():
        st.warning("Please enter a message...")
    else:
        input_data = [input_text]
        features = feature_extraction.transform(input_data)
        prediction = model.predict(features)
        
        if prediction[0]==1:
            st.success("✅ This is a **HAM** message.")
        else:
            st.error("🚫 This is a **SPAM** message.")
