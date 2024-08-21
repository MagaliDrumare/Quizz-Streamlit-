import streamlit as st

# Questions and choices
questions = {
    "What is the primary function of Microsoft Copilot for Microsoft 365?": [
        "To automate routine administrative tasks",
        "To enhance creativity, productivity, and understanding using LLMs",
        "To provide security solutions",
        "To manage email exclusively"
    ],
    "How does Microsoft Copilot integrate with Dynamics 365 applications?": [
        "By providing security enhancements",
        "By offering intelligent assistance in sales, customer service, and more",
        "By managing social media accounts",
        "By solely handling marketing content"
    ],
    "What does Microsoft Copilot Studio primarily offer?": [
        "Advanced analytics tools",
        "A low-code tool for creating AI-powered conversational interfaces",
        "High-code development environments",
        "Database management services"
    ],
    "What is a distinctive feature of GitHub Copilot?": [
        "It provides real-time security monitoring",
        "It offers real-time code suggestions in IDEs",
        "It focuses on hardware integration",
        "It automates user interface design"
    ],
    "How does Microsoft Fabric enhance data management?": [
        "By providing a unified platform combining multiple Microsoft services",
        "By offering manual data processing tools",
        "By focusing on non-AI-powered solutions",
        "By decentralizing data storage"
    ],
    "What is the key difference between OpenAI’s direct offerings and Azure OpenAI Service?": [
        "Azure OpenAI Service does not use AI models",
        "OpenAI offers direct cloud hosting, while Azure integrates with Microsoft cloud services",
        "OpenAI restricts access to its models to non-commercial use",
        "Azure OpenAI Service is less secure"
    ],
    "In what way is Microsoft Copilot adapted for mobile devices?": [
        "It enhances device hardware performance",
        "It is available through a mobile app",
        "It only functions when connected to desktop devices",
        "It manages mobile device storage"
    ],
    "What are the functionalities of Microsoft Copilot within Dynamics 365 for supply chain management?": [
        "Provides insights and automates routine tasks",
        "Handles only customer service requests",
        "Focuses on manual data entry",
        "Enhances only financial reporting"
    ],
    "What type of AI technology does GitHub Copilot utilize to assist developers?": [
        "Large language models",
        "Basic automation scripts",
        "Non-AI algorithms",
        "Simple heuristic models"
    ],
    "What aspect of Microsoft Fabric's capabilities focuses on real-time data handling?": [
        "Real-time data ingestion and event routing",
        "Delayed batch processing",
        "Manual data sorting",
        "Offline data analysis"
    ]
}

# Correct answers
correct_answers = {
    "What is the primary function of Microsoft Copilot for Microsoft 365?": "To enhance creativity, productivity, and understanding using LLMs",
    "How does Microsoft Copilot integrate with Dynamics 365 applications?": "By offering intelligent assistance in sales, customer service, and more",
    "What does Microsoft Copilot Studio primarily offer?": "A low-code tool for creating AI-powered conversational interfaces",
    "What is a distinctive feature of GitHub Copilot?": "It offers real-time code suggestions in IDEs",
    "How does Microsoft Fabric enhance data management?": "By providing a unified platform combining multiple Microsoft services",
    "What is the key difference between OpenAI’s direct offerings and Azure OpenAI Service?": "OpenAI offers direct cloud hosting, while Azure integrates with Microsoft cloud services",
    "In what way is Microsoft Copilot adapted for mobile devices?": "It is available through a mobile app",
    "What are the functionalities of Microsoft Copilot within Dynamics 365 for supply chain management?": "Provides insights and automates routine tasks",
    "What type of AI technology does GitHub Copilot utilize to assist developers?": "Large language models",
    "What aspect of Microsoft Fabric's capabilities focuses on real-time data handling?": "Real-time data ingestion and event routing"
}

# Streamlit user interface
def main():
    st.title("Microsoft Generative AI Quiz")

    # User responses
    user_answers = {}
    for q, choices in questions.items():
        answer = st.radio(q, choices, key=q)
        user_answers[q] = answer

    if st.button("Submit"):
        correct_count = sum([user_answers[q] == correct_answers[q] for q in questions])
        st.write(f"You got {correct_count}/{len(questions)} correct answers.")
        for q in questions:
            if user_answers[q] == correct_answers[q]:
                st.success(f"Correct! {q}: {user_answers[q]}")
            else:
                st.error(f"Incorrect! {q}: {user_answers[q]}")
                st.write(f"The correct answer was: {correct_answers[q]}")

if __name__ == "__main__":
    main()
