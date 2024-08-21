import streamlit as st

# Questions and choices
questions = {
    "What is Gemma primarily known for in the realm of AI?": [
        "Its integration into mobile devices",
        "Being a lightweight, state-of-the-art open model",
        "Enhancing Google Search and Gmail only",
        "A proprietary model exclusive to Google"
    ],
    "What significant feature does Gemma 2 introduce?": [
        "New token-based pricing model",
        "Multiple sizes with significant token training",
        "Decreased model performance",
        "Only cloud-based deployment"
    ],
    "How does Gemma's pre-training process contribute to its functionality?": [
        "It allows for domain-specific fine-tuning",
        "It focuses solely on sentiment analysis",
        "It only uses supervised learning techniques",
        "None of the above"
    ],
    "What is the purpose of Google's Gemini model?": [
        "To serve as Google's primary cloud computing service",
        "To enhance user experience across various applications",
        "To provide security services across Google platforms",
        "To act as a standalone product for data analytics"
    ],
    "What capabilities does Gemma 2 27B model boast?": [
        "Approaches the performance of Meta Llama 3 70B",
        "Limited to basic NLP tasks",
        "Only supports English language processing",
        "Offers reduced accuracy for quicker processing"
    ],
    "Where can one find demonstrations of Gemma 2 in action?": [
        "On Google’s main website",
        "Huggingface Spaces",
        "Official Google Play Store",
        "Google's physical retail stores"
    ],
    "What does the integration of Gemini into mobile devices aim to improve?": [
        "Battery life of devices",
        "Overall user experience",
        "Storage capacity of devices",
        "Physical durability of mobile devices"
    ],
    "What type of tasks is Gemma effective at due to its pre-training and fine-tuning stages?": [
        "Image processing",
        "Variety of NLP tasks",
        "Hardware optimization",
        "Web development"
    ],
    "What is a feature of Vertex AI in relation to Gemini?": [
        "It is a gaming platform",
        "It integrates AI models into Google's cloud services",
        "It is a new messaging service",
        "It provides hardware for AI computation"
    ],
    "How can developers explore and experiment with Gemini models?": [
        "Through Google Maps",
        "By participating in exclusive webinars",
        "Via Google Colab notebooks",
        "By visiting Google's headquarters"
    ]
}

# Correct answers
correct_answers = {
    "What is Gemma primarily known for in the realm of AI?": "Being a lightweight, state-of-the-art open model",
    "What significant feature does Gemma 2 introduce?": "Multiple sizes with significant token training",
    "How does Gemma's pre-training process contribute to its functionality?": "It allows for domain-specific fine-tuning",
    "What is the purpose of Google's Gemini model?": "To enhance user experience across various applications",
    "What capabilities does Gemma 2 27B model boast?": "Approaches the performance of Meta Llama 3 70B",
    "Where can one find demonstrations of Gemma 2 in action?": "Huggingface Spaces",
    "What does the integration of Gemini into mobile devices aim to improve?": "Overall user experience",
    "What type of tasks is Gemma effective at due to its pre-training and fine-tuning stages?": "Variety of NLP tasks",
    "What is a feature of Vertex AI in relation to Gemini?": "It integrates AI models into Google's cloud services",
    "How can developers explore and experiment with Gemini models?": "Via Google Colab notebooks"
}

# Streamlit user interface
def main():
    st.title("Google Generative AI Quiz")

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
