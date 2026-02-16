import streamlit as st
import base64
import os

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Mark Christian Garing | Cloud & DevOps",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper for base64 image
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# ----------------- SESSION STATE & THEME -----------------
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def toggle_theme():
    if st.session_state.theme == 'dark':
        st.session_state.theme = 'light'
    else:
        st.session_state.theme = 'dark'

# Define theme colors
themes = {
    "dark": {
        "bg_dark": "#0a0c10",
        "bg_card": "rgba(22, 27, 34, 0.8)",
        "border_color": "rgba(48, 54, 61, 0.7)",
        "primary": "#58a6ff",
        "text_main": "#c9d1d9",
        "text_bold": "#f0f6fc",
        "text_muted": "#8b949e",
        "hero_bg": "radial-gradient(circle at top right, rgba(31, 111, 235, 0.1), transparent 40%), radial-gradient(circle at bottom left, rgba(35, 134, 54, 0.1), transparent 40%)"
    },
    "light": {
        "bg_dark": "#ffffff",
        "bg_card": "rgba(255, 255, 255, 0.9)",
        "border_color": "#d0d7de",
        "primary": "#0969da",
        "text_main": "#24292f",
        "text_bold": "#1f2328",
        "text_muted": "#57606a",
        "hero_bg": "radial-gradient(circle at top right, rgba(9, 105, 218, 0.1), transparent 40%), radial-gradient(circle at bottom left, rgba(33, 169, 58, 0.1), transparent 40%)"
    }
}

current_theme = themes[st.session_state.theme]

# ----------------- CUSTOM CSS -----------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

:root {{
    --bg-dark: {current_theme['bg_dark']};
    --bg-card: {current_theme['bg_card']};
    --border-color: {current_theme['border_color']};
    --primary: {current_theme['primary']};
    --text-main: {current_theme['text_main']};
    --text-bold: {current_theme['text_bold']};
    --text-muted: {current_theme['text_muted']};
}}

/* Global Reset */
.stApp {{
    background-color: var(--bg-dark);
    font-family: 'Outfit', sans-serif;
    color: var(--text-main);
}}

h1, h2, h3, h4, h5, h6 {{
    color: var(--text-bold) !important;
    font-family: 'Outfit', sans-serif !important;
}}

code {{
    font-family: 'JetBrains Mono', monospace !important;
}}

/* Sidebar Customization */
[data-testid="stSidebar"] {{
    background-color: { "#f6f8fa" if st.session_state.theme == "light" else "#0d1117" };
    border-right: 1px solid var(--border-color);
}}

/* Compact Sidebar Radio */
.stRadio > div {{
    gap: 0px;
}}
.stRadio label {{
    padding-top: 4px !important;
    padding-bottom: 4px !important;
}}

/* HERO SECTION */
.hero-container {{
    padding: 3rem 2rem;
    background: {current_theme['hero_bg']};
    border-radius: 16px;
    border: 1px solid var(--border-color);
    margin-bottom: 2rem;
    text-align: center;
    backdrop-filter: blur(10px);
}}

.hero-title {{
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
    color: var(--text-bold);
}}

.hero-subtitle {{
    font-size: 1.25rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 2rem;
}}

/* INFO CARDS */
.glass-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}}

.glass-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border-color: var(--primary);
}}

.card-header {{
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.card-content {{
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-main);
}}

/* SKILL BADGES */
.skill-badge {{
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    margin: 4px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    background: rgba(88, 166, 255, 0.15);
    color: var(--primary);
    border: 1px solid rgba(88, 166, 255, 0.3);
    transition: all 0.2s;
}}

/* TIMELINE */
.timeline-item {{
    border-left: 2px solid var(--border-color);
    padding-left: 1.5rem;
    margin-bottom: 2rem;
    position: relative;
    margin-left: 1rem;
}}

.timeline-item::before {{
    content: '';
    position: absolute;
    left: -6px;
    top: 0;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--primary);
    box-shadow: 0 0 10px var(--primary);
}}

.timeline-date {{
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
    font-family: 'JetBrains Mono', monospace;
}}

/* CONTACT LINKS */
.contact-link {{
    display: flex;
    align-items: center;
    padding: 1rem;
    background: { "rgba(240, 240, 240, 0.5)" if st.session_state.theme == "light" else "rgba(48, 54, 61, 0.3)" };
    border-radius: 8px;
    color: var(--text-main);
    text-decoration: none;
    margin-bottom: 0.5rem;
    border: 1px solid transparent;
    transition: all 0.2s;
}}

.contact-link:hover {{
    border-color: var(--primary);
    text-decoration: none;
    transform: translateX(5px);
}}

/* PROFILE PICTURE CIRCLE */
.profile-pic-container {{
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
}}

.profile-pic-container img {{
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid var(--primary);
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    aspect-ratio: 1 / 1;
    display: block;
}}

</style>
""", unsafe_allow_html=True)

# ----------------- COMPONENT FUNCTIONS -----------------

def render_hero():
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Mark Christian Garing</div>
            <div class="hero-subtitle">&lt;Compiling Success... /&gt; | BSIT-4 | Future DevOps & Cloud Engineer</div>
            <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto; line-height: 1.6;">
                Building bridges between code and infrastructure. Passionate about automating the mundane, 
                optimizing the complex, and scaling the impossible.
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_card(title, content, icon="🔹"):
    st.markdown(f"""
        <div class="glass-card">
            <div class="card-header">
                <span>{icon}</span> {title}
            </div>
            <div class="card-content">
                {content}
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_timeline(date, title, description):
    st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-date">{date}</div>
            <h4 style="margin: 0; color: var(--text-bold);">{title}</h4>
            <div style="color: var(--text-main); font-size: 0.95rem; margin-top: 5px;">{description}</div>
        </div>
    """, unsafe_allow_html=True)

def render_skills(skills_list):
    html = '<div style="margin-top: 10px;">'
    for skill in skills_list:
        html += f'<span class="skill-badge">{skill}</span>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_contact(icon, platform, handle, link):
    st.markdown(f"""
        <a href="{link}" target="_blank" class="contact-link">
            <span class="icon">{icon}</span>
            <div style="flex-grow: 1;">
                <div style="font-weight: 600; font-size: 0.9rem; color: var(--text-bold);">{platform}</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">{handle}</div>
            </div>
            <span style="color: var(--primary);">→</span>
        </a>
    """, unsafe_allow_html=True)

# ----------------- NAVIGATION -----------------



# Theme Toggle
# Theme Toggle
is_dark_mode = st.session_state.theme == "dark"
toggle_val = st.sidebar.toggle("Dark Mode" if is_dark_mode else "Light Mode", value=is_dark_mode)

if toggle_val != is_dark_mode:
    st.session_state.theme = "dark" if toggle_val else "light"
    st.rerun()

# Navigation Selection
page = st.sidebar.radio("Navigate", ["Dashboard", "Journey", "Projects", "Stack", "Connect"], label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style="text-align: center; color: var(--text-muted); font-size: 0.8rem;">
        &copy; 2024 Mark Christian Garing<br>
        Designed with Streamlit
    </div>
""", unsafe_allow_html=True)

# ----------------- PAGES -----------------

if page == "Dashboard":
    render_hero()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🚀 Objectives")
        render_card(
            "Mission Statement", 
            "To leverage my skills in IT and passion for cloud technologies to build robust, scalable infrastructure. "
            "I aim to master the art of DevOps, ensuring seamless CI/CD pipelines and efficient cloud resource management.",
            icon="🎯"
        )
        
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            render_card("Focus Area", "Cloud Automation & Infrastructure as Code (IaC)", icon="⚡")
        with col_sub2:
            render_card("Current Status", "BSIT Senior Year | Seeking Internship/Entry Roles", icon="🎓")

    with col2:
        st.subheader("🔗 Quick Links")
        render_contact('<img src="https://img.icons8.com/fluent/48/000000/github.png" width="30"/>', "GitHub", "@heisenberrg19", "https://github.com/heisenberrg19")
        render_contact('<img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30"/>', "LinkedIn", "Mark Christian Garing", "https://linkedin.com/in/yourprofile")
        
        st.subheader("💡 Highlight")
        st.info("Currently diving deep into AWS services and Docker containerization patterns.")

elif page == "Journey":
    st.title("Autobiography")
    
    st.markdown("""
<div style="font-size: 1.05rem; line-height: 1.7; color: var(--text-main); margin-bottom: 2rem;">
<p>My name is Mark Christian Garing, a fourth-year Bachelor of Science in Information Technology (BSIT-4) student with a strong interest in modern computing technologies and system infrastructure. I chose Information Technology because I am passionate about solving technical problems, building systems, and understanding how software and hardware work together to support real-world applications.</p>

<p>Throughout my academic journey, I have developed foundational skills in programming, web development, and system design. I enjoy working on projects that challenge my logical thinking and creativity. Each project I complete strengthens my discipline, teamwork, and problem-solving abilities, which I consider essential qualities for a successful career in the tech industry.</p>

<p>My long-term goal is to become a DevOps Engineer or Cloud Engineer. I am particularly interested in cloud platforms, automation, infrastructure management, and deployment pipelines. I aspire to work in an environment where I can continuously learn new technologies and contribute to building scalable and secure systems. I believe that dedication, continuous learning, and hands-on experience will help me reach my professional goals.</p>
</div>

<h3 style="margin-bottom: 20px;">Key Milestones</h3>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    render_timeline(
        "2023 - Present", 
        "DevOps & Cloud Enthusiasm", 
        "Started focusing heavily on backend systems, Linux administration, and cloud platforms (AWS). "
        "Building projects with Docker and CI/CD pipelines."
    )
    
    render_timeline(
        "2020 - Present", 
        "Bachelor of Science in Information Technology", 
        "Maintaining high academic standing. Leader in multiple collaborative programming projects. "
        "Focus on Systems Administration and Web Development."
    )
    
    render_timeline(
        "2018 - 2020", 
        "Early Programming Days", 
        "Discovered passion for code through basic web development (HTML/CSS) and Python scripting. "
        "Solved algorithmic problems and built small automation scripts."
    )

elif page == "Projects":
    st.title("Project Portfolio")
    st.markdown("A collection of my personal work, forks, and collaborations.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_card(
            "ThriftShirtPawnshop",
            "A web and mobile system for digital pawn lending and thrift resale using Kotlin, Spring Boot, ReactJS, and MySQL.",
            icon="👕"
        )
        render_card(
            "MetaDoc Evaluator",
            "Software Project Proposal Evaluator. A tool to assess and streamline software proposals. (Collab with EdQuinJr)",
            icon="📑"
        )
        render_card(
            "EASYSTAY",
            "A Hotel Management Booking System to streamline reservations and guest management. Built with PHP.",
            icon="🏨"
        )
        render_card(
            "Wildtrack",
            "A system for tracking or monitoring wildlife/environmental data. (Collab with IamJesssie)",
            icon="🐾"
        )
        render_card(
            "ExpenseTracker",
            "Personal finance management tool to track income and expenses. (Collab with IamJesssie)",
            icon="💸"
        )

    with col2:
        render_card(
            "IndustryE",
            "Industrial management or enterprise resource platform. (Collab with vyn23232)",
            icon="🏭"
        )
        render_card(
            "CSIT360 NotesApp",
            "A collaborative notes application for organizing study materials and personal memos. (Collab with princeprog)",
            icon="📝"
        )
        render_card(
            "AttendanceSystem",
            "System for tracking attendance in educational or corporate settings. (Collab with ryukiaaa)",
            icon="📅"
        )
        render_card(
            "IT334 Midterm Project",
            "Academic project codebase demonstrating software engineering principles.",
            icon="💻"
        )

elif page == "Stack":
    st.title("Tech Stack & Skills")
    
    st.subheader("Core Technologies")
    render_skills(["Python", "Java", "Kotlin", "PHP", "JavaScript", "ReactJS", "Spring Boot", "SQL", "Git", "HTML5", "CSS3"])
    
    st.subheader("Cloud & DevOps")
    render_skills(["Linux Administration", "Networking", "Docker", "AWS (Basic)", "CI/CD Concepts", "Version Control"])
    
    st.subheader("Soft Skills")
    render_skills(["Problem Solving", "Team Leadership", "Technical Writing", "Agile Methodology"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image("https://skillicons.dev/icons?i=python,java,kotlin,php,js,react,spring,linux,git,docker,mysql,aws,vscode,github", caption="My Daily Drivers")

elif page == "Connect":
    st.title("Let's Connect!")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
            I am always open to discussing new projects, creative ideas, or opportunities to be part of your visions.
            
            **Mark Christian Garing**  
            *Aspiring DevOps Engineer*
            
            Feel free to reach out for collaborations or just a friendly hello!
        """)
        


        # Profile Picture with Custom Circle Styling
        img_path = "profile.jpg"
        img_base64 = get_base64_image(img_path)
        
        if img_base64:
            img_src = f"data:image/jpeg;base64,{img_base64}"
        else:
            img_src = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
            
        st.markdown(f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div class="profile-circle"></div>
            </div>
            <style>
                .profile-circle {{
                    width: 250px;
                    height: 250px;
                    border-radius: 50%;
                    background-image: url('{img_src}');
                    background-size: cover;
                    background-position: center;
                    border: 4px solid var(--primary);
                    box-shadow: 0 0 0 6px rgba(88, 166, 255, 0.2), 0 0 20px rgba(88, 166, 255, 0.6);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }}
                .profile-circle:hover {{
                    transform: scale(1.02);
                    box-shadow: 0 0 0 8px rgba(88, 166, 255, 0.3), 0 0 30px rgba(88, 166, 255, 0.8);
                }}
            </style>
        """, unsafe_allow_html=True)
        
    with col2:
        render_contact('<img src="https://img.icons8.com/fluent/48/000000/mail.png" width="30"/>', "Email", "garing.markchristian@gmail.com", "mailto:garing.markchristian@gmail.com")
        render_contact('<img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30"/>', "LinkedIn", "linkedin.com/in/yourprofile", "https://linkedin.com/in/yourprofile")
        render_contact('<img src="https://img.icons8.com/fluent/48/000000/github.png" width="30"/>', "GitHub", "github.com/heisenberrg19", "https://github.com/heisenberrg19")
