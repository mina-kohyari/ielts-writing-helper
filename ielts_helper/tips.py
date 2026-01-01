def get_tips(word_count, long_sentence_count, lexical_diversity, paragraphs, connectors):
    tips = []
    if word_count < 250:
        tips.append("Develop your ideas further to reach Task 2 length.")
    if long_sentence_count > 2:
        tips.append("Reduce sentence length to improve clarity.")
    if lexical_diversity < 0.45:
        tips.append("Use a wider range of vocabulary.")
    if paragraphs < 4:
        tips.append("Use clear paragraphing (intro, body, conclusion).")
    if connectors < 3:
        tips.append("Use more linking words to improve coherence.")
    tips.append("Check grammar and verb tense consistency.")
    tips.append("Avoid informal language in academic writing.")
    return tips