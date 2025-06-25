import os
import json
import requests
from dotenv import load_dotenv

from helpers import print_human_readable

load_dotenv()

from data.text import prerequisites
from data.hard_cases import hard_cases


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
INSTRUCTIONS_PATH = "instructions.md"
OUTPUT_PATH = "data/converted.json"
MODEL_1 = "google/gemini-2.5-pro"
MODEL_2 = "mistralai/mistral-7b-instruct:free"
MODEL = MODEL_1

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
        "reasoning" : {
            "effort": "high",
            "exclude": False, 
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.content}")
        response.raise_for_status()
    else: 
        try:
            try:
                choices = response.json().get("choices", [])
                if not choices or "message" not in choices[0] or "content" not in choices[0]["message"]:
                    raise ValueError("Response JSON does not contain expected 'choices/message/content' structure.")
                content = choices[0]["message"]["content"]
                # Remove markdown code block if present
                if content.strip().startswith("```json"):
                    content = content.strip().split("```json", 1)[1].split("```", 1)[0].strip()
                elif content.strip().startswith("```"):
                    content = content.strip().split("```", 1)[1].split("```", 1)[0].strip()
                return json.loads(content)
            except (KeyError, IndexError, ValueError, json.JSONDecodeError) as e:
                print(f"Failed to parse response content: {e}")
                # print(f"Raw response: {response.text}")
                raise e
        except Exception as e:
            print(f"Failed to JSON response.")
            raise e

def main():
    global MODEL
    
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    instructions = load_instructions()
    
    
    # Load existing results if the file exists
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            results = json.load(f)
    else:
        results = {}
    
    count_existing = sum(1 for text in prerequisites if text in results)
    count_hard = sum(1 for text in prerequisites if text in hard_cases)
    remaining = len(prerequisites) - count_existing - count_hard
    
    print("STATUS REPORT:")
    print(f"{count_existing} out of {len(prerequisites)} prerequisites already exist in results.")
    print(f"{count_hard} out of {len(prerequisites)} prerequisites cannot be converted.")
    print(f"{remaining} prerequisites remain to be converted.")

    for text in prerequisites:
        
        # temporarily skip bad ones
        # if "MDT" in text:# or "LET" in text:
        #     continue
        
        if text in hard_cases:
            print(f"Skipping {text[17:37]}... because we can't handle it.")
            continue
        
        if text in results:
            # print(f"Skipping {text[17:37]}... because it already exists.")
            continue
        
        # if len(text) > 150:
        #     print(f"Skipping {text[17:37]}... because it is too complicated.")
        #     continue
        
        print("="*50)
        print(f"{text}")
        print()
        responses: list[dict[str, object]] = []
        
        # do it twice
        attempts = 0
        max_attempts = 1
        MODEL = MODEL_1
        while True:
            if attempts >= max_attempts:
                break
            
            if attempts > 0:
                MODEL = MODEL_2
            
            try:
                result = call_openrouter(text, instructions)
                responses.append(result) # type: ignore
                print(f"RESULT ({attempts+1}/{max_attempts}) RECIEVED:")
                
                # print(result)
                
                print_human_readable(result)
                print()
                attempts += 1
            except Exception as e:
                print(f"Error on attempt {attempts}.")
                attempts += 0.5 # don't error infinitely
                input("Press enter to try again: ")
                print()
        
        while True:
            if len(responses) == 0:
                input("No responses generated. Press enter to continue: ")
                break
            
            print("-"*40)
            print("Conversion finished.")
            if len(responses) >= 2 and responses[0] == responses[1]:
                print("Both responses match!")
            elif len(responses) == 1:
                pass
            elif len(responses) == 0:
                print("Failed to generate conversion.")
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
                
            elif i == '1' or i == '2':
                if i == '1':
                    results[text] = responses[0]
                elif i == '2':
                    results[text] = responses[1]
                with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                break
            elif i == 's':
                print("Skipping.")
                break
            
            
            
    print("Done. Results saved to", OUTPUT_PATH)


if __name__ == "__main__":
    main()
