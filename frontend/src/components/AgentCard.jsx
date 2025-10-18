import './AgentCard.css';

function AgentCard({ turn }) {
  const getAgentInfo = (agent) => {
    const info = {
      Deon: { emoji: '🛡️', fullName: 'Deon (Deontologist)', class: 'deon' },
      Conse: { emoji: '⚖️', fullName: 'Conse (Consequentialist)', class: 'conse' },
      Virtue: { emoji: '✨', fullName: 'Virtue (Virtue Ethicist)', class: 'virtue' },
    };
    return info[agent] || { emoji: '🤖', fullName: agent, class: 'default' };
  };

  const agentInfo = getAgentInfo(turn.agent);

  return (
    <div className={`agent-card ${agentInfo.class}`}>
      <div className="agent-header">
        <div className="agent-name">
          {agentInfo.emoji} {agentInfo.fullName}
        </div>
        <div className={`stance-badge stance-${turn.stance.toLowerCase()}`}>
          Stance: {turn.stance}
        </div>
      </div>
      <div className="agent-argument">{turn.argument}</div>
    </div>
  );
}

export default AgentCard;
