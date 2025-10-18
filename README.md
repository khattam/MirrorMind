# 🧠 MirrorMinds: AI-Powered Ethical Debate Simulator  

**MirrorMinds** is an interactive web platform where AI agents debate real-world ethical dilemmas — each representing a distinct moral philosophy.  
It’s an experiment in *AI ethics, philosophy, and reasoning*, built to make complex moral discourse engaging, accessible, and thought-provoking.

---

## 🌍 Overview  

In a world where AI decisions increasingly affect human lives, **MirrorMinds** explores how artificial agents might reason about ethics.  
Users can enter complex dilemmas and watch as three philosophical agents debate, challenge, and justify their stances in real time.

Each debate unfolds like an academic roundtable between:
- 🧩 **Deon (Deontologist)** – Rules, duties, universal principles  
- ⚖️ **Conse (Consequentialist)** – Outcomes, happiness, utilitarian reasoning  
- 🌿 **Virtue (Virtue Ethicist)** – Character, virtues, and moral flourishing  

---

## 🚀 Why MirrorMinds?  

Ethical reasoning is often inaccessible — buried in dense philosophical texts.  
MirrorMinds aims to **democratize moral reasoning** by turning philosophy into a living, conversational experience.

### ✨ Key Goals  
- **Accessible Ethics:** Make moral frameworks tangible and interactive  
- **Multi-Perspective Reasoning:** Show how different systems reach — or clash on — conclusions  
- **Educational Insight:** Teach ethics by letting users *watch it in action*  
- **Decision Support:** Provide structured moral reasoning for real-world dilemmas  

---

## 🧩 Architecture  

### 🧠 Backend — **FastAPI (Python)**  
- Modular API endpoints for debate orchestration  
- Structured JSON-based communication with AI agents  
- Integrated retry, validation, and error-handling logic  
- Ready for both **local Ollama** and **cloud-hosted OSS models**

### 💻 Frontend — **React + Vite**  
- Modern functional components with hooks  
- Responsive, dark-themed UI inspired by ChatGPT and Claude  
- Animated debate flow with sequential agent responses  
- Smooth transitions, collapsible rounds, and sidebar history  

### 🤖 AI Integration — **Ollama + Local LLMs**  
- Currently using **Qwen 2.5 7B** (local inference)  
- Migrating to **Ollama Cloud GPT-OSS 20B** for faster responses  
- Structured prompt templates for consistent agent personas  
- Robust JSON parsing and debate schema validation  

---

## ⚙️ Core Features  

| Feature | Description |
|----------|-------------|
| 🧠 **Three Ethical Agents** | Each agent embodies a distinct moral framework |
| 💬 **Structured Debate Flow** | Opening → Rebuttals → Final Judgment |
| ⚡ **Real-Time Interaction** | Agents “think” and respond sequentially |
| 🕰 **Debate History** | Browse and revisit previous debates |
| 📚 **Agent Insights** | Learn about each philosophy in context |
| 🧩 **Error Resilience** | Built-in fallback logic and safe parsing |
| 📱 **Responsive UI** | Fully optimized for both desktop and mobile |

---

## 🧪 Sample Ethical Scenarios  

**Technology & AI**  
> Should autonomous weapons ever be permitted?  
> Should AI systems lie to prevent harm?  

**Medical Ethics**  
> How should doctors allocate limited ICU resources?  

**Academic Integrity**  
> Is it ever justified to use AI tools in academic writing?  

**Business Ethics**  
> Should companies prioritize profit over employee well-being?  

---


## 🛠️ Tech Stack  

**Frontend:** React / Vite / TypeScript  
**Backend:** FastAPI / Python  
**AI Integration:** Ollama (Local + Cloud) · Qwen 2.5 7B → GPT-OSS 20B  
**Styling:** CSS Modules · Responsive Design  
**Deployment:** Railway + Vercel (Planned)


---
