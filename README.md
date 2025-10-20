# 🧠 MirrorMinds: AI-Powered Ethical Debate Simulator

**MirrorMinds** is an interactive web platform where AI agents debate real-world ethical dilemmas — each representing a distinct moral philosophy. Now featuring a **Custom Agent Builder** that lets users create their own personalized ethical AI agents through natural language descriptions with AI-powered enhancement.

It's an experiment in *AI ethics, philosophy, and reasoning*, built to make complex moral discourse engaging, accessible, and thought-provoking.

---

## 🌟 What's New: Custom Agent Builder

Create your own ethical AI agents with our intuitive 4-step wizard:

1. **Basic Info** - Name your agent and choose an avatar
2. **Personality** - Describe their beliefs and values in natural language  
3. **AI Enhancement** - Watch as AI analyzes and improves your description
4. **Preview** - Test your agent before adding it to debates

**Example:** Transform "This bot cares about animals" into a sophisticated agent with clear reasoning frameworks, decision criteria, and personality traits.

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
- **AI-Powered Enhancement:** Automatic analysis and improvement of descriptions
- **Quality Scoring:** Real-time feedback on clarity, completeness, and consistency
- **Professional UI:** Full-screen wizard with smooth animations and progress tracking

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
- **Agent Management:** CRUD operations for custom agents with JSON storage
- **Enhancement Engine:** AI-powered prompt analysis and improvement using Ollama
- **Debate Orchestration:** Structured API endpoints with error handling and validation
- **Flexible AI Integration:** Support for local Ollama and cloud models

### 💻 **Frontend - React + Vite**
- **Modern React:** Functional components with hooks and context
- **Component Architecture:** Modular, reusable UI components
- **State Management:** Clean separation of concerns with proper data flow
- **Professional Design:** Consistent design system with smooth animations

### 🤖 **AI Integration - Ollama**
- **Local Models:** Currently using Qwen 2.5 7B for reliable local inference
- **Cloud Ready:** Infrastructure for Ollama cloud API integration
- **Structured Prompts:** Consistent agent personas with debate-specific formatting
- **Quality Assurance:** Multiple validation layers and fallback mechanisms

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React, Vite, Modern CSS | Interactive UI with smooth animations |
| **Backend** | FastAPI, Python, Pydantic | RESTful API with data validation |
| **AI Engine** | Ollama, Qwen 2.5 7B | Local AI inference and enhancement |
| **Storage** | JSON Files | Agent data and debate history |
| **Deployment** | Local Development | Ready for cloud deployment |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Ollama installed locally

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

### 🔄 **Phase 1: Core Enhancements**
- [ ] Agent selection for debates (mix default + custom agents)
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