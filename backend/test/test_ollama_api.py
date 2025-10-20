import requests
import os
from dotenv import load_dotenv

def test_ollama_api():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv('OLLAMA_API_KEY')
    print(f'API Key set: {"Yes" if api_key else "No"}')
    
    if not api_key:
        print('❌ No API key found in environment variable OLLAMA_API_KEY')
        return
    
    print(f'API Key (first 20 chars): {api_key[:20]}...')
    
    try:
        print('🔄 Testing Ollama cloud API...')
        response = requests.post(
            'https://ollama.com/api/generate',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'gpt-oss:20b-cloud',
                'prompt': 'Hello, respond with just "API test successful"',
                'stream': False
            },
            timeout=30
        )
        
        print(f'Status Code: {response.status_code}')
        
        if response.status_code == 200:
            result = response.json()
            print('✅ SUCCESS! API is working')
            print(f'Model Response: {result.get("response", "No response field")}')
            return True
        else:
            print(f'❌ Error {response.status_code}: {response.text}')
            return False
            
    except requests.exceptions.Timeout:
        print('❌ Request timed out - API might be slow')
        return False
    except requests.exceptions.RequestException as e:
        print(f'❌ Request Exception: {e}')
        return False
    except Exception as e:
        print(f'❌ Unexpected Exception: {e}')
        return False

if __name__ == "__main__":
    test_ollama_api()