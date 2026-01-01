import re
from collections import Counter
from ielts_helper.tips import get_tips

def analyze_text(text: str):
    words = re.findall(r"\b\w+\b", text.lower())
    word_count = len(words)

    repeated = [
        word for word, count in Counter(words).items()
        if count > 5
    ]

    sentences = re.split(r"[.!?]", text)
    long_sentences = [s for s in sentences if len(s.split()) > 25]

    print(f"\n Word count: {word_count}")

    if word_count < 150:
        print(" Too short for Task 1")
    elif word_count < 250:
        print(" Good for Task 1")
    else:
        print(" Good for Task 2")

    if repeated:
        print(f" Repeated words: {', '.join(repeated[:5])}")

    if long_sentences:
        print(f" Long sentences detected: {len(long_sentences)}")

    print("\n Tips:")
    for tip in get_tips(word_count, long_sentences):
        print(f"- {tip}")