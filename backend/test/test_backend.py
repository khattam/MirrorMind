import requests, json, sys, time, re

API = "http://127.0.0.1:8000"

def pretty(j):
    print(json.dumps(j, indent=2, ensure_ascii=False))

def call(path, payload, timeout=300):
    r = requests.post(f"{API}{path}", json=payload, timeout=timeout)
    r.raise_for_status()
    return r.json()

# ----- Dilemma -----
dilemma = {
  "title": "Academic Integrity vs Compassion",
  "A": "Decline to write the student's paper; offer resources and planning help.",
  "B": "Quietly write the paper to help them pass due to exceptional hardship.",
  "constraints": "Family emergency; deadline tonight; honor code exists; failure risks scholarship."
}

print("=== 1) /openings ===")
openings = call("/openings", dilemma, timeout=360)
for t in openings["turns"]:
    print(f"\n[{t['agent']}] stance={t.get('stance')}")
    arg = t.get("argument","")
    print(arg[:600])
    if arg in ["—", "-"] or "[failed" in arg or "[error" in arg:
        print(f"  DEBUG: {t.get('_debug', 'no debug info')}")
        print(f"  RAW: {t.get('_raw', 'no raw info')}")

# Build transcript
transcript = {"dilemma": dilemma, "turns": openings["turns"]}

def validate_counter(turn):
    txt = turn.get("argument","").lower()
    agent = turn["agent"].lower()
    
    # Check for opponent names (not self)
    names = ["deon", "conse", "virtue"]
    mentioned_opponents = [n for n in names if n in txt and n != agent]
    
    # Must mention an opponent and have reasonable content
    return len(mentioned_opponents) > 0 and len(txt) > 30

print("\n=== 2) /continue (round 1) ===")
cont1 = call("/continue", transcript, timeout=420)
for t in cont1["turns"]:
    print(f"\n[{t['agent']}] stance={t.get('stance')}")
    arg = t.get("argument","")
    print(arg[:600])
    if not validate_counter(t):
        print(f"⚠️  WARNING: {t['agent']} failed validation (no opponent mentioned or too short)")
transcript["turns"] += cont1["turns"]

print("\n=== 3) /continue (round 2) ===")
cont2 = call("/continue", transcript, timeout=420)
for t in cont2["turns"]:
    print(f"\n[{t['agent']}] stance={t.get('stance')}")
    arg = t.get("argument","")
    print(arg[:600])
    if not validate_counter(t):
        print(f"⚠️  WARNING: {t['agent']} failed validation (no opponent mentioned or too short)")
transcript["turns"] += cont2["turns"]

print("\n=== 4) /judge ===")
verdict = call("/judge", transcript, timeout=360)
pretty(verdict)

print("\nDone.\n")
