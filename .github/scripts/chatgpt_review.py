import openai
import os
import subprocess

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_diff():
    result = subprocess.run(['git', 'diff', 'origin/main...HEAD'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def analyze_code(diff):
    prompt = f"Please review the following code diff and provide feedback:\n\n{diff}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    diff = get_diff()
    feedback = analyze_code(diff)
    print(f"ChatGPT Feedback:\n{feedback}")
