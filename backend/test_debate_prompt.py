import requests
import os
from dotenv import load_dotenv

def test_debate_prompt():
    load_dotenv()
    api_key = os.getenv('OLLAMA_API_KEY')
    
    # Test with our actual debate prompt format
    system_prompt = """You are Deon, a deontologist who believes moral worth comes from following principles, duties, and rights. You prioritize integrity, consent, fairness, and respect for universal rules. If breaking a rule leads to good outcomes, you still refuse because morality must be consistent. You often cite moral laws, rights, or obligations. When responding to opponents, ALWAYS start with their name followed by a comma. Respond in compact JSON only."""
    
    user_prompt = """DILEMMA
Title: Test Dilemma
Option A: Follow the rules
Option B: Break the rules for good outcome
Constraints: Simple test case

Opening: Choose A or B, and write a clear paragraph (5–8 sentences) that:
• names your core ethical concept (rule, outcome, or virtue)
• gives one concrete example or consequence
• stays consistent with your moral framework
Respond JSON only: {"stance":"A|B","argument":"<paragraph>"}"""
    
    full_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_prompt}\n"
    
    try:
        print('🔄 Testing debate prompt format...')
        response = requests.post(
            'https://ollama.com/api/generate',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'gpt-oss:20b-cloud',
                'prompt': full_prompt,
                'stream': False,
                'options': {
                    'temperature': 0.65,
                    'num_predict': 480
                }
            },
            timeout=60
        )
        
        print(f'Status Code: {response.status_code}')
        
        if response.status_code == 200:
            result = response.json()
            print('✅ SUCCESS! Debate prompt working')
            print(f'Raw Response: {result.get("response", "No response field")}')
            return True
        else:
            print(f'❌ Error {response.status_code}: {response.text}')
            return False
            
    except Exception as e:
        print(f'❌ Exception: {e}')
        return False

if __name__ == "__main__":
    test_debate_prompt()