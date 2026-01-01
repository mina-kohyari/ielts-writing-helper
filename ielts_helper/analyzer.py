import re
from collections import Counter
from statistics import mean
from ielts_helper.tips import get_tips


def analyze_text(text: str):
    print("\n IELTS Writing Analysis\n")

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    paragraphs = [p for p in text.split("\n") if p.strip()]

    word_count = len(words)
    sentence_lengths = [len(s.split()) for s in sentences if len(s.split()) > 0]

    # ---- Word Count ----
    print(f" Word count: {word_count}")

    if word_count < 150:
        task_type = "Task 1 (Too short)"
    elif word_count < 250:
        task_type = "Task 1 (OK length)"
    else:
        task_type = "Task 2 (OK length)"

    print(f" Detected: {task_type}")

    # ---- Sentence Analysis ----
    avg_sentence_length = round(mean(sentence_lengths), 1)
    long_sentences = [s for s in sentence_lengths if s > 25]

    print(f"\n Avg sentence length: {avg_sentence_length} words")
    print(f" Long sentences (>25 words): {len(long_sentences)}")

    # ---- Vocabulary Analysis ----
    unique_words = set(words)
    lexical_diversity = round(len(unique_words) / word_count, 2) if word_count else 0

    repeated_words = [
        word for word, count in Counter(words).items()
        if count > max(4, word_count * 0.02)
    ]

    print(f"\n Lexical diversity: {lexical_diversity}")
    if repeated_words:
        print(f" Overused words: {', '.join(repeated_words[:6])}")

    # ---- Paragraph Structure ----
    print(f"\n Paragraphs: {len(paragraphs)}")
    if len(paragraphs) < 3:
        print(" Consider using more paragraphs for clarity")

    # ---- Coherence Check ----
    connectors = [
        "however", "therefore", "moreover",
        "in addition", "for example", "on the other hand"
    ]
    connector_count = sum(text.lower().count(c) for c in connectors)

    print(f"\n Linking words used: {connector_count}")

    # ---- Final Tips ----
    print("\n💡 IELTS Improvement Tips:")
    tips = get_tips(
        word_count=word_count,
        long_sentence_count=len(long_sentences),
        lexical_diversity=lexical_diversity,
        paragraphs=len(paragraphs),
        connectors=connector_count
    )

    for tip in tips:
        print(f"- {tip}")