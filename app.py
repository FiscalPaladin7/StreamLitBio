import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Joseph Ericson A. Tiu | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* --- SIDEBAR STYLING FIX --- */
    /* Force sidebar background to be white and text to be dark grey */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    /* Force all text inside sidebar to be dark, regardless of theme */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #333333 !important;
    }
    
    /* Custom headers in main area */
    h1, h2, h3 {
        color: #0e1117; 
        /* In dark mode, you might want these white. If the main bg is black, change this to #ffffff */
    }
    
    /* Card styling for projects */
    .stContainer {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA & VARIABLES ---
NAME = "Joseph Ericson A. Tiu"
BIRTHDATE = date(2001, 4, 12)
LOCATION = "341-B F. Jaca Street, Inayawan, Cebu City"
ROLE = "BSIT Student @ CIT-U"
EMAIL = "FiscalPaladin7@gmail.com"
PHONE = "+63 976 050 7513"
GITHUB_LINK = "https://github.com/FiscalPaladin7"

def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

current_age = get_age(BIRTHDATE)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    # Profile Picture Placeholder
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    
    st.title(NAME)
    st.write(f"🎓 {ROLE}")
    st.write(f"🎂 {BIRTHDATE.strftime('%B %d, %Y')} ({current_age} y/o)")
    st.write(f"📍 {LOCATION}")
    
    st.markdown("---")
    
    # Improved Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Profile", "Education", "Tech Stack", "Projects", "Contact"], 
        icons=["person-circle", "book-half", "cpu", "code-slash", "envelope"], 
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#ff4b4b", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#f0f2f6", "color": "#333333"},
            "nav-link-selected": {"background-color": "#ff4b4b", "color": "white !important"},
        }
    )
    
    st.markdown("---")
    st.caption("© 2026 Joseph Tiu. All Rights Reserved.")


# --- MAIN CONTENT ---

# 1. PROFILE SECTION
if selected == "Profile":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title(f"Hello, I'm Joseph! 👋")
        st.subheader("Aspiring IT Specialist & Systems Developer")
        
        # Objective text
        st.info("""
        **OBJECTIVE**
        
        Motivated and enthusiastic individual with a strong intention to learn and improve the 
        skills that I gained all throughout the academic years. I also possess a strong 
        willingness to adapt quickly into a new environment. Lastly, to work in an environment 
        which encourages me to succeed and grow professionally where I can utilize my skills 
        and knowledge appropriately.
        """)
        
        st.markdown("### Key Stats")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="Years Coding", value="3+")
        with c2:
            st.metric(label="Projects", value="10+")
        with c3:
            st.metric(label="Coffee Intake", value="∞")

    with col2:
        st.markdown("### Connect")
        st.button("📄 Download Resume")
        # FIXED: Direct link button to GitHub
        st.link_button("🐙 Visit GitHub", GITHUB_LINK)


# 2. EDUCATION SECTION
elif selected == "Education":
    st.title("📚 Academic Journey")
    
    # College
    st.header("Cebu Institute of Technology - University")
    st.subheader("Bachelor of Science in Information Technology")
    st.caption("2020 - Present | Cebu City")
    st.write("""
    - **Relevant Coursework:** Data Structures & Algorithms, Object Oriented Programming, Networking 101, Systems Administration.
    - **Activities:** Member of the CIT-U College of Computer Studies Council.
    """)
    st.divider()
    
    # Senior High School
    st.header("Cebu Institute of Technology - University")
    st.subheader("Senior High School (STEM)")
    st.caption("2018 - 2020")
    st.write("Focus on Science, Technology, Engineering, and Mathematics.")
    st.divider()

    # Junior High School
    st.header("Holy Rosary School of Pardo")
    st.subheader("Junior High School")
    st.caption("2014 - 2018")
    st.write("Completed Junior High School education with a strong foundation in basic sciences and mathematics.")


# 3. TECH STACK (Proficiencies)
elif selected == "Tech Stack":
    st.title("🛠️ Technical Proficiencies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Programming Languages")
        st.code("Python  |  Java  |  C++  |  SQL", language="text")
        
        st.write("**Python (Data & Scripting)**")
        st.progress(85)
        st.write("**Java (OOP)**")
        st.progress(75)
        st.write("**HTML/CSS (Web Design)**")
        st.progress(90)

    with col2:
        st.subheader("Tools & Technologies")
        
        # FIXED: Replaced JSON block with readable list
        st.markdown("""
        **💻 Development Environments**
        - VS Code
        - PyCharm
        - IntelliJ
        
        **🐙 Version Control**
        - Git & GitHub
        
        **🗄️ Databases**
        - MySQL
        - Firebase
        """)
        
        st.markdown("### Core Competencies")
        st.success("✅ Systems Analysis")
        st.success("✅ Network Troubleshooting")
        st.success("✅ UI/UX Prototyping")


# 4. PROJECTS SECTION
elif selected == "Projects":
    st.title("💻 Project Showcase")
    st.write("Here are some of the key projects I've worked on during my academic career.")
    
    tab1, tab2 = st.tabs(["Web Development", "System Admin"])
    
    with tab1:
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("Project A: E-Commerce Dashboard")
            st.image("https://via.placeholder.com/400x200?text=Dashboard+Preview", caption="Admin Panel")
            st.write("A Python-based dashboard for tracking sales and inventory metrics.")
            st.link_button("View Code", GITHUB_LINK)
            
        with col_b:
            st.subheader("Project B: Student Portal")
            st.image("https://via.placeholder.com/400x200?text=Portal+Preview", caption="Login Interface")
            st.write("A secure login system for students to check grades and schedules.")
            st.link_button("View Code", GITHUB_LINK)
            
    with tab2:
        st.warning("🚧 System Administration projects coming soon!")


# 5. CONTACT SECTION
elif selected == "Contact":
    st.title("📞 Get In Touch")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.")
        st.markdown(f"""
        📧 **Email:** [{EMAIL}](mailto:{EMAIL})  
        📱 **Phone:** {PHONE}  
        📍 **Address:** {LOCATION}
        """)
        
    with col2:
        st.container(border=True)
        with st.form("contact_form"):
            st.header("Send a Message")
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            
            if submit:
                st.success("Thanks! I'll get back to you soon.")