# backend/services/enhancement_service.py
import re
from typing import Dict, List
from models.custom_agent import EnhancementRequest
from main import call_ollama  # Import the existing Ollama function


class PromptAnalyzer:
    """Analyzes user descriptions for completeness and quality"""
    
    def analyze_description(self, description: str) -> Dict[str, float]:
        """Analyze description and return quality scores"""
        scores = {
            "clarity": self._score_clarity(description),
            "completeness": self._score_completeness(description),
            "specificity": self._score_specificity(description),
            "consistency": self._score_consistency(description)
        }
        return scores
    
    def _score_clarity(self, description: str) -> float:
        """Score clarity based on sentence structure and readability"""
        sentences = description.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        
        # Optimal sentence length is 15-20 words
        if 10 <= avg_sentence_length <= 25:
            clarity_score = 10.0
        else:
            clarity_score = max(0, 10 - abs(avg_sentence_length - 17.5) * 0.3)
        
        return min(10.0, clarity_score)
    
    def _score_completeness(self, description: str) -> float:
        """Score completeness based on presence of key elements"""
        description_lower = description.lower()
        
        # Key elements to look for
        elements = {
            "values": any(word in description_lower for word in 
                         ["believe", "value", "prioritize", "important", "care about"]),
            "reasoning": any(word in description_lower for word in 
                           ["because", "reason", "logic", "think", "consider"]),
            "examples": any(word in description_lower for word in 
                          ["example", "such as", "like", "including", "for instance"]),
            "personality": any(word in description_lower for word in 
                             ["compassionate", "logical", "firm", "gentle", "strict", "flexible"]),
            "decision_making": any(word in description_lower for word in 
                                 ["decision", "choose", "evaluate", "judge", "determine"])
        }
        
        present_elements = sum(elements.values())
        completeness_score = (present_elements / len(elements)) * 10
        
        return completeness_score
    
    def _score_specificity(self, description: str) -> float:
        """Score specificity based on concrete details vs vague terms"""
        description_lower = description.lower()
        
        # Vague terms that reduce specificity
        vague_terms = ["good", "bad", "important", "very", "really", "always", "never", "everything"]
        vague_count = sum(description_lower.count(term) for term in vague_terms)
        
        # Specific terms that increase specificity
        specific_indicators = ["specific", "particular", "exactly", "precisely", "namely"]
        specific_count = sum(description_lower.count(term) for term in specific_indicators)
        
        # Calculate specificity score
        word_count = len(description.split())
        vague_ratio = vague_count / max(word_count, 1)
        specific_ratio = specific_count / max(word_count, 1)
        
        specificity_score = max(0, 10 - (vague_ratio * 20) + (specific_ratio * 10))
        
        return min(10.0, specificity_score)
    
    def _score_consistency(self, description: str) -> float:
        """Score consistency based on coherent theme and no contradictions"""
        # Simple consistency check - look for contradictory terms
        description_lower = description.lower()
        
        contradictions = [
            (["always", "never"], ["sometimes", "occasionally"]),
            (["strict", "rigid"], ["flexible", "adaptable"]),
            (["emotional", "feeling"], ["logical", "rational"])
        ]
        
        contradiction_count = 0
        for group1, group2 in contradictions:
            has_group1 = any(term in description_lower for term in group1)
            has_group2 = any(term in description_lower for term in group2)
            if has_group1 and has_group2:
                contradiction_count += 1
        
        # Start with high consistency, reduce for contradictions
        consistency_score = max(0, 10 - (contradiction_count * 2))
        
        return consistency_score
    
    def generate_suggestions(self, description: str, scores: Dict[str, float]) -> List[str]:
        """Generate improvement suggestions based on analysis"""
        suggestions = []
        
        if scores["completeness"] < 6:
            suggestions.append("Consider adding specific examples of what this agent would prioritize")
            suggestions.append("Describe how this agent makes decisions or evaluates situations")
        
        if scores["clarity"] < 6:
            suggestions.append("Try using shorter, clearer sentences to describe the agent")
            suggestions.append("Break down complex ideas into simpler statements")
        
        if scores["specificity"] < 6:
            suggestions.append("Replace vague terms like 'good' or 'important' with specific values")
            suggestions.append("Add concrete examples of the agent's beliefs or principles")
        
        if scores["consistency"] < 6:
            suggestions.append("Review for any contradictory statements about the agent's personality")
            suggestions.append("Ensure the agent's values and reasoning style align consistently")
        
        # General suggestions
        description_lower = description.lower()
        if "reasoning" not in description_lower and "logic" not in description_lower:
            suggestions.append("Describe whether this agent uses logical, emotional, or rule-based reasoning")
        
        if len(description.split()) < 30:
            suggestions.append("Consider expanding the description with more details about the agent's personality")
        
        return suggestions


class PromptEnhancer:
    """Enhances user descriptions using AI"""
    
    ENHANCER_SYSTEM_PROMPT = (
        "You are an expert at creating ethical AI agent personalities. Your job is to take a user's "
        "description of an ethical agent and enhance it into a professional system prompt that will "
        "work well for ethical debates. "
        "\n\nGuidelines for enhancement:"
        "\n- Keep the user's core intent and values"
        "\n- Add clear reasoning framework (deontological, consequentialist, virtue ethics, or custom)"
        "\n- Specify decision-making criteria and examples"
        "\n- Define personality traits that affect argumentation style"
        "\n- Ensure the agent can participate in structured debates"
        "\n- Make it specific enough to be consistent across different scenarios"
        "\n- End with 'Respond in compact JSON only.' for debate compatibility"
        "\n\nReturn only the enhanced system prompt, nothing else."
    )
    
    def enhance_description(self, description: str) -> EnhancementRequest:
        """Enhance a user description into a better system prompt"""
        analyzer = PromptAnalyzer()
        
        # Analyze original description
        scores = analyzer.analyze_description(description)
        suggestions = analyzer.generate_suggestions(description, scores)
        
        # Generate enhancement prompt
        enhancement_prompt = (
            f"Original user description: \"{description}\"\n\n"
            f"Please enhance this into a professional system prompt for an ethical debate agent. "
            f"The agent should maintain the user's core values while being more specific about "
            f"reasoning style, decision-making criteria, and personality traits."
        )
        
        try:
            # Use existing Ollama integration to enhance
            enhanced_prompt = call_ollama(
                self.ENHANCER_SYSTEM_PROMPT,
                enhancement_prompt,
                num_predict=400,
                temp=0.7
            )
            
            # Clean up the response
            enhanced_prompt = enhanced_prompt.strip()
            
            # Ensure it ends with the required JSON instruction
            if not enhanced_prompt.endswith("Respond in compact JSON only."):
                enhanced_prompt += " Respond in compact JSON only."
            
            # Generate improvements list
            improvements = self._identify_improvements(description, enhanced_prompt)
            
            return EnhancementRequest(
                original_description=description,
                enhanced_prompt=enhanced_prompt,
                improvements_made=improvements,
                analysis_scores=scores,
                suggestions=suggestions
            )
            
        except Exception as e:
            # Fallback enhancement if AI fails
            return self._fallback_enhancement(description, scores, suggestions)
    
    def _identify_improvements(self, original: str, enhanced: str) -> List[str]:
        """Identify what improvements were made"""
        improvements = []
        
        original_lower = original.lower()
        enhanced_lower = enhanced.lower()
        
        # Check for added elements
        if "reasoning" not in original_lower and any(word in enhanced_lower for word in ["reasoning", "framework", "approach"]):
            improvements.append("Added clear reasoning framework")
        
        if "decision" not in original_lower and "decision" in enhanced_lower:
            improvements.append("Specified decision-making criteria")
        
        if len(enhanced.split()) > len(original.split()) * 1.5:
            improvements.append("Expanded personality description and behavioral patterns")
        
        if "example" not in original_lower and "example" in enhanced_lower:
            improvements.append("Added specific examples and applications")
        
        if any(word in enhanced_lower for word in ["deontological", "consequentialist", "virtue", "utilitarian"]):
            improvements.append("Connected to established ethical framework")
        
        if "json" in enhanced_lower:
            improvements.append("Ensured compatibility with debate system format")
        
        return improvements if improvements else ["Enhanced clarity and specificity"]
    
    def _fallback_enhancement(self, description: str, scores: Dict[str, float], suggestions: List[str]) -> EnhancementRequest:
        """Provide a basic enhancement if AI enhancement fails"""
        # Create a simple enhanced version
        enhanced = (
            f"You are an ethical agent based on the following principles: {description} "
            f"When evaluating ethical dilemmas, you apply your core values consistently and "
            f"provide clear reasoning for your positions. You engage respectfully with other "
            f"perspectives while maintaining your ethical stance. Respond in compact JSON only."
        )
        
        improvements = [
            "Added structured reasoning approach",
            "Ensured debate system compatibility",
            "Enhanced consistency guidelines"
        ]
        
        return EnhancementRequest(
            original_description=description,
            enhanced_prompt=enhanced,
            improvements_made=improvements,
            analysis_scores=scores,
            suggestions=suggestions
        )


class EnhancementService:
    """Main service for handling agent enhancement requests"""
    
    def __init__(self):
        self.analyzer = PromptAnalyzer()
        self.enhancer = PromptEnhancer()
    
    def enhance_agent_description(self, description: str) -> EnhancementRequest:
        """Main method to enhance an agent description"""
        return self.enhancer.enhance_description(description)
    
    def analyze_only(self, description: str) -> Dict:
        """Analyze description without enhancement"""
        scores = self.analyzer.analyze_description(description)
        suggestions = self.analyzer.generate_suggestions(description, scores)
        
        return {
            "analysis_scores": scores,
            "suggestions": suggestions,
            "overall_score": sum(scores.values()) / len(scores)
        }
    
    def generate_system_prompt(self, enhanced_prompt: str, agent_name: str) -> str:
        """Convert enhanced prompt into final system prompt format"""
        # Format the enhanced prompt as a proper system prompt
        system_prompt = (
            f"You are {agent_name}, an ethical agent. {enhanced_prompt} "
            f"When responding to opponents, ALWAYS start with their name followed by a comma. "
            f"Respond in compact JSON only."
        )
        
        return system_prompt