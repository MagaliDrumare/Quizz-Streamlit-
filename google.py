import streamlit as st

# Questions and choices
questions = {
    "What is the primary design goal of Gemma compared to Gemini?": [
        "Gemma focuses on language model efficiency, while Gemini targets a broader application integration.",
        "Gemma is designed for high-performance computing, Gemini for mobile devices.",
        "Gemma supports only NLP tasks, while Gemini is multi-functional.",
        "Gemma is proprietary, whereas Gemini is open-source."
    ],
    "Which model is integrated into Google’s mobile applications like Gmail and Docs?": [
        "Gemma",
        "Gemini",
        "Both Gemma and Gemini",
        "Neither"
    ],
    "How does the size of the models in Gemma compare to those in Gemini?": [
        "Gemma models are larger.",
        "Gemini models are larger.",
        "Both have similar sizes.",
        "The size is undisclosed."
    ],
    "Which model emphasizes user experience enhancements across various Google applications?": [
        "Gemma",
        "Gemini",
        "Both equally",
        "Neither specifically"
    ],
    "What type of AI model architecture is primarily used in Gemma that differs from Gemini?": [
        "Transformers",
        "Recurrent Neural Networks",
        "Convolutional Neural Networks",
        "Mixture of Experts"
    ],
    "How does the training data volume for Gemma 2’s largest model compare to that used for Gemini?": [
        "Gemma 2 uses more data.",
        "Gemini uses more data.",
        "They use the same amount of data.",
        "Data usage is not comparable due to different applications."
    ],
    "In terms of deployment, how does Gemma’s open model nature compare to Gemini’s application?": [
        "Gemma is open for public modification, Gemini is not.",
        "Gemini is open-source, Gemma is not.",
        "Both are completely proprietary.",
        "Both models are open to the public."
    ],
    "What training approach is uniquely emphasized in Gemma that is less pronounced in Gemini?": [
        "Self-supervised learning",
        "Supervised learning",
        "Reinforcement learning",
        "Unsupervised learning"
    ],
    "How do Gemma and Gemini models differ in their handling of multiple languages?": [
        "Gemma supports more languages.",
        "Gemini supports more languages.",
        "Both support an equal number of languages.",
        "Language support is not a focus for either model."
    ],
    "Which model is specifically noted for its application in enhancing Android operating system functionalities?": [
        "Gemma",
        "Gemini",
        "Both",
        "Neither"
    ]
}

# Correct answers
correct_answers = {
    "What is the primary design goal of Gemma compared to Gemini?": "Gemma focuses on language model efficiency, while Gemini targets a broader application integration.",
    "Which model is integrated into Google’s mobile applications like Gmail and Docs?": "Gemini",
    "How does the size of the models in Gemma compare to those in Gemini?": "Gemma models are larger.",
    "Which model emphasizes user experience enhancements across various Google applications?": "Gemini",
    "What type of AI model architecture is primarily used in Gemma that differs from Gemini?": "Transformers",
    "How does the training data volume for Gemma 2’s largest model compare to that used for Gemini?": "Gemma 2 uses more data.",
    "In terms of deployment, how does Gemma’s open model nature compare to Gemini’s application?": "Gemma is open for public modification, Gemini is not.",
    "What training approach is uniquely emphasized in Gemma that is less pronounced in Gemini?": "Self-supervised learning",
    "How do Gemma and Gemini models differ in their handling of multiple languages?": "Gemma supports more languages.",
    "Which model is specifically noted for its application in enhancing Android operating system functionalities?": "Gemini"
}

# Streamlit user interface
def main():
    st.title("Google Gemma vs. Gemini Quiz")

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
