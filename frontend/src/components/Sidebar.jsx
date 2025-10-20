import { useState } from 'react';
import './Sidebar.css';

function Sidebar({ stage, debateHistory, onNewDebate, onViewHistory, onDeleteHistory, onOpenAgentBuilder }) {
  const [activeTab, setActiveTab] = useState('history');
  const [expandedAgents, setExpandedAgents] = useState(new Set());
  const [customAgents, setCustomAgents] = useState([]);

  const agentInfo = {
    Deon: {
      name: 'Deon',
      role: 'Deontologist',
      icon: '⚖',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      description: 'Believes moral worth comes from following principles, duties, and rights. Prioritizes integrity, consent, fairness, and respect for universal rules.',
      philosophy: 'Actions are right or wrong based on adherence to moral rules, regardless of consequences.'
    },
    Conse: {
      name: 'Conse',
      role: 'Consequentialist',
      icon: '◆',
      gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      description: 'Evaluates actions purely by their outcomes. Rules are heuristics, not absolutes. Focuses on maximizing overall well-being.',
      philosophy: 'The ends justify the means - actions are right if they produce the best overall consequences.'
    },
    Virtue: {
      name: 'Virtue',
      role: 'Virtue Ethicist',
      icon: '✦',
      gradient: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
      description: 'Focuses on character and human flourishing rather than strict rules or outcomes. Emphasizes virtues like honesty, compassion, and wisdom.',
      philosophy: 'What would a virtuous person do? Character and moral excellence guide ethical decisions.'
    }
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="logo">
          <span className="logo-icon">⚖️</span>
          <span>MirrorMinds</span>
        </div>
      </div>

      <div className="sidebar-content">
        {stage !== 'form' && (
          <button className="new-debate-btn" onClick={onNewDebate}>
            <span>+</span>
            New Debate
          </button>
        )}

        <div className="sidebar-tabs">
          <button 
            className={`tab-btn ${activeTab === 'history' ? 'active' : ''}`}
            onClick={() => setActiveTab('history')}
          >
            History
          </button>
          <button 
            className={`tab-btn ${activeTab === 'agents' ? 'active' : ''}`}
            onClick={() => setActiveTab('agents')}
          >
            Agents
          </button>
        </div>

        <button className="create-agent-btn" onClick={onOpenAgentBuilder}>
          <span className="create-icon">✨</span>
          Create Custom Agent
        </button>

        {activeTab === 'history' && (
          <div className="history-section">
            {debateHistory.length === 0 ? (
              <div className="empty-state">
                <p>No debates yet</p>
                <span>Start your first ethical debate!</span>
              </div>
            ) : (
              <div className="history-list">
                {debateHistory.map((item) => (
                  <div key={item.id} className="history-item">
                    <div className="history-content" onClick={() => onViewHistory(item)}>
                      <h4 className="history-title">{item.title}</h4>
                      <div className="history-meta">
                        <span className="history-date">{item.date}</span>
                        <span className="history-result">
                          Option {item.recommendation} ({item.confidence}%)
                        </span>
                      </div>
                    </div>
                    <button 
                      className="delete-btn"
                      onClick={(e) => {
                        e.stopPropagation();
                        onDeleteHistory(item.id);
                      }}
                    >
                      ×
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === 'agents' && (
          <div className="agents-section">
            <div className="agents-subsection">
              <h3 className="subsection-title">Default Agents</h3>
              {Object.values(agentInfo).map((agent) => (
                <div key={agent.name} className="agent-info-card">
                  <div 
                    className="agent-info-header clickable"
                    onClick={() => {
                      const newExpanded = new Set(expandedAgents);
                      if (newExpanded.has(agent.name)) {
                        newExpanded.delete(agent.name);
                      } else {
                        newExpanded.add(agent.name);
                      }
                      setExpandedAgents(newExpanded);
                    }}
                  >
                    <div className="agent-info-avatar" style={{ background: agent.gradient }}>
                      <span className="agent-info-icon">{agent.icon}</span>
                    </div>
                    <div className="agent-header-text">
                      <h4 className="agent-info-name">{agent.name}</h4>
                      <p className="agent-info-role">{agent.role}</p>
                    </div>
                    <span className="expand-icon">{expandedAgents.has(agent.name) ? '−' : '+'}</span>
                  </div>
                  
                  {expandedAgents.has(agent.name) && (
                    <div className="agent-info-details">
                      <p className="agent-info-description">{agent.description}</p>
                      <div className="agent-info-philosophy">
                        <strong>Core Belief:</strong> {agent.philosophy}
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>

            {customAgents.length > 0 && (
              <div className="agents-subsection">
                <h3 className="subsection-title">Custom Agents</h3>
                {customAgents.map((agent) => (
                  <div key={agent.id} className="agent-info-card custom">
                    <div className="agent-info-header">
                      <div className="agent-info-avatar custom">
                        <span className="agent-info-icon">{agent.avatar}</span>
                      </div>
                      <div className="agent-header-text">
                        <h4 className="agent-info-name">{agent.name}</h4>
                        <p className="agent-info-role">Custom Agent</p>
                        {agent.average_rating > 0 && (
                          <div className="agent-rating">
                            ⭐ {agent.average_rating.toFixed(1)} ({agent.rating_count})
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}


      </div>
    </aside>
  );
}

export default Sidebar;