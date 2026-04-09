from flask import Flask, render_template

app = Flask(__name__)

# Portfolio Data - Easy to edit
portfolio_data = {
    "personal": {
        "name": "Ravi Kumar Mohane",
        "role": "Network Data Specialist | Automation Test Engineer | Full Stack Developer",
        "bio": "I am a dedicated Network Data Specialist and Automation Test Engineer with a deep-rooted passion for architecting robust network infrastructures and streamlining software quality through advanced automation. With a B.Tech and M.Tech in Computer Science Engineering from SIRT Bhopal, I have cultivated a unique intersection of networking expertise and full-stack development capability. My journey includes hands-on internships in Cyber Security (Penetration Testing & Bug Bounty) and .NET development, allowing me to build secure, scalable, and high-performance digital solutions. I thrive on solving complex technical challenges, whether it's optimizing network data flow or building AI-driven assistants that push the boundaries of modern technology. My goal is to leverage my multi-disciplinary expertise to deliver state-of-the-art technological experiences.",
        "dob": "22/09/2000",
        "father_name": "Gajanand Mohane",
        "location": "At Tawla, Post Bihargaon, Tehsil Multai, Dist. Betul, Madhya Pradesh",
        "nationality": "Indian",
        "languages": "Hindi, English",
        "email": "ravikumarmohane@gmail.com",
        "phone": ["7247518285", "9285180577"],
        "social": {
            "github": "https://github.com/en-rmohane?tab=repositories",
            "linkedin": "https://www.linkedin.com/in/ravi-kumar-mohane-58094421a/",
            "instagram": "https://www.instagram.com/ravikumar__mohane/"
        }
    },
    "skills": [
        {"name": "Python", "level": 90, "icon": "fa-brands fa-python"},
        {"name": "Flask", "level": 85, "icon": "fa-solid fa-flask"},
        {"name": "JavaScript", "level": 95, "icon": "fa-brands fa-js"},
        {"name": "HTML/CSS", "level": 100, "icon": "fa-brands fa-css3-alt"},
        {"name": "React", "level": 80, "icon": "fa-brands fa-react"},
        {"name": "PostgreSQL", "level": 75, "icon": "fa-solid fa-database"},
        {"name": "Networking", "level": 85, "icon": "fa-solid fa-network-wired"},
        {"name": "Cyber Security", "level": 80, "icon": "fa-solid fa-user-shield"},
        {"name": "Protocols (TCP/IP, HTTP/S, DNS, SSH, DHCP)", "level": 90, "icon": "fa-solid fa-shield-halved"}
    ],
    "education": [
        {
            "degree": "M.Tech in Computer Science Engineering",
            "institution": "Sagar Institute of Research and Technology, Bhopal",
            "period": "2022 - 2024",
            "description": "Specializing in Advanced Engineering Research."
        },
        {
            "degree": "B.Tech in Computer Science Engineering",
            "institution": "Sagar Institute of Research Technology and Science, Bhopal",
            "period": "2018 - 2022",
            "description": "Bachelor of Technology."
        },
        {
            "degree": "12th Standard",
            "institution": "New Betul Higher Secondary School, Betul",
            "period": "2016 - 2018",
            "description": "Science Stream."
        },
        {
            "degree": "10th Standard",
            "institution": "G.H.S Bihargaon",
            "period": "2015 - 2016",
            "description": "General Schooling."
        }
    ],
    "experience": [
        {
            "company": "NG Networks",
            "role": "Network Data Specialist",
            "period": "2025",
            "description": "Specializing in network data analysis, routing, and switching infrastructure."
        },
        {
            "company": "BridgeLabz",
            "role": ".NET Internship",
            "period": "2022",
            "description": "Engaged in .NET development, learning core frameworks and building scalable applications."
        },
        {
            "company": "Drop Org, Kolkata",
            "role": "Cyber Security Internship",
            "period": "2021",
            "description": "Focused on Penetration Testing and Bug Bounty programs, identifying vulnerabilities and securing digital assets."
        }
    ],
    "projects": [
        {
            "title": "College Attendance ERP",
            "description": "A comprehensive cloud-based attendance and resource management system for students and staff.",
            "image": "/static/images/erp.png",
            "tech": ["Flask", "PostgreSQL", "React"],
            "link": "https://sbitmattendance.vercel.app/"
        },
        {
            "title": "Official College Website",
            "description": "The official digital portal for SBITM Betul, featuring academic resources and department info.",
            "image": "/static/images/sbitm.png",
            "tech": ["HTML/CSS", "JavaScript", "SEO"],
            "link": "https://sbitmbetul.vercel.app/"
        },
        {
            "title": "Desktop Automation",
            "description": "Streamlined workflow automation using Python, Selenium, and PyAutoGUI to handle repetitive tasks.",
            "image": "/static/images/project1.png",
            "tech": ["Python", "Selenium", "PyAutoGUI"],
            "link": "https://github.com/en-rmohane?tab=repositories"
        },
        {
            "title": "Personal AI Assistant",
            "description": "An intelligent virtual assistant capable of handling schedules and answering complex queries.",
            "image": "/static/images/project2.png",
            "tech": ["Python", "OpenAI", "NLTK"],
            "link": "https://github.com/en-rmohane?tab=repositories"
        },
        {
            "title": "Spiritual AI Guru",
            "description": "A niche AI system trained to provide spiritual guidance and wisdom based on ancient texts.",
            "image": "/static/images/hero-bg.png",
            "tech": ["NLP", "Transformers", "Python"],
            "link": "https://github.com/en-rmohane?tab=repositories"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
