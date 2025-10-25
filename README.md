# 🧠 MirrorMinds: AI-Powered Ethical Debate Simulator

**MirrorMinds** is an interactive web platform where AI agents debate real-world ethical dilemmas — each representing a distinct moral philosophy. Now featuring a **Custom Agent Builder** that lets users create their own personalized ethical AI agents through natural language descriptions with AI-powered enhancement.

It's an experiment in *AI ethics, philosophy, and reasoning*, built to make complex moral discourse engaging, accessible, and thought-provoking.

---

## 🌟 What's New: Custom Agent Builder with AI Enhancement

Create your own ethical AI agents with our intuitive 4-step wizard powered by GPT-4o:

1. **Basic Info** - Name your agent and choose from 32 emoji avatars across 4 categories
2. **Personality** - Describe their beliefs and values in natural language (50-1000 chars)
3. **AI Enhancement** - GPT-4o analyzes and improves your description with quality scoring
4. **Preview** - Review side-by-side comparison and create your agent

**Real Example:**
- **Input:** "This agent is a doctor who believes in patient autonomy above all else."
- **Output:** "Dr. Maya Chen is a bioethicist who champions patient autonomy as the cornerstone of medical ethics. She applies a framework rooted in informed consent and bodily autonomy, citing landmark cases like Cruzan v. Director..."

**Quality Metrics:** Clarity, Specificity, Consistency, Depth (scored 0-10)

---

## 🌍 Overview  

In a world where AI decisions increasingly affect human lives, **MirrorMinds** explores how artificial agents might reason about ethics. Users can enter complex dilemmas and watch as philosophical agents debate, challenge, and justify their stances in real time.

### 🤖 Default Agents
Each debate features three distinct philosophical perspectives:
- **⚖️ Deon (Deontologist)** – Rules, duties, universal principles  
- **◆ Conse (Consequentialist)** – Outcomes, happiness, utilitarian reasoning  
- **✦ Virtue (Virtue Ethicist)** – Character, virtues, and moral flourishing  

### ✨ Custom Agents
Create unlimited personalized agents representing any ethical framework:
- **🌱 Environmental Ethics** - Prioritizing ecological sustainability
- **🏛️ Legal Reasoning** - Following constitutional principles  
- **🤝 Community Values** - Emphasizing social harmony
- **💡 Innovation Ethics** - Balancing progress with responsibility

---

## 🚀 Key Features

### 🎯 **Core Debate System**
- **Structured Debate Flow:** Opening arguments → Counter-rounds → Final judgment
- **Real-Time Interaction:** Agents "think" and respond sequentially with loading animations
- **Intelligent Parsing:** Robust JSON parsing with multiple fallback strategies
- **Debate History:** Save, browse, and revisit previous debates

### 🛠️ **Custom Agent Builder**
- **Natural Language Input:** Describe agents in plain English (50-1000 characters)
- **GPT-4o Enhancement:** Recursive improvement with structured output for consistency
- **Quality Scoring:** Four-dimensional analysis (clarity, specificity, consistency, depth)
- **Transparency:** See exactly what improvements were made and why
- **Professional UI:** Full-screen wizard with purple gradient theme and glass morphism
- **Persistent Storage:** JSON-based agent library with full CRUD operations

### 🎨 **Modern User Experience**
- **Responsive Design:** Optimized for desktop, tablet, and mobile
- **Dark Theme:** Professional interface inspired by modern AI tools
- **Smooth Animations:** Engaging transitions and loading states
- **Agent Library:** Browse and manage all available agents (default + custom)

---

## 🧪 Sample Use Cases

### **Academic Ethics**
> Should researchers publish potentially dangerous AI findings?
> *Agents debate academic freedom vs. public safety*

### **Medical Dilemmas**  
> How should doctors allocate limited ICU resources during a pandemic?
> *Utilitarian efficiency vs. individual rights vs. virtue-based care*

### **Technology Ethics**
> Should social media platforms use AI to moderate content?
> *Free speech vs. harm prevention vs. platform responsibility*

### **Environmental Policy**
> Should we prioritize economic growth or environmental protection?
> *Short-term welfare vs. long-term sustainability vs. balanced approaches*

---

## 🏗️ Architecture

### 🔧 **Backend - FastAPI (Python)**
- **Agent Management:** Full CRUD operations with `AgentService` and JSON persistence
- **Enhancement Engine:** Two-stage AI pipeline with `PromptAnalyzer` and `PromptEnhancer`
- **GPT-4o Integration:** Structured output format ensures reliable JSON responses
- **Debate Orchestration:** RESTful API endpoints with Pydantic validation
- **Modular Architecture:** Clean separation between services, models, and routes

### 💻 **Frontend - React + Vite**
- **Modern React:** Functional components with hooks and context
- **Component Architecture:** Modular, reusable UI components
- **State Management:** Clean separation of concerns with proper data flow
- **Professional Design:** Consistent design system with smooth animations

### 🤖 **AI Integration**
- **Debate Engine:** Ollama with Qwen 2.5 7B for local agent responses
- **Enhancement Engine:** OpenAI GPT-4o for intelligent prompt improvement
- **Structured Output:** JSON schema validation ensures consistent responses
- **Recursive Improvement:** Analysis scores guide targeted enhancements
- **Quality Assurance:** Multiple validation layers and error handling

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React, Vite, Modern CSS | Interactive UI with purple gradient theme |
| **Backend** | FastAPI, Python, Pydantic | RESTful API with data validation |
| **Debate AI** | Ollama, Qwen 2.5 7B | Local AI inference for debates |
| **Enhancement AI** | OpenAI GPT-4o | Cloud-based prompt improvement |
| **Storage** | JSON Files | Agent data and debate history |
| **Deployment** | Local Development | Ready for cloud deployment |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Ollama installed locally
- OpenAI API key (for custom agent enhancement)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/khattam/MirrorMind.git
   cd MirrorMind
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   
   # Create .env file with your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

3. **Setup Frontend**
   ```bash
   cd frontend
   npm install
   ```

4. **Start Ollama**
   ```bash
   ollama serve
   ollama pull qwen2.5:7b-instruct-q4_K_M
   ```

5. **Run the Application**
   ```bash
   # Terminal 1 - Backend
   cd backend
   uvicorn main:app --reload

   # Terminal 2 - Frontend  
   cd frontend
   npm run dev
   ```

6. **Open your browser**
   Navigate to `http://localhost:5173`

---

## 📖 Usage

### Creating Your First Custom Agent

1. Click **"✨ Create Custom Agent"** in the sidebar
2. **Step 1:** Enter a name (e.g., "EcoWarrior") and choose an avatar 🌱
3. **Step 2:** Describe your agent's personality and values:
   ```
   This agent believes environmental protection is the highest moral priority. 
   It prioritizes future generations and uses scientific evidence to make decisions.
   ```
4. **Step 3:** Watch the AI enhance your description with reasoning frameworks
5. **Step 4:** Preview and create your agent

### Starting a Debate

1. Enter an ethical dilemma with two clear options
2. Choose which agents should participate (default or custom)
3. Watch the structured debate unfold in real-time
4. Review the final judgment and reasoning

---

## 🎯 Roadmap

### 🔄 **Phase 1: Core Enhancements** (In Progress)
- [x] Custom agent builder with AI enhancement
- [x] Quality scoring and analysis system
- [x] Agent library with CRUD operations
- [ ] Custom agents participating in live debates
- [ ] Community rating system for custom agents
- [ ] Agent performance analytics and metrics
- [ ] Export debates as formatted reports

### 🌐 **Phase 2: Social Features**
- [ ] Public agent library with search and discovery
- [ ] Real-time collaborative debates with multiple users
- [ ] Agent tournaments and competitions
- [ ] Community voting and leaderboards

### 🎓 **Phase 3: Educational Platform**
- [ ] LMS integration (Canvas, Blackboard, Moodle)
- [ ] Curriculum-specific ethical scenarios
- [ ] Student progress tracking and analytics
- [ ] Assignment templates and grading rubrics

### 🚀 **Phase 4: Advanced AI**
- [ ] Multi-model support (GPT-4, Claude, Llama variants)
- [ ] Agent learning and evolution from debates
- [ ] Specialized domain agents (Legal, Medical, Business)
- [ ] Advanced argument analysis and logical fallacy detection

---

## 📊 Technical Deep Dive

### Custom Agent Enhancement Pipeline

```
User Input → Frontend Validation → POST /api/enhance
    ↓
PromptAnalyzer.analyze()
    ├─ Clarity Score (0-10)
    ├─ Specificity Score (0-10)
    ├─ Consistency Score (0-10)
    └─ Depth Score (0-10)
    ↓
PromptEnhancer.enhance(description, scores)
    ├─ Build context-aware prompt
    ├─ Call GPT-4o with structured output
    └─ Parse improvements list
    ↓
Return {enhanced_prompt, scores, improvements}
    ↓
User Reviews → POST /api/agents/create
    ↓
AgentService.create() → JSON Storage
```

### Key Design Decisions

**Separation of Concerns:**
- `PromptAnalyzer`: Scores quality dimensions independently
- `PromptEnhancer`: Focuses on improvement based on scores
- `AgentService`: Handles persistence and CRUD operations

**Structured Output:**
- GPT-4o's JSON schema ensures consistent response format
- Eliminates parsing errors and validation issues
- Enables reliable frontend rendering

**Recursive Improvement:**
- Analyzer identifies weak areas (score < 8/10)
- Enhancer targets those specific dimensions
- Creates measurable quality improvements

**Transparency:**
- Users see original vs enhanced side-by-side
- Explicit list of improvements made
- Quality scores provide objective feedback

For detailed architecture diagrams, see [`docs/agent-builder-architecture.md`](docs/agent-builder-architecture.md)

---

## 🤝 Contributing

We welcome contributions! Whether you're interested in:
- 🐛 **Bug fixes** and performance improvements
- ✨ **New features** and UI enhancements  
- 📚 **Documentation** and examples
- 🧪 **Testing** and quality assurance
- 🎨 **Design** and user experience

Please feel free to open issues, submit pull requests, or start discussions.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Ollama** for providing excellent local AI model infrastructure
- **FastAPI** for the robust and intuitive Python web framework
- **React** and **Vite** for the modern frontend development experience
- The **open-source community** for inspiration and foundational tools

---

## 📞 Contact

**Project Link:** [https://github.com/khattam/MirrorMind](https://github.com/khattam/MirrorMind)

Built with ❤️ for exploring the intersection of AI, ethics, and human reasoning.