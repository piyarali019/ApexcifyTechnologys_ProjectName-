from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. FAQs (Questions & Answers)
faqs = {
    "What is your name?": "I am a FAQ chatbot.",
    "How can I reset my password?": "Go to settings and click on reset password.",
    "What is your service?": "We provide customer support.",
    "How to contact support?": "You can contact support via email.",
    "What are your working hours?": "We work from 9 AM to 5 PM."
}

questions = list(faqs.keys())
answers = list(faqs.values())

# 2. Vectorization
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

# 3. Chat loop
print("FAQ Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)

    best_match = similarity.argmax()

    print("Bot:", answers[best_match])
