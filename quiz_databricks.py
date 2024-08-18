import streamlit as st

# Questions and choices
questions = {
    "What is the purpose of prompt engineering in the context of generative AI?": [
        "To modify the underlying AI model directly.",
        "To elicit better responses from the model without modifying it.",
        "To increase the processing speed of AI models.",
        "None of the above."
    ],
    "What does RAG stand for and what is its function?": [
        "Relevant Answer Generation; it creates new data.",
        "Retrieval-Augmented Generation; it finds relevant documents to provide context for better responses.",
        "Rapid AI Generation; it speeds up response times.",
        "None of the above."
    ],
    "What is fine-tuning in the context of LLMs?": [
        "Adjusting model parameters slightly to improve performance.",
        "Adapting an existing general-purpose model with additional training.",
        "Training a model from scratch.",
        "Both A and B."
    ],
    "What does pre-training involve?": [
        "Re-training a model on new tasks.",
        "Building a new LLM model from scratch tailored to specific domains.",
        "Adjusting only the final layers of an LLM.",
        "None of the above."
    ],
    "How does Mosaic AI Model Training differ in its approach?": [
        "It only uses proprietary models.",
        "It focuses on training smaller LLMs cost-effectively.",
        "It prohibits the fine-tuning of models.",
        "Both A and C."
    ],
    "How can one use Databricks AI Playground?": [
        "To buy and sell AI models.",
        "To interact and compare different LLMs in a chat-like environment.",
        "To download AI software.",
        "None of the above."
    ],
    "What architectural feature does DBRX utilize to achieve high efficiency and speed?": [
        "Mixture-of-Experts (MoE).",
        "Singular Expert Systems.",
        "Basic Neural Networks.",
        "Advanced Reinforcement Learning."
    ],
    "What is the primary benefit of using DBRX according to Databricks?": [
        "It is slower but more accurate.",
        "It outperforms existing open-source models on standard benchmarks.",
        "It uses fewer parameters.",
        "It is exclusively for private use."
    ],
    "Which notable companies leverage the Databricks Data Intelligence Platform?": [
        "NASDAQ and JetBlue.",
        "Apple and Microsoft.",
        "Google and Amazon.",
        "Tesla and SpaceX."
    ],
    "What major benefit does fine-tuning on Databricks' platform offer?": [
        "It significantly increases the size of LLMs.",
        "It allows for training LLMs without any cost.",
        "It enables the adaptation of general-purpose LLMs to more specialized tasks.",
        "It provides unlimited access to all LLMs globally."
    ]
}

# Correct answers
correct_answers = {
    "What is the purpose of prompt engineering in the context of generative AI?": "To elicit better responses from the model without modifying it.",
    "What does RAG stand for and what is its function?": "Retrieval-Augmented Generation; it finds relevant documents to provide context for better responses.",
    "What is fine-tuning in the context of LLMs?": "Adapting an existing general-purpose model with additional training.",
    "What does pre-training involve?": "Building a new LLM model from scratch tailored to specific domains.",
    "How does Mosaic AI Model Training differ in its approach?": "It focuses on training smaller LLMs cost-effectively.",
    "How can one use Databricks AI Playground?": "To interact and compare different LLMs in a chat-like environment.",
    "What architectural feature does DBRX utilize to achieve high efficiency and speed?": "Mixture-of-Experts (MoE).",
    "What is the primary benefit of using DBRX according to Databricks?": "It outperforms existing open-source models on standard benchmarks.",
    "Which notable companies leverage the Databricks Data Intelligence Platform?": "NASDAQ and JetBlue.",
    "What major benefit does fine-tuning on Databricks' platform offer?": "It enables the adaptation of general-purpose LLMs to more specialized tasks."
}

# Streamlit user interface
def main():
    st.title("Databricks Generative AI Quizz")

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
