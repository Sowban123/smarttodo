import datetime
import random

# Sample categories based on keywords
CATEGORY_KEYWORDS = {
    "work": ["project", "meeting", "deadline", "client", "email"],
    "personal": ["birthday", "grocery", "family", "movie", "dinner"],
    "health": ["doctor", "exercise", "medicine", "appointment", "gym"],
}

PRIORITY_KEYWORDS = {
    "high": ["urgent", "asap", "immediately", "important"],
    "medium": ["soon", "this week", "moderate"],
    "low": ["later", "optional", "someday"]
}

def suggest_priority(description, context_entries):
    text = (description + " " + " ".join(context_entries)).lower()
    for level, keywords in PRIORITY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return level
    return "medium"

def suggest_deadline(description):
    today = datetime.datetime.now()
    if "urgent" in description.lower():
        return today + datetime.timedelta(days=1)
    return today + datetime.timedelta(days=random.choice([2, 3, 4]))

def suggest_category(description):
    text = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return category
    return "general"

def enhance_description(description, context_entries):
    if context_entries:
        return description + " (Related to: " + ", ".join(context_entries[:2]) + ")"
    return description
