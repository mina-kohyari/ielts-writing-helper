import random



# Optional constants or prompts for your analyzer
TASK_PROMPT = "Analyze this essay for IELTS writing task 1 or 2."

PROMPTS = [
    "Some people think technology makes life easier. Discuss both views.",
    "Should governments spend more money on education or healthcare?",
    "Many people prefer to work from home. Is this a positive or negative development?",
    "Some believe exams are not a good way to measure ability. Do you agree?"
]

def get_prompt():
    return " IELTS Writing Prompt:\n" + random.choice(PROMPTS)