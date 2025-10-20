# backend/models/custom_agent.py
from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class CustomAgent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(min_length=1, max_length=50)
    avatar: str = Field(default="🤖")
    description: str = Field(min_length=50, max_length=1000)
    enhanced_prompt: str
    system_prompt: str
    created_by: str = Field(default="user")
    created_at: datetime = Field(default_factory=datetime.now)
    is_public: bool = Field(default=True)
    usage_count: int = Field(default=0)
    average_rating: float = Field(default=0.0)
    rating_count: int = Field(default=0)


class AgentRating(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    agent_id: str
    debate_id: str
    user_id: str = Field(default="anonymous")
    argument_quality: int = Field(ge=1, le=5)
    consistency: int = Field(ge=1, le=5)
    engagement: int = Field(ge=1, le=5)
    overall_satisfaction: int = Field(ge=1, le=5)
    comment: Optional[str] = Field(default=None, max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)


class EnhancementRequest(BaseModel):
    original_description: str
    enhanced_prompt: str
    improvements_made: List[str]
    analysis_scores: Dict[str, float]
    suggestions: List[str]


class AgentCreationRequest(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    avatar: str = Field(default="🤖")
    description: str = Field(min_length=50, max_length=1000)


class AgentUpdateRequest(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=50)
    avatar: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None, min_length=50, max_length=1000)