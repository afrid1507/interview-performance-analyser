import streamlit as st
from src.audio_analysis import transcribe_audio
from src.text_analysis import analyze_text
from src.video_analysis import analyze_video
from src.feedback import generate_feedback

st.title("Interview Performance Analyzer")

audio = st.file_uploader("Upload Audio (.wav)", type=["wav"])
video = st.file_uploader("Upload Video (.mp4)", type=["mp4"])

if st.button("Analyze Interview"):
    text = transcribe_audio(audio)
    confidence, clarity = analyze_text(text)
    emotion = analyze_video(video)

    strengths, weaknesses, suggestions = generate_feedback(confidence, clarity, emotion)

    st.subheader("Scores")
    st.write("Confidence:", confidence)
    st.write("Clarity:", clarity)
    st.write("Body Language:", emotion)

    st.subheader("Strengths")
    st.write(strengths)

    st.subheader("Weaknesses")
    st.write(weaknesses)

    st.subheader("Suggestions")
    st.write(suggestions)
