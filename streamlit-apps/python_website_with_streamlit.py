import streamlit as st
from PIL import Image

# Page config must be first
st.set_page_config(
    page_title="My Portfolio",
    layout="centered",
    page_icon="🌐",
)

# Sidebar navigation
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Streamlit Site! 🚀")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQovXSjh7U2wgD2DFzF3uWj8NpMRsZPJ6nyYQ&s/150", caption="That's me!", width=150)

    with col2:
        st.subheader("👋 Hello, I'm a Python Developer")
        st.write("""
                This simple yet beautiful site is powered by **Streamlit**. I enjoy building:
- 🛍️ Full-stack marketplace websites (Next.js + TypeScript)
- 🐍 Python projects & mini tools
- 📈 Interactive apps using Streamlit
""")

        st.markdown("[💼 Check my LinkedIn](https://www.linkedin.com/in/zeenat-yameen-0168a829b/)")


# About Page
elif page == "About":
    st.header("About This Website")
    st.write("""
    This project is an example of how you can use Streamlit to create a responsive, minimal website
    that can be used for portfolios, contact forms, or interactive data apps.
    """)

    st.info("Built with Python, ❤️, and Streamlit.")

# Contact Page
elif page == "Contact":
    st.header("📬 Get in Touch")

    st.write("Fill out the form below to send me a message:")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name:")
        email = st.text_input("Your Email:")
        message = st.text_area("Your Message:")
        submit = st.form_submit_button("📤 Send Message")

        if submit:
            if name and email and message:
                st.success(f"✅ Thanks {name}! I’ll get back to you at {email}.")
            else:
                st.warning("⚠️ Please fill out all fields.")

# --- Footer ---
st.markdown("""---""")
st.markdown(
    "<div style='text-align: center; padding-top: 10px;'>"
    "<strong>Created by Zeenat Yameen ❤️</strong>"
    "</div>",
    unsafe_allow_html=True
)
