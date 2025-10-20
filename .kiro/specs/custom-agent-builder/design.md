# Custom Agent Builder Design

## Overview

The Custom Agent Builder is a comprehensive system that enables users to create personalized ethical AI agents through natural language descriptions. The system consists of a user-friendly interface for agent creation, an AI-powered enhancement engine, and a management system for organizing and using custom agents.

## Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend UI   │◄──►│  Backend API    │◄──►│  AI Enhancement │
│                 │    │                 │    │     Engine      │
│ - Agent Builder │    │ - Agent CRUD    │    │ - Prompt Analysis│
│ - Agent Library │    │ - Enhancement   │    │ - Enhancement   │
│ - Agent Selector│    │ - Rating System │    │ - Validation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Data Storage  │
                       │                 │
                       │ - Agent Configs │
                       │ - User Ratings  │
                       │ - Usage Stats   │
                       └─────────────────┘
```

### Component Architecture

```
Frontend Components:
├── AgentBuilder/
│   ├── AgentBuilderForm.jsx      # Main creation interface
│   ├── DescriptionInput.jsx      # Natural language input
│   ├── EnhancementPanel.jsx      # AI enhancement display
│   └── AgentPreview.jsx          # Test agent functionality
├── AgentLibrary/
│   ├── AgentLibrary.jsx          # Browse all agents
│   ├── AgentCard.jsx             # Individual agent display
│   └── AgentSelector.jsx         # Multi-select for debates
└── AgentManagement/
    ├── MyAgents.jsx              # User's created agents
    ├── AgentEditor.jsx           # Edit existing agents
    └── AgentRating.jsx           # Rate agent performance

Backend Services:
├── models/
│   ├── custom_agent.py           # Agent data models
│   ├── agent_rating.py           # Rating system models
│   └── enhancement_request.py    # Enhancement tracking
├── services/
│   ├── agent_service.py          # Agent CRUD operations
│   ├── enhancement_service.py    # AI prompt enhancement
│   ├── rating_service.py         # Community rating system
│   └── validation_service.py     # Input validation
└── api/
    ├── agents.py                 # Agent management endpoints
    ├── enhancement.py            # Enhancement endpoints
    └── ratings.py                # Rating endpoints
```

## Components and Interfaces

### Frontend Components

#### AgentBuilderForm
**Purpose:** Main interface for creating new agents
**Props:**
- `onAgentCreated: (agent) => void` - Callback when agent is successfully created
- `initialDescription?: string` - Pre-populate with existing description

**State:**
- `description: string` - User's natural language input
- `agentName: string` - Custom agent name
- `agentAvatar: string` - Selected emoji/icon
- `enhancement: EnhancementResult | null` - AI enhancement results
- `isAnalyzing: boolean` - Loading state for AI analysis

#### EnhancementPanel
**Purpose:** Display AI enhancement results and allow user interaction
**Props:**
- `original: string` - Original user description
- `enhanced: string` - AI-enhanced version
- `improvements: string[]` - List of improvements made
- `onAccept: () => void` - Accept enhanced version
- `onReject: () => void` - Reject and use original
- `onEdit: (text: string) => void` - Manual editing callback

#### AgentLibrary
**Purpose:** Browse and manage all available agents
**Props:**
- `agents: Agent[]` - List of all agents (default + custom)
- `onAgentSelect?: (agent: Agent) => void` - Selection callback
- `showRatings: boolean` - Display community ratings
- `allowMultiSelect: boolean` - Enable multi-selection mode

### Backend Models

#### CustomAgent
```python
class CustomAgent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(min_length=1, max_length=50)
    avatar: str = Field(default="🤖")
    description: str = Field(min_length=50, max_length=1000)
    enhanced_prompt: str
    system_prompt: str
    created_by: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_public: bool = Field(default=True)
    usage_count: int = Field(default=0)
    average_rating: float = Field(default=0.0)
    rating_count: int = Field(default=0)
```

#### AgentRating
```python
class AgentRating(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    agent_id: str
    debate_id: str
    user_id: str
    argument_quality: int = Field(ge=1, le=5)
    consistency: int = Field(ge=1, le=5)
    engagement: int = Field(ge=1, le=5)
    overall_satisfaction: int = Field(ge=1, le=5)
    comment: Optional[str] = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
```

#### EnhancementRequest
```python
class EnhancementRequest(BaseModel):
    original_description: str
    enhanced_prompt: str
    improvements_made: List[str]
    analysis_scores: Dict[str, float]
    suggestions: List[str]
```

### API Endpoints

#### Agent Management
```python
POST /api/agents/create
- Body: {name, avatar, description}
- Returns: CustomAgent with enhanced_prompt

GET /api/agents
- Query: ?public_only=true&search=term&limit=20
- Returns: List[CustomAgent]

GET /api/agents/{agent_id}
- Returns: CustomAgent details

PUT /api/agents/{agent_id}
- Body: {name?, avatar?, description?}
- Returns: Updated CustomAgent

DELETE /api/agents/{agent_id}
- Returns: Success confirmation
```

#### Enhancement Engine
```python
POST /api/enhance
- Body: {description: string}
- Returns: EnhancementRequest

POST /api/agents/{agent_id}/regenerate
- Returns: CustomAgent with new enhanced_prompt
```

#### Rating System
```python
POST /api/agents/{agent_id}/rate
- Body: AgentRating (without id, agent_id)
- Returns: Success confirmation

GET /api/agents/{agent_id}/ratings
- Returns: List[AgentRating] and aggregate stats
```

## Data Models

### Agent Storage Structure
```json
{
  "id": "agent_123",
  "name": "EcoWarrior",
  "avatar": "🌱",
  "description": "This bot believes environmental protection is the highest moral priority...",
  "enhanced_prompt": "You are EcoWarrior, an ethical agent who prioritizes environmental sustainability...",
  "system_prompt": "You are EcoWarrior, an ethical agent who prioritizes environmental sustainability above economic considerations. You believe in intergenerational justice and use consequentialist reasoning focused on long-term environmental outcomes. When evaluating dilemmas, you consistently ask: 'What are the environmental implications?' and 'How does this affect future generations?' You are passionate but evidence-based, often citing climate science and ecological research. You support strong environmental regulations even when they impose economic costs. Respond in compact JSON only.",
  "created_by": "user_456",
  "created_at": "2024-01-15T10:30:00Z",
  "is_public": true,
  "usage_count": 15,
  "average_rating": 4.2,
  "rating_count": 8
}
```

### Enhancement Analysis Structure
```json
{
  "analysis_scores": {
    "clarity": 7.5,
    "completeness": 6.0,
    "specificity": 8.0,
    "consistency": 9.0
  },
  "missing_elements": [
    "reasoning_framework",
    "decision_criteria"
  ],
  "suggestions": [
    "Add specific examples of environmental priorities",
    "Define how you weigh short-term vs long-term consequences"
  ],
  "improvements_made": [
    "Added consequentialist reasoning framework",
    "Specified decision-making criteria",
    "Enhanced personality traits with evidence-based approach"
  ]
}
```

## Error Handling

### Input Validation
- Description length validation (50-1000 characters)
- Profanity and inappropriate content filtering
- Duplicate agent name detection
- Rate limiting for enhancement requests

### AI Enhancement Failures
- Fallback to original description if enhancement fails
- Retry mechanism with different parameters
- Manual editing option as backup
- Clear error messages for users

### Agent Creation Failures
- Validation error display with specific field feedback
- Auto-save draft descriptions to prevent data loss
- Graceful degradation if enhancement service is unavailable

## Testing Strategy

### Unit Tests
- Agent model validation and serialization
- Enhancement engine prompt generation
- Rating calculation and aggregation
- Input sanitization and validation

### Integration Tests
- Complete agent creation workflow
- Enhancement service integration
- Database operations and data persistence
- API endpoint functionality

### User Experience Tests
- Agent creation flow usability
- Enhancement quality validation
- Agent performance in actual debates
- Community rating system effectiveness

### Performance Tests
- Enhancement engine response times
- Agent library loading with large datasets
- Concurrent agent creation requests
- Database query optimization

## Security Considerations

### Input Sanitization
- XSS prevention in agent descriptions
- SQL injection protection
- Content filtering for inappropriate material
- Rate limiting to prevent abuse

### User Authentication
- Agent ownership verification
- Public/private agent access controls
- Rating system integrity (prevent self-rating)
- API authentication for agent operations

### Data Privacy
- User-created agent content protection
- Optional anonymous agent creation
- GDPR compliance for user data
- Secure storage of agent configurations

## Performance Optimization

### Caching Strategy
- Agent library caching with TTL
- Enhancement result caching for similar descriptions
- Rating aggregation caching
- Popular agent preloading

### Database Optimization
- Indexed searches on agent names and descriptions
- Efficient rating aggregation queries
- Pagination for large agent libraries
- Connection pooling for concurrent requests

### AI Enhancement Optimization
- Batch processing for multiple enhancement requests
- Model response caching for similar inputs
- Async processing for non-blocking user experience
- Fallback to simpler enhancement if primary fails