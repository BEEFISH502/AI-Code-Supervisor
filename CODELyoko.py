import openai
import os
client = openai.Client(api_key=os.getenv("OPENAI_API_KEY")) 
# Set OpenAI API key from environment variable
api_key = os.getenv("")
openai.api_key = 
from openai.types import ChatModel
def get_code_snippet(prompt):
    """This function sends a request to the OpenAI API with a prompt to generate code and returns the response"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Generate code based on the following prompt:"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def get_code_explanation(prompt):
    """This function sends a request to the OpenAI API with a prompt to explain code and returns the explanation"""
    explanation_prompt = f"Explain the following code in detail:\n\n{prompt}"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Explain the following code:"},
                {"role": "user", "content": explanation_prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to C.O.D.E Lyoko")
    while True:
        user_input = input("What are we coding today, senpai?")

        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye")
            break

        # Generate code based on user input
        code = get_code_snippet(user_input)
        print("\nGenerated Code:\n", code)

        # Explain the generated code
        explanation = get_code_explanation(code)
        print("\nExplanation\n", explanation)

if __name__ == '__main__':
    main()

