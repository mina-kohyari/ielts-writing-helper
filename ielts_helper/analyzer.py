import re
import json
from collections import Counter
from statistics import mean
from ielts_helper.tips import get_tips

def analyze_text(text: str, as_json: bool = False):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    paragraphs = [p for p in text.split("\n") if p.strip()]

    word_count = len(words)
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    avg_sentence_len = round(mean(sentence_lengths), 1) if sentence_lengths else 0
    long_sentences = [s for s in sentence_lengths if s > 25]

    unique_words = set(words)
    lexical_diversity = round(len(unique_words)/word_count,2) if word_count else 0

    repeated_words = [w for w,c in Counter(words).items() if c>max(4, word_count*0.02)]
    connectors = ["however","therefore","moreover","in addition","for example","on the other hand","as a result"]
    connector_count = sum(text.lower().count(c) for c in connectors)

    score = calculate_score(word_count, avg_sentence_len, len(long_sentences), lexical_diversity, len(paragraphs), connector_count)
    band = estimate_band(score)
    tips = get_tips(word_count,len(long_sentences),lexical_diversity,len(paragraphs),connector_count)

    result = {
        "word_count": word_count,
        "avg_sentence_length": avg_sentence_len,
        "lexical_diversity": lexical_diversity,
        "paragraphs": len(paragraphs),
        "linking_words": connector_count,
        "overused_words": repeated_words[:6],
        "estimated_band": band,
        "tips": tips
    }

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        pretty_print(result)

def calculate_score(word_count, avg_len, long_count, lex_div, paragraphs, connectors):
    score = 0
    if word_count>=270: score+=2
    elif word_count>=250: score+=1
    if avg_len<=22 and long_count<=2: score+=2
    elif long_count<=4: score+=1
    if lex_div>=0.55: score+=2
    elif lex_div>=0.45: score+=1
    if paragraphs>=4: score+=2
    elif paragraphs==3: score+=1
    if connectors>=5: score+=2
    elif connectors>=3: score+=1
    return score

def estimate_band(score):
    if score>=9: return "Band 8.5–9"
    elif score>=7: return "Band 7–8"
    elif score>=5: return "Band 6–6.5"
    elif score>=3: return "Band 5–5.5"
    else: return "Below Band 5"

def pretty_print(data):
    print("\n IELTS Writing Analysis\n")
    print(f" Word count: {data['word_count']}")
    print(f" Avg sentence length: {data['avg_sentence_length']}")
    print(f" Lexical diversity: {data['lexical_diversity']}")
    print(f" Paragraphs: {data['paragraphs']}")
    print(f" Linking words: {data['linking_words']}")
    if data["overused_words"]:
        print(f" Overused words: {', '.join(data['overused_words'])}")
    print(f"\n Estimated IELTS Band: {data['estimated_band']}")
    print("\n Tips:")
    for tip in data["tips"]:
        print(f"- {tip}")