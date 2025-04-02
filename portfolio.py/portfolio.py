import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="💻", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

if page == "Home":
    st.title("Hello every one welcome to my portfolio")
    
    st.header("About Me")
    st.write(
        

"Aswin is a software developerand iot enthustatic with expertise in Python, Flutter, React, Verilog, SQL, IoT, and Frontend Development. His portfolio highlights technical projects, including an Automatic Number Plate Recognition (ANPR) system using OpenCV and a personal website built with React and Flask, demonstrating his ability to build scalable and efficient applications. With a strong foundation in software and hardware development, Aswin is eager to apply his skills in a professional environment through job opportunities and internships. His portfolio provides a clear overview of his skills, projects, and a direct way to connect for potential collaborations."
    )

elif page == "Projects":
    st.header("🚀 Projects")
    projects = [
        {"title": "ANPR System with OpenCV", "description": "Automatic Number Plate Recognition using Python and OpenCV.", "repo": "https://github.com/Aswin29-k/ANPR-technology/commit/f429e057047909245b901b561bead103fcceea0f"},
        {"title": "Portfolio Website", "description": "A personal website built with React and Flask.", "repo": "https://github.com/Aswin29-k/portfolio"},
        {"title": "Solar Tracking System", "description": "A system that automatically adjusts solar panels to track the sun for maximum energy efficiency.", "repo": "https://github.com/Aswin29-k/solar-tracking-system/tree/main"},
        {"title": "Food Website", "description": "A responsive food ordering website with an interactive user interface.", "repo": "https://github.com/Aswin29-k/food-web"},
        {"title": "CRM System", "description": "A Customer Relationship Management (CRM) system to track and manage customer interactions and data.", "repo": "https://github.com/Aswin29-k/crm-app"},
        {"title": "OTP Website Generator", "description": "A web application that generates and verifies one-time passwords for authentication.", "repo": "https://github.com/Aswin29-k/otp-generator/upload"},
        {"title": "BMI Calculator", "description": "A simple web application to calculate Body Mass Index (BMI) based on user input.", "repo": "https://github.com/yourusername/bmi-calculator"},
        {"title": "Furniture Website", "description": "An e-commerce platform for browsing and purchasing furniture online.", "repo": "https://github.com/yourusername/furniture-website"},
        {"title": "Cafe Management System", "description": "A software solution for managing orders, inventory, and customer interactions in a cafe.", "repo": "https://github.com/Aswin29-k/cafe-management-system-using-python"},
        {"title": "Grocery Management System", "description": "A system for managing grocery store inventory, sales, and customer orders efficiently.", "repo": "https://github.com/Aswin29-k/threater-booking-app"},
        {"title": "Flutter CRM App for Students", "description": "A mobile CRM application built with Flutter to help students manage academic and extracurricular activities.", "repo": "https://github.com/yourusername/flutter-crm-students"},
        {"title": "Smart Parking System", "description": "An intelligent parking system that uses sensors and real-time data to optimize parking availability.", "repo": "https://github.com/yourusername/smart-parking-system"},
        {"title": "Machine Learning Project", "description": "An ML-based application leveraging data analysis and predictive modeling for decision-making.", "repo": "https://github.com/Aswin29-k/machinelearning/tree/main"},
        {"title": "Machine Learning crop yeild predetion model", "description": "An ML-based application leveraging data analysis and predictive modeling for decision-making.", "repo": "https://github.com/Aswin29-k/crop-yeid-predection/tree/main"},
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        st.markdown(f"[🔗 View on GitHub]({project['repo']})")

elif page == "Skills":
    st.header("🛠️ Skills")
    skills = ["Python", "Flutter", "React", "Verilog", "SQL", "IoT", "Frontend Development","embedead system"]
    st.write(", ".join(skills))
    st.header("🎓 Education")
    st.write("CARE College of Engineering – B.E. in Electronics and Communication Engineering (ECE)"
"📅 Year of Graduation: [2023-2027] | CGPA: 7.81"

"Saraswathi Vidyalaya – High School"
"📅 Year of Completion: [2023] | Percentage: 76%")

elif page == "Contact":
    st.header("📩 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you for reaching out! I'll get back to you soon.")

# Footer
st.markdown("---")
st.write("@copyrights:Aswinkathaperumal")
st.write("LINKED IN: Aswinkathaperumal")
st.write("GMAIL:kaswin29062006@gmail.com")
