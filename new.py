# Define a function to print resume details
def print_resume():
    resume = {
        "Profile": "Full Stack Developer",
        "Summary": """Dedicated FullStack Developer with 6 months of internship experience at Besant Technologies. 
Hands-on with SQL, HTML5, CSS3, JavaScript, ReactJs, and JAVA. Eager to contribute to dynamic projects and expand skill set within collaborative teams.""",
        "Internship Experience": {
            "Company": "Besant Technologies",
            "Duration": "April/2024 - Present",
            "Role": "FullStack Developer",
            "Responsibilities": [
                "Created dynamic, responsive, and interactive user interfaces (UIs) using HTML5, CSS3, JavaScript.",
                "Developed and maintained both frontend and backend components of web applications using Java and JavaScript.",
                "Collaborated with senior developers to understand project requirements and contribute to codebases."
            ]
        },
        "Education": [
            {
                "Institution": "Sri Krishna College of Engineering and Technology",
                "Degree": "B.E- Electrical and Electronics Engineering",
                "CGPA": 9.25,
                "Location": "Coimbatore, Tamil Nadu",
                "Year": "2019 - 2023"
            },
            {
                "Institution": "Vikas Vidhyalaya Matric School",
                "Degree": "XII",
                "Percentage": 86.8,
                "Location": "Tiruppur, Tamil Nadu",
                "Year": "2018 - 2019"
            },
            {
                "Institution": "Kongu Vellalar Matric School",
                "Degree": "X",
                "Percentage": 98.6,
                "Location": "Tiruppur, Tamil Nadu",
                "Year": "2016 - 2017"
            }
        ],
        "Coursework / Skills": {
            "Front-end": ["HTML", "CSS", "JavaScript", "ReactJs"],
            "Back-end": ["Java", "Spring Boot"],
            "Databases": ["MySQL"],
            "CSS Frameworks": ["Bootstrap"]
        },
        "Projects": [
            {
                "Name": "Property Expert",
                "Type": "Web Application",
                "Technologies": ["HTML5", "CSS3", "JavaScript"],
                "Description": "Real estate website project allowing users to search for properties and connect with property owners or agents."
            },
            {
                "Name": "Bus Reservation System",
                "Type": "Console Application",
                "Technologies": ["Java"],
                "Description": "Console-level bus reservation system allowing users to view and book buses for a particular date."
            },
            {
                "Name": "Taxi Booking Application",
                "Type": "Console Application",
                "Technologies": ["Java"],
                "Description": "Taxi booking system where passengers can book a taxi by entering their pickup and drop locations."
            }
        ],
        "Certifications": [
            "Java SE-8 Programmer - ORACLE",
            "Full-Stack Java Development - Besant Technologies"
        ]
    }

    # Print the resume in a structured format
    print(f"Profile: {resume['Profile']}\n")
    print(f"Summary:\n{resume['Summary']}\n")

    # Print Internship Experience
    print("Internship Experience:")
    print(f"Company: {resume['Internship Experience']['Company']}")
    print(f"Duration: {resume['Internship Experience']['Duration']}")
    print(f"Role: {resume['Internship Experience']['Role']}")
    print("Responsibilities:")
    for responsibility in resume['Internship Experience']['Responsibilities']:
        print(f"- {responsibility}")
    print("\n")

    # Print Education
    print("Education:")
    for edu in resume["Education"]:
        print(f"{edu['Degree']} - {edu['Institution']}")
        print(f"CGPA/Percentage: {edu.get('CGPA', edu.get('Percentage'))}")
        print(f"Location: {edu['Location']} | Year: {edu['Year']}")
    print("\n")

    # Print Skills
    print("Skills:")
    for category, skills in resume["Coursework / Skills"].items():
        print(f"{category}: {', '.join(skills)}")
    print("\n")

    # Print Projects
    print("Projects:")
    for project in resume["Projects"]:
        print(f"{project['Name']} - {project['Type']}")
        print(f"Technologies: {', '.join(project['Technologies'])}")
        print(f"Description: {project['Description']}\n")

    # Print Certifications
    print("Certifications:")
    for cert in resume["Certifications"]:
        print(f"- {cert}")


# Call the function to display the resume
print_resume()