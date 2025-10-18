import requests
import json

# Test just Conse specifically
API = "http://127.0.0.1:8000"

dilemma = {
  "title": "Academic Integrity vs Compassion",
  "A": "Decline to write the student's paper; offer resources and planning help.",
  "B": "Quietly write the paper to help them pass due to exceptional hardship.",
  "constraints": "Family emergency; deadline tonight; honor code exists; failure risks scholarship."
}

print("Testing Conse specifically...")
try:
    r = requests.post(f"{API}/openings", json=dilemma, timeout=60)
    r.raise_for_status()
    result = r.json()
    
    print("All turns returned:")
    for i, turn in enumerate(result["turns"]):
        print(f"{i+1}. Agent: {turn['agent']}")
        print(f"   Stance: {turn.get('stance', 'MISSING')}")
        print(f"   Argument length: {len(turn.get('argument', ''))}")
        print(f"   Argument preview: {turn.get('argument', 'MISSING')[:100]}...")
        print()
        
except Exception as e:
    print(f"Error: {e}")