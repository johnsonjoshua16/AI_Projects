import openai
import os

class FacilitateAI:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def ask(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # GPT-3 text completion engine
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
                n=1,
                stop=None,
            )
            answer = response.choices[0].text.strip()
            return answer
        except Exception as e:
            return f"Error: {str(e)}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print(" " * 18 + "🤖 FacilitateAI Chat 🤖")
    print("=" * 60)
    print("Type 'exit' to quit at any time.")
    print("-" * 60)

def main():
    clear_screen()
    print_header()
    api_key = input("🔑 Please enter your OpenAI API key: ").strip()
    ai = FacilitateAI(api_key)

    while True:
        print("\n" + "-" * 60)
        user_input = input("🧑 You: ").strip()
        if user_input.lower() == "exit":
            print("\n👋 Goodbye! Thanks for using FacilitateAI.")
            print("=" * 60)
            break
        if not user_input:
            print("⚠️  Please enter a prompt.")
            continue

        print("🤖 FacilitateAI is thinking...\n")
        response = ai.ask(user_input)
        print(f"🤖 FacilitateAI: {response}")

if __name__ == "__main__":
    main()
