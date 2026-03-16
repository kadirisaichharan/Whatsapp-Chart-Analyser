import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #1c1f26, #0e1117);
}
h1, h2, h3 {
    color: #ffffff;
}
.stMetric {
    background: rgba(255,255,255,0.05);
    padding: 18px;
    border-radius: 16px;
}
.stDataFrame {
    border-radius: 12px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD ASSETS =================
BASE_DIR = Path(__file__).resolve().parent
logo = Image.open(BASE_DIR / "assets" / "whatsapp.png")
analysis = Image.open(BASE_DIR / "assets" / "analysis.png")
search = Image.open(BASE_DIR / "assets" / "search.png")

# ================= HEADER =================
h1, h2 = st.columns([1, 4])

with h1:
    st.image(logo, width=120)

with h2:
    st.markdown("""
    <h1 style="margin-bottom:0;">WhatsApp Chat Analyzer</h1>
    <p style="color:#b0b3b8; font-size:15px;">
    Analyze WhatsApp conversations with rich statistics, timelines,
    word clouds, emoji insights, and user-level analytics.
    </p>
    """, unsafe_allow_html=True)

i1, i2, i3 = st.columns(3)
with i1:
    st.image(analysis, width=60)
    st.caption("Message & Time Analysis")

with i2:
    st.image(search, width=60)
    st.caption("Words & Emoji Insights")

with i3:
    st.image(analysis, width=60)
    st.caption("User-wise Statistics")

st.markdown("---")

# ================= SIDEBAR =================
st.sidebar.header("📂 Upload WhatsApp Chat")

uploaded_file = st.sidebar.file_uploader(
    "Choose exported .txt file",
    type=["txt"]
)

st.sidebar.markdown("---")
st.sidebar.header("🔍 Analysis Options")

# ================= MAIN LOGIC =================
if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    if "group_notification" in user_list:
        user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox(
        "Show analysis with respect to",
        user_list
    )

    if st.sidebar.button("🚀 Show Analysis"):

        with st.spinner("Analyzing chat..."):

            # ================= TOP STATS =================
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

            st.markdown("## 📊 Top Statistics")
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("💬 Total Messages", num_messages)
            with c2:
                st.metric("📝 Total Words", words)
            with c3:
                st.metric("📸 Media Shared", num_media_messages)
            with c4:
                st.metric("🔗 Links Shared", num_links)

            # ================= TIMELINES =================
            st.markdown("## 🗓 Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color="cyan")
            plt.xticks(rotation=45)
            st.pyplot(fig)

            st.markdown("## 📆 Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color="orange")
            plt.xticks(rotation=45)
            st.pyplot(fig)

            # ================= ACTIVITY MAP =================
            st.markdown("## 🔥 Activity Map")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Most Active Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_day.index, busy_day.values)
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.subheader("Most Active Month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values, color="tomato")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            st.subheader("Weekly Heatmap")
            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            sns.heatmap(user_heatmap, ax=ax)
            st.pyplot(fig)

        # ================= BUSY USERS =================
        if selected_user == "Overall":
            st.markdown("## 👥 Most Active Users")
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color="purple")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # ================= WORD CLOUD =================
        st.markdown("## ☁️ Word Cloud")
        wc = helper.create_word_cloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(wc)
        ax.axis("off")
        st.pyplot(fig)

        # ================= COMMON WORDS =================
        st.markdown("## 📝 Most Frequent Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        st.pyplot(fig)

        # ================= EMOJI ANALYSIS =================
        st.markdown("## 😀 Emoji Analysis")
        emojis_df = helper.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emojis_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(
                emojis_df[1].head(),
                labels=emojis_df[0].head(),
                autopct="%0.2f"
            )
            st.pyplot(fig)

# ================= FOOTER =================
st.markdown("""
<hr>
<center style="color:#888;">
Built with ❤️ using Python & Streamlit | WhatsApp Chat Analyzer
</center>
""", unsafe_allow_html=True)
