import { useState } from 'react';
import AgentSelector from './AgentSelector';
import './DilemmaForm.css';

function DilemmaForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    title: '',
    A: '',
    B: '',
    constraints: '',
  });
  
  const [selectedAgents, setSelectedAgents] = useState(['deon', 'conse', 'virtue']); // Default selection

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validAgents = selectedAgents.filter(agent => agent !== null);
    if (validAgents.length !== 3) {
      alert('Please select exactly 3 agents for the debate.');
      return;
    }
    onSubmit(formData, validAgents);
  };

  return (
    <div className="dilemma-form card">
      <h2>Enter Your Ethical Dilemma</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="e.g., Academic Integrity vs Compassion"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="constraints">Constraints/Context</label>
          <textarea
            id="constraints"
            name="constraints"
            value={formData.constraints}
            onChange={handleChange}
            rows="2"
            placeholder="Any relevant constraints or context..."
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="A">Option A</label>
          <textarea
            id="A"
            name="A"
            value={formData.A}
            onChange={handleChange}
            rows="2"
            placeholder="Describe the first option..."
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="B">Option B</label>
          <textarea
            id="B"
            name="B"
            value={formData.B}
            onChange={handleChange}
            rows="2"
            placeholder="Describe the second option..."
            required
          />
        </div>

        <AgentSelector 
          selectedAgents={selectedAgents}
          onSelectionChange={setSelectedAgents}
        />

        <button 
          type="submit" 
          className={`btn btn-primary ${selectedAgents.filter(a => a !== null).length !== 3 ? 'disabled' : ''}`}
          disabled={selectedAgents.filter(a => a !== null).length !== 3}
        >
          Start Debate with Selected Team
        </button>
      </form>
    </div>
  );
}

export default DilemmaForm;
