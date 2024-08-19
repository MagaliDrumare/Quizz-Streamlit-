import streamlit as st

# Define quiz questions, options, and correct answers
quiz_data = [
    {"question": "What is the name of the event that the transcript details?",
     "options": ["Data Dev Day", "Innovation Preview", "Dreamforce", "Einstein Day"],
     "answer": "Innovation Preview"},
    {"question": "Who is Elizabeth Maxon in the context of the event?",
     "options": ["CEO of Tableau", "Chief Marketing Officer for Tableau", "Special Guest Speaker", "Tableau Visionary"],
     "answer": "Chief Marketing Officer for Tableau"},
    {"question": "What is Salesforce Einstein Trust Layer primarily known for?",
     "options": ["A gateway to generative AI models", "A data visualization tool", "A CRM platform", "A marketing analytics tool"],
     "answer": "A gateway to generative AI models"},
    {"question": "Which new technology infrastructure was mentioned as providing scalability and security?",
     "options": ["Data Cloud", "Hyperforce", "Einstein Co-pilot", "VizQL"],
     "answer": "Hyperforce"},
    {"question": "What significant growth metrics about Tableau community were mentioned?",
     "options": ["Over 4 million Tableau Public profiles", "Over 5 million Tableau Public visits", "23,000 global user group members", "All of the above"],
     "answer": "All of the above"},
    {"question": "Which new feature in Tableau allows for creating internal marketplaces for analytics components?",
     "options": ["Data Cloud", "Tableau Pulse", "Einstein Semantics", "Composable architecture"],
     "answer": "Composable architecture"},
    {"question": "What is the main purpose of Tableau Pulse for Salesforce as introduced in the event?",
     "options": ["To manage CRM data effectively", "To provide out-of-box metrics like win rates", "To analyze customer feedback data", "To integrate with AI insights"],
     "answer": "To provide out-of-box metrics like win rates"},
    {"question": "Which major Salesforce event is mentioned as an upcoming opportunity to learn more about Tableau innovations?",
     "options": ["Salesforce Live", "Dreamforce", "Salesforce Summit", "Einstein Analytics Day"],
     "answer": "Dreamforce"},
    {"question": "What is 'Einstein Co-pilot for Tableau' primarily designed to assist with?",
     "options": ["Building advanced AI models", "Enhancing user engagement with data", "Automating data entry tasks", "Guiding users in creating visuals"],
     "answer": "Guiding users in creating visuals"},
    {"question": "According to the transcript, what does 'Data Cloud' primarily focus on?",
     "options": ["Storing data", "Enhancing data security", "Improving customer experiences by unifying data", "Providing AI-powered insights"],
     "answer": "Improving customer experiences by unifying data"},
    {"question": "Which key feature does Hyperforce provide according to the transcript?",
     "options": ["Predictive analytics tools", "Global cloud infrastructure", "Local data storage solutions", "In-house data processing"],
     "answer": "Global cloud infrastructure"},
    {"question": "What significant new feature was announced for the Tableau platform, aimed at enhancing user interaction with data?",
     "options": ["Local file saving", "Desktop public edition", "AI assistance in prep and catalog", "All of the above"],
     "answer": "All of the above"},
    {"question": "According to the transcript, what is the main benefit of leveraging Salesforce's Einstein Trust Layer for Tableau?",
     "options": ["Increased data visualization options", "Enhanced data privacy and security", "Improved user interface design", "Expanded integration with third-party apps"],
     "answer": "Enhanced data privacy and security"},
    {"question": "What does 'composable architecture' in Tableau refer to?",
     "options": ["A method for integrating various software components", "A new infrastructure for cloud services", "A marketplace for sharing internal analytics components", "An architectural design for better user experience"],
     "answer": "A marketplace for sharing internal analytics components"},
    {"question": "Which event specifically focused on Tableau developers is mentioned in the transcript?",
     "options": ["Dreamforce", "Data Dev Day", "Tableau Conference", "Salesforce Summit"],
     "answer": "Data Dev Day"},
    {"question": "What role does 'Einstein semantics' play in the new Tableau features?",
     "options": ["It's an AI tool for generating text-based data insights.", "It serves as a semantic translation layer between raw data and business insights.", "It's a new interface design element for Tableau dashboards.", "It's a security feature for data governance."],
     "answer": "It serves as a semantic translation layer between raw data and business insights."},
    {"question": "According to the transcript, what does the 'Data Cloud' enable beyond bringing data together?",
     "options": ["Enhancing cloud storage capacity", "Facilitating better data analytics", "Unifying organizations around the customer", "Simplifying data entry processes"],
     "answer": "Unifying organizations around the customer"},
    {"question": "What is the main functionality of 'Hyperforce' as discussed in the event?",
     "options": ["To provide AI analytics", "To offer a secure cloud infrastructure", "To enable faster data processing", "To improve data visualization techniques"],
     "answer": "To offer a secure cloud infrastructure"},
    {"question": "What new feature related to 'relationships' and 'spell check' is mentioned for the latest release of Tableau?",
     "options": ["Multi-relationships", "Spell check in web authoring", "Both A and B", "Neither A nor B"],
     "answer": "Both A and B"},
    {"question": "What is the key focus of the new event, 'Data Fam Europe'?",
     "options": ["To expand Tableau's user community in Europe", "To introduce new Tableau features to the European market", "To focus on data development and AI integration", "To showcase Tableau's new architectural changes"],
     "answer": "To expand Tableau's user community in Europe"}
]

# Initialize session state variables if not already initialized
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

def handle_answer(answer, correct_answer):
    if answer == correct_answer:
        st.session_state.score += 1
    st.session_state.question_index += 1

# Display current question
if st.session_state.question_index < len(quiz_data):
    question = quiz_data[st.session_state.question_index]
    st.write(f"Question {st.session_state.question_index + 1}: {question['question']}")
    options = question['options']
    answer = st.radio("Select an option:", options)
    if st.button("Submit"):
        handle_answer(answer, question['answer'])
else:
    st.write(f"Quiz completed! Your score is {st.session_state.score} out of {len(quiz_data)}")
    if st.button("Restart quiz"):
        st.session_state.question_index = 0
        st.session_state.score = 0
