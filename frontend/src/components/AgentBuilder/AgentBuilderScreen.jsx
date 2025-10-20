import { useState, useEffect } from 'react';
import './AgentBuilderScreen.css';

const API_URL = 'http://127.0.0.1:8000';

function AgentBuilderScreen({ onClose, onAgentCreated }) {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    name: '',
    avatar: '🤖',
    description: ''
  });
  const [enhancement, setEnhancement] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [errors, setErrors] = useState({});

  const steps = [
    { id: 1, title: 'Basic Info', subtitle: 'Name and appearance' },
    { id: 2, title: 'Personality', subtitle: 'Describe your agent' },
    { id: 3, title: 'Enhancement', subtitle: 'AI-powered improvements' },
    { id: 4, title: 'Preview', subtitle: 'Test and finalize' }
  ];

  const avatarCategories = {
    'Emotions': ['😊', '🤔', '😤', '😌', '🥺', '😎', '🤗', '😇'],
    'Objects': ['⚖️', '🔬', '💡', '🎭', '🏛️', '📚', '🔥', '💎'],
    'Nature': ['🌱', '🌊', '🌟', '🌙', '⭐', '🌈', '🔆', '🌸'],
    'Symbols': ['🤖', '🧠', '💭', '⚡', '🎯', '🔮', '🎪', '🎨']
  };

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: null }));
    }
  };

  const validateStep = (step) => {
    const newErrors = {};
    
    if (step === 1) {
      if (!formData.name.trim()) {
        newErrors.name = 'Agent name is required';
      } else if (formData.name.length > 50) {
        newErrors.name = 'Name must be 50 characters or less';
      }
    }
    
    if (step === 2) {
      if (!formData.description.trim()) {
        newErrors.description = 'Description is required';
      } else if (formData.description.length < 50) {
        newErrors.description = 'Description must be at least 50 characters';
      } else if (formData.description.length > 1000) {
        newErrors.description = 'Description must be 1000 characters or less';
      }
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const nextStep = async () => {
    if (!validateStep(currentStep)) return;
    
    if (currentStep === 2) {
      // Trigger enhancement when moving from step 2 to 3
      await enhanceDescription();
    }
    
    setCurrentStep(prev => Math.min(prev + 1, steps.length));
  };

  const prevStep = () => {
    setCurrentStep(prev => Math.max(prev - 1, 1));
  };

  const enhanceDescription = async () => {
    setIsProcessing(true);
    try {
      const response = await fetch(`${API_URL}/api/enhance`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: formData.description })
      });
      
      if (!response.ok) throw new Error('Enhancement failed');
      
      const result = await response.json();
      setEnhancement(result);
    } catch (error) {
      console.error('Enhancement error:', error);
      setErrors({ enhancement: 'Failed to enhance description. You can still proceed.' });
    } finally {
      setIsProcessing(false);
    }
  };

  const createAgent = async (useEnhanced = true) => {
    setIsProcessing(true);
    try {
      const response = await fetch(`${API_URL}/api/agents/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: formData.name,
          avatar: formData.avatar,
          description: useEnhanced && enhancement ? enhancement.enhanced_prompt : formData.description
        })
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to create agent');
      }
      
      const result = await response.json();
      onAgentCreated && onAgentCreated(result.agent);
      onClose();
    } catch (error) {
      console.error('Creation error:', error);
      setErrors({ creation: error.message });
    } finally {
      setIsProcessing(false);
    }
  };

  const getStepProgress = () => (currentStep / steps.length) * 100;

  return (
    <div className="agent-builder-screen">
      {/* Header */}
      <header className="builder-header">
        <div className="header-left">
          <button className="close-button" onClick={onClose}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
            </svg>
          </button>
          <div className="header-title">
            <h1>Create Ethical Agent</h1>
            <p>Build your personalized AI debate participant</p>
          </div>
        </div>
        
        <div className="header-right">
          <div className="step-indicator">
            Step {currentStep} of {steps.length}
          </div>
        </div>
      </header>

      {/* Progress Bar */}
      <div className="progress-container">
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${getStepProgress()}%` }}
          />
        </div>
        <div className="step-labels">
          {steps.map((step) => (
            <div 
              key={step.id} 
              className={`step-label ${currentStep >= step.id ? 'active' : ''} ${currentStep === step.id ? 'current' : ''}`}
            >
              <div className="step-number">{step.id}</div>
              <div className="step-text">
                <div className="step-title">{step.title}</div>
                <div className="step-subtitle">{step.subtitle}</div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <main className="builder-main">
        <div className="builder-content">
          
          {/* Step 1: Basic Info */}
          {currentStep === 1 && (
            <div className="step-content step-1">
              <div className="content-header">
                <h2>Let's start with the basics</h2>
                <p>Give your agent a name and choose how it looks</p>
              </div>
              
              <div className="form-section">
                <div className="input-group">
                  <label htmlFor="agent-name">Agent Name</label>
                  <input
                    id="agent-name"
                    type="text"
                    value={formData.name}
                    onChange={(e) => handleInputChange('name', e.target.value)}
                    placeholder="e.g., EcoWarrior, LogicBot, CompassionateAI"
                    className={errors.name ? 'error' : ''}
                    maxLength={50}
                  />
                  {errors.name && <span className="error-text">{errors.name}</span>}
                  <div className="char-count">{formData.name.length}/50</div>
                </div>

                <div className="avatar-section">
                  <label>Choose Avatar</label>
                  <div className="avatar-categories">
                    {Object.entries(avatarCategories).map(([category, emojis]) => (
                      <div key={category} className="avatar-category">
                        <h4>{category}</h4>
                        <div className="avatar-grid">
                          {emojis.map(emoji => (
                            <button
                              key={emoji}
                              type="button"
                              className={`avatar-option ${formData.avatar === emoji ? 'selected' : ''}`}
                              onClick={() => handleInputChange('avatar', emoji)}
                            >
                              {emoji}
                            </button>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Step 2: Personality */}
          {currentStep === 2 && (
            <div className="step-content step-2">
              <div className="content-header">
                <h2>Describe your agent's personality</h2>
                <p>Tell us what this agent believes, how it thinks, and what values it holds</p>
              </div>
              
              <div className="form-section">
                <div className="textarea-group">
                  <label htmlFor="description">Agent Description</label>
                  <textarea
                    id="description"
                    value={formData.description}
                    onChange={(e) => handleInputChange('description', e.target.value)}
                    placeholder="This agent believes in environmental protection above all else. It prioritizes future generations and uses scientific evidence to make decisions. When evaluating ethical dilemmas, it always considers the long-term impact on the planet and wildlife..."
                    className={errors.description ? 'error' : ''}
                    maxLength={1000}
                    rows={8}
                  />
                  {errors.description && <span className="error-text">{errors.description}</span>}
                  <div className={`char-count ${formData.description.length < 50 ? 'warning' : ''}`}>
                    {formData.description.length}/1000 characters
                    {formData.description.length < 50 && <span className="min-note"> (minimum 50)</span>}
                  </div>
                </div>

                <div className="tips-section">
                  <h4>💡 Tips for Better Agents</h4>
                  <div className="tips-grid">
                    <div className="tip">
                      <div className="tip-icon">🎯</div>
                      <div className="tip-text">
                        <strong>Be Specific</strong>
                        <p>Describe exact values and beliefs</p>
                      </div>
                    </div>
                    <div className="tip">
                      <div className="tip-icon">🧠</div>
                      <div className="tip-text">
                        <strong>Decision Making</strong>
                        <p>Explain how the agent evaluates situations</p>
                      </div>
                    </div>
                    <div className="tip">
                      <div className="tip-icon">💭</div>
                      <div className="tip-text">
                        <strong>Personality Traits</strong>
                        <p>Include traits like logical, compassionate, strict</p>
                      </div>
                    </div>
                    <div className="tip">
                      <div className="tip-icon">📚</div>
                      <div className="tip-text">
                        <strong>Examples</strong>
                        <p>Give examples of what the agent prioritizes</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Step 3: Enhancement */}
          {currentStep === 3 && (
            <div className="step-content step-3">
              <div className="content-header">
                <h2>AI Enhancement Results</h2>
                <p>Our AI analyzed your description and made improvements</p>
              </div>

              {isProcessing ? (
                <div className="processing-state">
                  <div className="processing-animation">
                    <div className="processing-spinner"></div>
                  </div>
                  <h3>Enhancing your agent...</h3>
                  <p>Our AI is analyzing and improving your description</p>
                </div>
              ) : enhancement ? (
                <div className="enhancement-results">
                  <div className="analysis-scores">
                    <h4>Quality Analysis</h4>
                    <div className="scores-grid">
                      {Object.entries(enhancement.analysis_scores).map(([key, score]) => (
                        <div key={key} className="score-card">
                          <div className="score-label">{key.charAt(0).toUpperCase() + key.slice(1)}</div>
                          <div className="score-visual">
                            <div className="score-circle">
                              <svg viewBox="0 0 36 36" className="circular-chart">
                                <path
                                  className="circle-bg"
                                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                />
                                <path
                                  className="circle"
                                  strokeDasharray={`${(score / 10) * 100}, 100`}
                                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                />
                              </svg>
                              <div className="score-text">{score.toFixed(1)}</div>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="comparison-section">
                    <div className="comparison-grid">
                      <div className="original-card">
                        <h4>Your Original</h4>
                        <div className="description-text">{formData.description}</div>
                      </div>
                      <div className="enhanced-card">
                        <h4>AI Enhanced</h4>
                        <div className="description-text enhanced">{enhancement.enhanced_prompt}</div>
                      </div>
                    </div>
                  </div>

                  {enhancement.improvements_made.length > 0 && (
                    <div className="improvements-section">
                      <h4>✨ Improvements Made</h4>
                      <div className="improvements-list">
                        {enhancement.improvements_made.map((improvement, index) => (
                          <div key={index} className="improvement-item">
                            <div className="improvement-icon">✓</div>
                            <div className="improvement-text">{improvement}</div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <div className="error-state">
                  <div className="error-icon">⚠️</div>
                  <h3>Enhancement Failed</h3>
                  <p>Don't worry, you can still create your agent with the original description.</p>
                </div>
              )}
            </div>
          )}

          {/* Step 4: Preview */}
          {currentStep === 4 && (
            <div className="step-content step-4">
              <div className="content-header">
                <h2>Preview Your Agent</h2>
                <p>Review your agent before creating it</p>
              </div>

              <div className="preview-section">
                <div className="agent-preview-card">
                  <div className="preview-header">
                    <div className="preview-avatar">{formData.avatar}</div>
                    <div className="preview-info">
                      <h3>{formData.name}</h3>
                      <p>Custom Ethical Agent</p>
                    </div>
                  </div>
                  
                  <div className="preview-description">
                    <h4>Personality & Values</h4>
                    <p>{enhancement ? enhancement.enhanced_prompt : formData.description}</p>
                  </div>

                  {enhancement && (
                    <div className="preview-stats">
                      <div className="stat">
                        <span className="stat-label">Quality Score</span>
                        <span className="stat-value">
                          {(Object.values(enhancement.analysis_scores).reduce((a, b) => a + b, 0) / Object.keys(enhancement.analysis_scores).length).toFixed(1)}/10
                        </span>
                      </div>
                      <div className="stat">
                        <span className="stat-label">Improvements</span>
                        <span className="stat-value">{enhancement.improvements_made.length}</span>
                      </div>
                    </div>
                  )}
                </div>

                <div className="creation-options">
                  <button 
                    className="create-btn primary"
                    onClick={() => createAgent(true)}
                    disabled={isProcessing}
                  >
                    {isProcessing ? 'Creating Agent...' : 'Create Agent'}
                  </button>
                  
                  {enhancement && (
                    <button 
                      className="create-btn secondary"
                      onClick={() => createAgent(false)}
                      disabled={isProcessing}
                    >
                      Use Original Description
                    </button>
                  )}
                </div>

                {errors.creation && (
                  <div className="error-message">{errors.creation}</div>
                )}
              </div>
            </div>
          )}
        </div>
      </main>

      {/* Footer Navigation */}
      <footer className="builder-footer">
        <div className="footer-content">
          <button 
            className="nav-btn secondary"
            onClick={prevStep}
            disabled={currentStep === 1}
          >
            ← Previous
          </button>
          
          <div className="footer-center">
            <div className="step-dots">
              {steps.map((step) => (
                <div 
                  key={step.id}
                  className={`step-dot ${currentStep >= step.id ? 'active' : ''}`}
                />
              ))}
            </div>
          </div>
          
          {currentStep < steps.length ? (
            <button 
              className="nav-btn primary"
              onClick={nextStep}
              disabled={isProcessing}
            >
              Next →
            </button>
          ) : (
            <div className="footer-spacer" />
          )}
        </div>
      </footer>
    </div>
  );
}

export default AgentBuilderScreen;