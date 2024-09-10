import streamlit as st

# Questions and choices
questions = {
    "What is the primary function of Einstein Copilot in Salesforce?": [
        "To provide cloud storage solutions",
        "To process natural language commands and generate responses based on business data",
        "To manage email communications automatically",
        "To enhance website security"
    ],
    "How can businesses customize Einstein Copilot to better suit their needs?": [
        "By modifying the source code of Salesforce",
        "By using custom Salesforce data fields and incorporating existing workflows",
        "By limiting its access to sensitive data",
        "By using it straight out of the box without any customizations"
    ],
    "What is LlamaRank primarily used for?": [
        "To automate sales processes",
        "To rank document relevancy accurately",
        "To enhance graphical user interface design",
        "To manage Salesforce cloud infrastructure"
    ],
    "What unique approach does LlamaRank employ to improve its performance?": [
        "Using high-frequency trading algorithms",
        "Iterative on-policy feedback from the Salesforce RLHF data annotation team",
        "Deep learning techniques based on neural network architectures",
        "Blockchain technology to secure data transactions"
    ],
    "What is the goal of introducing the xLAM models by Salesforce?": [
        "To provide entertainment through games",
        "To assist in creating marketing content",
        "To help businesses increase automation and efficiency",
        "To improve personal communication between employees"
    ],
    "How does Agentforce leverage AI models?": [
        "By using them to power autonomous sales tasks",
        "By employing AI to manage employee leave requests",
        "To track changes in software development",
        "To predict stock market trends"
    ],
    "What is a primary feature of the xGen-MM-1 models?": [
        "They are specifically designed for medical research.",
        "They are designed to handle complex tasks and generate actionable outputs.",
        "They focus exclusively on cybersecurity threats.",
        "They serve as personal assistants to executives."
    ],
    "How can Salesforce's AI models like xLAM and xGen-Sales transform sales processes?": [
        "By eliminating the need for human sales representatives",
        "By driving autonomous actions that scale operations",
        "By reducing the efficiency of sales tasks",
        "By focusing only on manual data entry"
    ],
    "What role does RAG (Retrieval Augmented Generation) play in Salesforce AI technologies?": [
        "It is used to enhance musical composition algorithms.",
        "It improves search capabilities through enhanced enterprise search.",
        "It is used for automating the creation of visual content.",
        "It provides virtual reality experiences for training purposes."
    ],
    "How do Salesforce AI technologies integrate with existing Salesforce workflows?": [
        "By replacing all existing workflows with AI-driven processes",
        "By adding custom actions with descriptive metadata to Flows and Apex classes",
        "By requiring complete reimplementation of all business processes",
        "By disconnecting existing workflows and starting from scratch"
    ]
}

# Correct answers
correct_answers = {
    "What is the primary function of Einstein Copilot in Salesforce?": "To process natural language commands and generate responses based on business data",
    "How can businesses customize Einstein Copilot to better suit their needs?": "By using custom Salesforce data fields and incorporating existing workflows",
    "What is LlamaRank primarily used for?": "To rank document relevancy accurately",
    "What unique approach does LlamaRank employ to improve its performance?": "Iterative on-policy feedback from the Salesforce RLHF data annotation team",
    "What is the goal of introducing the xLAM models by Salesforce?": "To help businesses increase automation and efficiency",
    "How does Agentforce leverage AI models?": "By using them to power autonomous sales tasks",
    "What is a primary feature of the xGen-MM-1 models?": "They are designed to handle complex tasks and generate actionable outputs.",
    "How can Salesforce's AI models like xLAM and xGen-Sales transform sales processes?": "By driving autonomous actions that scale operations",
    "What role does RAG (Retrieval Augmented Generation) play in Salesforce AI technologies?": "It improves search capabilities through enhanced enterprise search.",
    "How do Salesforce AI technologies integrate with existing Salesforce workflows?": "By adding custom actions with descriptive metadata to Flows and Apex classes"
}

# Streamlit user interface
def main():
    st.title("Salesforce Generative AI Quiz")

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
