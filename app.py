import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Portfolio | Professional Profile",
    page_icon="👤",
    layout="wide",
)

# 2. Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    st.info("Select a section below to learn more about my background and projects.")
    selection = st.radio("Go to:", ["🏠 Home", "💻 Projects", "📊 Skills", "📞 Contact"])
    st.divider()
    st.caption("Built with Streamlit by [Your Name]")

# 3. Home / Bio Section
if selection == "🏠 Home":
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # Placeholder for a profile image
        st.image("https://via.placeholder.com/300", caption="BSIT Student @ CIT-U")
        
    with col2:
        st.title("Hello, I'm [Classmate's Name] 👋")
        st.subheader("Aspiring IT Professional & Developer")
        st.write("""
            I am a 4th-year Bachelor of Science in Information Technology student at 
            Cebu Institute of Technology - University. I am passionate about solving 
            complex problems through code and building efficient systems.
        """)
        st.markdown("---")
        st.write("📍 Based in Cebu, Philippines")

# 4. Projects Section
elif selection == "💻 Projects":
    st.title("Featured Projects")
    
    # Bento-style grid for projects
    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.container(border=True):
            st.subheader("🚀 Project Alpha")
            st.write("A system designed to streamline [specific task].")
            st.button("View Source Code", key="p1")

    with col_b:
        with st.container(border=True):
            st.subheader("🌐 Web App Beta")
            st.write("A gamified learning platform built using Python.")
            st.button("View Source Code", key="p2")

# 5. Skills Section
elif selection == "📊 Skills":
    st.title("Technical Proficiency")
    
    st.subheader("Programming Languages")
    st.progress(0.9, text="Python")
    st.progress(0.85, text="Java")
    st.progress(0.7, text="C++")

    st.subheader("Tools & Frameworks")
    st.write("`-` Git & GitHub")
    st.write("`-` MySQL / Database Management")
    st.write("`-` Streamlit Cloud")

# 6. Contact Section
elif selection == "📞 Contact":
    st.title("Get In Touch")
    st.write("Feel free to reach out for collaborations or inquiries!")
    
    contact_form = """
    <form action="https://formsubmit.co/your-email@email.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your Message"></textarea>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)