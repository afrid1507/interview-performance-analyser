# 🎤 Interview Performance Analyser

---

## 📸 Project Preview

### 🖥️ Home Interface

![Home UI](./assets/home.png)

### 📊 Analysis Output

![Output UI](./assets/output.png)

---

## 📌 1. Business Problem

In interviews, candidates often struggle to evaluate:

* Communication clarity
* Confidence level
* Emotional tone
* Overall delivery

There is no simple tool to provide **instant AI-based feedback**.

---

## 💡 2. Possible Solution

Build a system that:

* Transcribes interview audio
* Analyzes communication
* Provides feedback on strengths & weaknesses

---

## ⚙️ 3. Implemented Solution

A **Streamlit web app** that:

* 🎧 Takes audio input (.wav)
* 🎥 Takes video input (.mp4)
* 🧠 Uses:

  * Whisper → speech-to-text
  * TextBlob → sentiment analysis
* 📊 Outputs:

  * Confidence score
  * Clarity score
  * Strengths & weaknesses
  * Suggestions

👉 Note: Face analysis (DeepFace) removed due to Python compatibility issues.

---

## 🛠️ 4. Tech Stack

* Python
* Streamlit
* OpenAI Whisper
* TextBlob
* OpenCV
* PyTorch
* FFmpeg

---

# 🚀 How to Run the Project

## 🔹 Step 1: Clone Repo

```bash
git clone https://github.com/afrid1507/interview-performance-analyser.git
cd interview-performance-analyser
```

---

## 🔹 Step 2: Create Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
py -m pip install --upgrade pip
py -m pip install numpy
py -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
py -m pip install streamlit
py -m pip install openai-whisper
py -m pip install textblob
py -m pip install opencv-python
```

---

## 🔹 Step 4: Download TextBlob Data

```bash
py -m textblob.download_corpora
```

---

## 🔹 Step 5: Install FFmpeg

1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Extract
3. Add `bin` folder to PATH

Example:

```
C:\Users\afrid\Downloads\ffmpeg-8.1-essentials_build\ffmpeg-8.1-essentials_build\bin
```

Verify:

```bash
ffmpeg -version
```

---

## 🔹 Step 6: Run App

```bash
py -m streamlit run app.py
```
---

# 🐞 Errors Faced & Solutions

## ❌ Torch DLL Error

**Fix:**

```bash
py -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

## ❌ Numpy Error

**Fix:**

* Deleted venv
* Reinstalled numpy

---

## ❌ Missing Modules

(streamlit, whisper, textblob, cv2)

**Fix:**

```bash
py -m pip install streamlit openai-whisper textblob opencv-python
```

---

## ❌ DeepFace Error

**Reason:**

* Python 3.14 incompatible with TensorFlow

**Fix:**

* Removed DeepFace

---

## ❌ temp.wav Error

**Fix:**
Used `tempfile` instead of manual file creation

---

## ❌ FFmpeg Error

**Fix:**

* Installed FFmpeg
* Added to PATH

---

# 📊 Features

* ✅ Audio transcription
* ✅ Text sentiment analysis
* ✅ Confidence & clarity scoring
* ✅ Suggestions generation
* ❌ Face analysis (removed)

---

# 🎯 Conclusion

This project demonstrates how AI can:

* Evaluate interview performance
* Provide actionable feedback
* Help candidates improve communication

---

# 👨‍💻 Author

Afrid
GitHub: https://github.com/afrid1507

---

# ⭐ Future Improvements

* Add real-time analysis
* Add face emotion detection (with compatible Python)
* Improve scoring accuracy
