# 📊 WhatsApp Chat Analyzer  
*A Data Science & Text Analytics Project*

---

## 🔍 Overview

The **WhatsApp Chat Analyzer** is an interactive data analytics application built using **Python and Streamlit** to analyze exported WhatsApp chat data.  
It provides comprehensive insights into chat activity, user behavior, word usage, emojis, timelines, and interaction patterns through rich visualizations and statistics.

This project focuses on **Exploratory Data Analysis (EDA)** and **rule-based Natural Language Processing (NLP)** on real-world conversational data.

---

## ✨ Features

- 📈 **Message Statistics**
  - Total messages, words, media shared, and links
- 🕒 **Time-based Analysis**
  - Daily & monthly activity timelines
  - Weekly activity heatmaps
- 👥 **User-level Insights**
  - Most active users
  - User-wise message distribution
- ☁️ **Word Cloud Visualization**
  - Highlights most frequently used words
- 📝 **Most Common Words Analysis**
  - After removing English + custom stopwords
- 😀 **Emoji Analysis**
  - Most frequently used emojis
  - Emoji distribution charts
- 🎨 **Interactive Dashboard**
  - Clean dark-mode UI using Streamlit

---

## 🖼️ Application Screenshots

### 🔹 Home & File Upload
![Home Screen](screenshots/home.png)

### 🔹 Active users
![Active_users](screenshots/active_user.png)

### 🔹 Most active day & monnth
![Most_Active_Day](screenshots/most_active.png)

### 🔹 Emoji Analysis
![Emoji](screenshots/emoji.png)


---

## 🧠 Project Category

- **Primary:** Data Analysis / Exploratory Data Analysis (EDA)
- **Secondary:** Text Analytics, NLP (Rule-based)
- **Visualization:** Interactive Dashboards

> ⚠️ This project does **not** involve machine learning model training or prediction.  
> NLP techniques used are **rule-based**, such as tokenization, stopword removal, and frequency analysis.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries & Tools:**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Streamlit
  - WordCloud
  - Emoji
- **Concepts:**
  - Data Cleaning & Preprocessing
  - Exploratory Data Analysis (EDA)
  - Text & Emoji Analytics
  - Data Visualization

---

## 📁 Project Structure

```text
whatsapp_chat_analyser/
│
├── app.py                 # Streamlit application
├── preprocessor.py        # Chat preprocessing logic
├── helper.py              # Analysis helper functions
├── assets/
│   ├── whatsapp.png
│   ├── analysis.png
│   ├── search.png
│   └── screenshots/
│       ├── home.png
│       ├── stats.png
│       ├── timeline.png
│       └── wordcloud.png
└── README.md
```

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

### 4️⃣ Upload WhatsApp Chat File

- Export a WhatsApp chat as a `.txt` file  
- Upload it using the sidebar in the application  

---

## 📊 Insights Generated

- Most active users in group chats  
- Peak messaging hours and days  
- Monthly and daily activity trends  
- Frequently used words and emojis  
- Media and link sharing behavior  

---

## 🔮 Future Enhancements

- Sentiment analysis using NLP models  
- User clustering based on chat behavior  
- Topic modeling for conversation themes  
- Interactive Plotly visualizations  
- Deployment on Streamlit Cloud  

---

## 👨‍💻 Author

**Abhi 😉**  
Data Science Enthusiast  

---

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub!

