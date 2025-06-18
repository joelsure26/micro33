import random
import re

# Sample intents and responses
faq_data = {
    "greeting": {
        "patterns": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! Feel free to ask any questions.",
            "Hey! I'm here to help you with internship and application queries."
        ]
    },
    "internship_info": {
        "patterns": [
            "apply.*internship",
            "internship opportunities",
            "want.*internship",
            "available internships",
            "any internships"
        ],
        "responses": [
            "You can apply for internships via our careers page: https://company.com/careers.",
            "Please visit our internship portal to submit your application: https://company.com/internships."
        ]
    },
    "application_deadline": {
        "patterns": [
            "deadline.*applications",
            "application deadline",
            "last date.*apply",
            "application closing date"
        ],
        "responses": [
            "The deadline for applications is June 30, 2025.",
            "All applications must be submitted before June 30, 2025."
        ]
    },
    "organization_info": {
        "patterns": [
            "about.*organization",
            "about.*company",
            "what does.*organization.*do"
        ],
        "responses": [
            "We are a leading company providing excellent opportunities for students and professionals.",
            "Our organization focuses on innovation, research, and development across multiple domains."
        ]
    },
    "goodbye": {
        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "exit"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you soon. Feel free to come back if you have more questions."
        ]
    },
    "default": {
        "responses": [
            "I'm sorry, I didn't understand that. Can you please rephrase?",
            "I don't have an answer to that right now. You can email us at support@company.com."
        ]
    }
}

# Rule-based intent matching
def match_intent(user_input):
    user_input = user_input.lower()
    for intent, intent_data in faq_data.items():
        for pattern in intent_data.get("patterns", []):
            if re.search(pattern, user_input):
                return intent
    return "default"

def get_response(user_input):
    intent = match_intent(user_input)
    responses = faq_data[intent]['responses']
    return random.choice(responses), intent
