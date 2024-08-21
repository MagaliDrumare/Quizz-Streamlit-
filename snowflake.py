import streamlit as st

# Questions and choices
questions = {
    "What is the primary function of Snowflake Cortex Analyst?": [
        "To provide a no-code development platform for AI applications.",
        "To offer a conversational interface for interacting with structured data.",
        "To enhance data storage capabilities in the cloud.",
        "None of the above."
    ],
    "What technology base does Snowflake Cortex Analyst utilize?": [
        "Google's BERT.",
        "Meta's Llama and Mistral models.",
        "IBM Watson.",
        "OpenAI's GPT-3."
    ],
    "What major benefit does serverless fine-tuning provide in Snowflake Cortex AI?": [
        "Decreases the cost of application deployment.",
        "Allows users to interact directly with the AI model.",
        "Eliminates the need for managing server infrastructure.",
        "Both A and C."
    ],
    "What is a key feature of the Snowflake Arctic LLM?": [
        "It is primarily for small-scale applications.",
        "It is designed for enterprise AI, focusing on efficiency and openness.",
        "It supports only basic natural language processing tasks.",
        "It is closed-source software."
    ],
    "How does Snowflake facilitate building generative AI applications?": [
        "By providing only pre-trained models without customization options.",
        "Through fully managed LLMs and chat-with-data services.",
        "By exclusively focusing on hardware improvements.",
        "By offering only client-side implementations."
    ],
    "What was a significant update in Snowflake's AI capabilities as of August 2024?": [
        "Introduction of Snowflake Arctic.",
        "Introduction of Llama 3.1 in Snowflake Cortex AI.",
        "Discontinuation of all AI services.",
        "Merging with another tech giant's AI division."
    ],
    "What is the aim of the Snowflake Cortex AI suite?": [
        "To provide AI features that are difficult to use and require extensive coding.",
        "To enable businesses to create and deploy generative AI applications securely and serverlessly.",
        "To solely improve the graphical interface of Snowflake platforms.",
        "None of the above."
    ],
    "What unique feature does the Demo: Build A RAG Application with Snowflake Cortex Search highlight?": [
        "Advanced machine learning algorithms for predictive analytics.",
        "The ability to retrieve and generate responses based on contextual understanding.",
        "High-performance transaction processing.",
        "Enhanced data visualization tools."
    ],
    "How does Snowflake's no-code development platform benefit users?": [
        "It restricts users to predefined templates.",
        "It enables users of all technical levels to develop AI applications.",
        "It requires deep technical expertise to be used effectively.",
        "It supports only data professionals."
    ],
    "What is the role of Llama 3.1 in Snowflake's ecosystem?": [
        "It's used primarily for data visualization.",
        "It's a key component in enhancing the manageability of AI applications.",
        "It's part of the suite of features enhancing the AI capabilities of Snowflake.",
        "It's a new data storage format."
    ]
}

# Correct answers
correct_answers = {
    "What is the primary function of Snowflake Cortex Analyst?": "To offer a conversational interface for interacting with structured data.",
    "What technology base does Snowflake Cortex Analyst utilize?": "Meta's Llama and Mistral models.",
    "What major benefit does serverless fine-tuning provide in Snowflake Cortex AI?": "Eliminates the need for managing server infrastructure.",
    "What is a key feature of the Snowflake Arctic LLM?": "It is designed for enterprise AI, focusing on efficiency and openness.",
    "How does Snowflake facilitate building generative AI applications?": "Through fully managed LLMs and chat-with-data services.",
    "What was a significant update in Snowflake's AI capabilities as of August 2024?": "Introduction of Llama 3.1 in Snowflake Cortex AI.",
    "What is the aim of the Snowflake Cortex AI suite?": "To enable businesses to create and deploy generative AI applications securely and serverlessly.",
    "What unique feature does the Demo: Build A RAG Application with Snowflake Cortex Search highlight?": "The ability to retrieve and generate responses based on contextual understanding.",
    "How does Snowflake's no-code development platform benefit users?": "It enables users of all technical levels to develop AI applications.",
    "What is the role of Llama 3.1 in Snowflake's ecosystem?": "It's part of the suite of features enhancing the AI capabilities of Snowflake."
}

# Streamlit user interface
def main():
    st.title("Snowflake Generative AI Quiz")

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
