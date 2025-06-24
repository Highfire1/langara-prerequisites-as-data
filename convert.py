import os
import json
import requests
from dotenv import load_dotenv

from helpers import print_human_readable

load_dotenv()

from data.text import prerequisites


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
INSTRUCTIONS_PATH = "instructions.md"
OUTPUT_PATH = "data/converted.json"
MODEL = "mistralai/mistral-7b-instruct:free"

def load_instructions():
    with open(INSTRUCTIONS_PATH, "r", encoding="utf-8") as f:
        return f.read()

def call_openrouter(prompt:str, instructions:str):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": f'Convert the following prerequisite text to JSON as per the instructions. Only output the JSON.\n\nText:\n{prompt}'}
    ]
    data: dict[str, object] = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.content}")
        response.raise_for_status()
    else: 
        try:
            content = response.json()["choices"][0]["message"]["content"]
            # Remove markdown code block if present
            if content.strip().startswith("```json"):
                content = content.strip().split("```json")[1].split("```")[0].strip()
            return json.loads(content)
        except Exception as e:
            print(f"Failed to JSON response: {response.content}")
            raise e

def main():
    
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    instructions = load_instructions()
    
    
    # Load existing results if the file exists
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            results = json.load(f)
    else:
        results = {}

    for text in prerequisites:
        if text in results:
            print(f"Skipping {text[17:37]}... because it already exists.")
            continue
        
        if len(text) > 140:
            print(f"Skipping {text[17:37]}... because it is too complicated.")
            continue
        
        print("="*50)
        print(f"Processing: {text}")
        print()
        responses: list[dict[str, object]] = []
        
        # do it twice
        attempts = 0
        max_attempts = 2
        while True:
            if attempts >= max_attempts:
                break
            
            try:
                result = call_openrouter(text, instructions)
                responses.append(result) # type: ignore
                print(f"RESULT ({attempts+1}/{max_attempts}) RECIEVED:")
                
                # print(result)
                
                print_human_readable(result)
                print()
                attempts += 1
            except Exception as e:
                input(f"Error on attempt {attempts}. Error: {e}")
                attempts += 0.5 # don't error infinitely
        
        while True:
            print("-"*40)
            print("Conversion finished.")
            if responses[0] == responses[1]:
                print("Both responses match!")
            else:
                print("RESPONSES DO NOT MATCH.")
            print("(p): print raw responses (s): skip")
            i = input("(1/2): save response: ")
            if i == 'p':
                print("-"*40)
                for n, r in enumerate(responses):
                    print(f"{n} :")
                    print(json.dumps(r, indent=2, ensure_ascii=False))
                    print()
                print("-"*40)
            elif i == '1' or i == 2:
                results[text] = responses
                with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                break
            elif i == 's':
                print("Skipping.")
                break
            
            
            
    print("Done. Results saved to", OUTPUT_PATH)


if __name__ == "__main__":
    main()
