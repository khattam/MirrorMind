# MirrorMinds Class Diagram

## System Architecture Overview

This class diagram represents the MirrorMinds AI-Powered Ethical Debate Simulator, showing the key components and their relationships across the backend API and frontend application.

```mermaid
classDiagram
    %% Backend Models
    class Dilemma {
        +string title
        +string A
        +string B
        +string constraints
    }

    class AgentTurn {
        +string agent
        +string stance
        +string argument
    }

    class Transcript {
        +Dilemma dilemma
        +List~AgentTurn~ turns
    }

    class Verdict {
        +dict scores
        +string final_recommendation
        +int confidence
        +string verdict
    }

    %% Backend Services
    class FastAPIApp {
        +CORSMiddleware middleware
        +post_openings(dilemma: Dilemma)
        +post_agent(agent_name: string, dilemma: Dilemma)
        +post_continue(transcript: Transcript)
        +post_judge(transcript: Transcript)
    }

    class OllamaService {
        -string MODEL
        -string OLLAMA_API
        -string OLLAMA_API_KEY
        +call_ollama(system_prompt: string, user_prompt: string) string
    }

    class JSONParser {
        +clamp_json(response: string, fallback: dict) dict
    }

    %% AI Agents
    class EthicalAgent {
        <<abstract>>
        +string name
        +string system_prompt
        +generate_opening(dilemma: Dilemma) AgentTurn
        +generate_response(transcript: Transcript) AgentTurn
    }

    class DeontologistAgent {
        +string name = "Deon"
        +string system_prompt = DEON_SYS
        +generate_opening(dilemma: Dilemma) AgentTurn
        +generate_response(transcript: Transcript) AgentTurn
    }

    class ConsequentialistAgent {
        +string name = "Conse"
        +string system_prompt = CONSE_SYS
        +generate_opening(dilemma: Dilemma) AgentTurn
        +generate_response(transcript: Transcript) AgentTurn
    }

    class VirtueEthicistAgent {
        +string name = "Virtue"
        +string system_prompt = VIRTUE_SYS
        +generate_opening(dilemma: Dilemma) AgentTurn
        +generate_response(transcript: Transcript) AgentTurn
    }

    class JudgeAgent {
        +string name = "Judge"
        +string system_prompt = JUDGE_SYS
        +evaluate_debate(transcript: Transcript) Verdict
    }

    %% Frontend Components
    class App {
        -string stage
        -Dilemma dilemma
        -Transcript transcript
        -Verdict verdict
        -int roundCount
        -string currentThinkingAgent
        -Array debateHistory
        +handleStartDebate(dilemmaData: object)
        +handleContinue()
        +handleJudge()
        +handleReset()
    }

    class DilemmaForm {
        +onSubmit: function
        +render() JSX
        +handleSubmit(formData: object)
    }

    class DebateView {
        +transcript: Transcript
        +roundCount: number
        +currentThinkingAgent: string
        +onContinue: function
        +onJudge: function
        +render() JSX
    }

    class VerdictView {
        +verdict: Verdict
        +onReset: function
        +render() JSX
    }

    class Sidebar {
        +stage: string
        +debateHistory: Array
        +onNewDebate: function
        +onViewHistory: function
        +render() JSX
    }

    class AgentCard {
        +agent: string
        +turn: AgentTurn
        +isThinking: boolean
        +render() JSX
    }

    %% API Service
    class APIService {
        -string API_URL
        +startDebate(dilemma: Dilemma) Promise~Array~
        +continueDebate(transcript: Transcript) Promise~Array~
        +judgeDebate(transcript: Transcript) Promise~Verdict~
    }

    %% Relationships
    FastAPIApp --> OllamaService : uses
    FastAPIApp --> JSONParser : uses
    FastAPIApp --> Dilemma : processes
    FastAPIApp --> Transcript : processes
    FastAPIApp --> AgentTurn : returns
    FastAPIApp --> Verdict : returns

    EthicalAgent <|-- DeontologistAgent : implements
    EthicalAgent <|-- ConsequentialistAgent : implements
    EthicalAgent <|-- VirtueEthicistAgent : implements
    EthicalAgent <|-- JudgeAgent : implements

    EthicalAgent --> OllamaService : uses
    EthicalAgent --> JSONParser : uses

    Transcript --> Dilemma : contains
    Transcript --> AgentTurn : contains

    App --> DilemmaForm : renders
    App --> DebateView : renders
    App --> VerdictView : renders
    App --> Sidebar : renders
    App --> APIService : uses

    DebateView --> AgentCard : renders
    
    APIService --> FastAPIApp : calls

    %% Data Flow
    DilemmaForm --> App : submits dilemma
    App --> APIService : requests debate
    APIService --> FastAPIApp : HTTP requests
    FastAPIApp --> EthicalAgent : generates responses
    EthicalAgent --> OllamaService : AI inference
    OllamaService --> JSONParser : parses response
```

## Component Descriptions

### Backend Components

#### **Models (Pydantic)**
- **Dilemma**: Represents an ethical scenario with two options and constraints
- **AgentTurn**: Captures an agent's stance and argument in the debate
- **Transcript**: Complete record of a debate session
- **Verdict**: Final judgment with scores and recommendation

#### **Services**
- **FastAPIApp**: Main application with REST endpoints for debate management
- **OllamaService**: Handles AI model communication (local/cloud Ollama)
- **JSONParser**: Robust parsing of AI responses with fallback strategies

#### **AI Agents**
- **EthicalAgent**: Abstract base class defining agent interface
- **DeontologistAgent**: Rule-based ethical reasoning (duties, rights)
- **ConsequentialistAgent**: Outcome-based ethical reasoning (utility, welfare)
- **VirtueEthicistAgent**: Character-based ethical reasoning (virtues, flourishing)
- **JudgeAgent**: Neutral evaluator providing final verdict

### Frontend Components

#### **Main Application**
- **App**: Root component managing application state and navigation
- **APIService**: Handles HTTP communication with backend

#### **UI Components**
- **DilemmaForm**: Input form for creating ethical scenarios
- **DebateView**: Real-time display of agent arguments and responses
- **VerdictView**: Final judgment display with scores and recommendation
- **Sidebar**: Navigation and debate history management
- **AgentCard**: Individual agent display with thinking states

## Key Design Patterns

### **Strategy Pattern**
Each ethical agent implements the same interface but with different reasoning strategies (deontological, consequentialist, virtue ethics).

### **Observer Pattern**
Frontend components observe state changes and update UI accordingly (thinking states, new arguments).

### **Factory Pattern**
Agent creation and management through the FastAPI endpoints.

### **Model-View-Controller (MVC)**
- **Model**: Pydantic models and data structures
- **View**: React components for UI rendering
- **Controller**: FastAPI endpoints and React event handlers

## Technology Stack

- **Backend**: Python, FastAPI, Pydantic, Ollama
- **Frontend**: React, Vite, Modern JavaScript
- **AI**: Local/Cloud Ollama models (Qwen 2.5 7B)
- **Communication**: REST API with JSON payloads

## Scalability Considerations

The modular design allows for:
- **New Agent Types**: Easy addition through EthicalAgent interface
- **Multiple AI Providers**: OllamaService can be extended or replaced
- **Enhanced UI**: Component-based architecture supports feature expansion
- **Cloud Deployment**: Environment-aware configuration for local/cloud AI
