#!/usr/bin/env python3
"""
Test script for custom agent functionality
"""
import requests
import json
import sys

API_URL = "http://127.0.0.1:8000"

def test_agent_creation():
    """Test creating a custom agent"""
    print("🧪 Testing agent creation...")
    
    agent_data = {
        "name": "EcoWarrior",
        "avatar": "🌱",
        "description": "This agent believes environmental protection is the highest moral priority. It prioritizes future generations and uses scientific evidence to make decisions. When evaluating ethical dilemmas, it always considers the long-term impact on the planet and wildlife. The agent is passionate but evidence-based, often citing climate science and ecological research."
    }
    
    try:
        response = requests.post(f"{API_URL}/api/agents/create", json=agent_data, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Agent created successfully!")
            print(f"   Name: {result['agent']['name']}")
            print(f"   ID: {result['agent']['id']}")
            print(f"   Enhanced: {len(result['enhancement']['improvements_made'])} improvements made")
            return result['agent']['id']
        else:
            print(f"❌ Failed to create agent: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Exception during agent creation: {e}")
        return None

def test_agent_listing():
    """Test listing all agents"""
    print("\n🧪 Testing agent listing...")
    
    try:
        response = requests.get(f"{API_URL}/api/agents/all", timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            agents = result['agents']
            print(f"✅ Found {len(agents)} total agents:")
            
            for agent in agents:
                agent_type = agent.get('type', 'unknown')
                rating = agent.get('rating', 0)
                usage = agent.get('usage_count', 0)
                print(f"   - {agent['name']} ({agent_type}) {agent['avatar']} - Rating: {rating}, Usage: {usage}")
            
            return agents
        else:
            print(f"❌ Failed to list agents: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"❌ Exception during agent listing: {e}")
        return []

def test_enhancement_only():
    """Test description enhancement without creating agent"""
    print("\n🧪 Testing description enhancement...")
    
    description = "This bot cares about animals and thinks we should protect them. It doesn't like factory farming."
    
    try:
        response = requests.post(f"{API_URL}/api/enhance", json={"description": description}, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Enhancement successful!")
            print(f"   Original length: {len(description)} chars")
            print(f"   Enhanced length: {len(result['enhanced_prompt'])} chars")
            print(f"   Improvements: {len(result['improvements_made'])}")
            print(f"   Suggestions: {len(result['suggestions'])}")
            
            # Show analysis scores
            scores = result['analysis_scores']
            print("   Analysis scores:")
            for key, score in scores.items():
                print(f"     {key.capitalize()}: {score:.1f}/10")
            
            return result
        else:
            print(f"❌ Failed to enhance: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Exception during enhancement: {e}")
        return None

def test_custom_agent_in_debate(agent_id):
    """Test using a custom agent in a debate"""
    if not agent_id:
        print("\n⏭️  Skipping debate test (no agent ID)")
        return
        
    print(f"\n🧪 Testing custom agent in debate...")
    
    dilemma = {
        "title": "Environmental vs Economic Dilemma",
        "A": "Shut down the factory to protect the environment",
        "B": "Keep the factory running to preserve jobs",
        "constraints": "Factory provides 1000 jobs but pollutes local river"
    }
    
    try:
        # Test single agent response
        response = requests.post(f"{API_URL}/agent/{agent_id}", json=dilemma, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Custom agent responded successfully!")
            print(f"   Agent: {result['agent']}")
            print(f"   Stance: {result['stance']}")
            print(f"   Argument preview: {result['argument'][:100]}...")
            return True
        else:
            print(f"❌ Failed to get agent response: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception during debate test: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Custom Agent API Tests\n")
    
    # Test enhancement first (doesn't require agent creation)
    enhancement_result = test_enhancement_only()
    
    # Test agent creation
    agent_id = test_agent_creation()
    
    # Test agent listing
    agents = test_agent_listing()
    
    # Test custom agent in debate
    test_custom_agent_in_debate(agent_id)
    
    print("\n🏁 Tests completed!")
    
    # Summary
    print("\n📊 Summary:")
    print(f"   Enhancement: {'✅' if enhancement_result else '❌'}")
    print(f"   Agent Creation: {'✅' if agent_id else '❌'}")
    print(f"   Agent Listing: {'✅' if agents else '❌'}")
    print(f"   Total Agents: {len(agents) if agents else 0}")

if __name__ == "__main__":
    main()