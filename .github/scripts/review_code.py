import os
import openai

# Load API key
api_key = os.getenv("OPENAI_API_KEY")

# Read the student's code file (Assuming a single Python file for simplicity)
file_path = "student_code.py"  # Adjust to match the file being analyzed
with open(file_path, "r") as f:
    student_code = f.read()

# Send to AI for feedback
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content": "You are a coding tutor."},
              {"role": "user", "content": f"Review this Python code and provide constructive feedback:\n\n{student_code}"}]
)

# Save feedback
feedback_text = response["choices"][0]["message"]["content"]
with open(".github/feedback.txt", "w") as f:
    f.write(feedback_text)

print("Feedback generated.")
