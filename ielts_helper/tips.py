def get_tips(word_count, long_sentences):
    tips = []

    if word_count < 250:
        tips.append("Try to develop your ideas more clearly.")
    else:
        tips.append("Good length. Focus on coherence and cohesion.")

    if long_sentences:
        tips.append("Break long sentences into shorter ones.")

    tips.append("Use more linking words (however, moreover, therefore).")
    tips.append("Avoid repeating the same vocabulary.")

    return tips