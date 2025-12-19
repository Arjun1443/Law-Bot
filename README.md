# Law-Bot
LawBot is an AI-powered legal question-answering system focused on the Indian Constitution and legal domain. The project covers the complete pipeline from data preprocessing and fine-tuning to Retrieval-Augmented Generation (RAG) and a final demo-ready chatbot.

📌 Project Objectives
Build a domain-specific legal assistant (LawBot)
Fine-tune a language model on Indian legal data
Reduce hallucinations using Retrieval-Augmented Generation (RAG)
Provide accurate, source-backed legal answers

🧱 Project Architecture
Data Sources
   ↓
Data Cleaning & Normalization (Phase 1)
   ↓
Fine-Tuning Dataset (JSONL)
   ↓
Model Fine-Tuning (Phase 2)
   ↓
RAG Pipeline (Phase 3)
   ↓
Final LawBot Demo (Phase 6)


📂 Repository Structure
LawBot/
│
├── data/
│   ├── lawbot_cleaned.jsonl
│
├── notebooks/
│   ├── preprocessing_report.ipynb
│   ├── finetune_lawbot.ipynb
│   ├── RAG.ipynb
│
├── docs/
│   ├── LawBot_Report.docx
│
├── README.md

⚙️ Phase-wise Explanation
🔹 Phase 1: Data Preparation
Loaded and merged 14,543 legal records
Normalized data into instruction–output format
Removed duplicates based on instruction
Final dataset size: 14,460 records
Split into:
Training: 11,568 (80%)
Validation: 2,892 (20%)
Data Format:
{
  "instruction": "<legal question>",
  "output": "<legal answer>",
  "source": ["CONSTITUTION"]
}
🔹 Phase 2: Model Fine-Tuning
Fine-tuned a base language model on cleaned legal dataset
Optimized for instruction-following legal Q&A
Training and validation handled using JSONL format
Notebook: finetune_lawbot.ipynb
🔹 Phase 3: RAG (Retrieval-Augmented Generation)
Integrated document retrieval for factual grounding
Improved answer accuracy and reduced hallucinations
Legal sources retrieved before response generation
Notebook: RAG.ipynb

🔹 Phase 6: Final Demo
End-to-end LawBot working demo
Example interaction:
User:
What is India according to the Union and its Territory?
LawBot:
India, that is Bharat, shall be a Union of States.
Source: Constitution of India
🛠️ Tech Stack
Python
Jupyter Notebook
JSON / JSONL
Large Language Models (Fine-tuning)
Retrieval-Augmented Generation (RAG)
🚀 How to Run
Clone the repository
git clone https://github.com/your-username/LawBot.git
cd LawBot

Open notebooks in Jupyter
jupyter notebook
Run notebooks in order:
preprocessing_report.ipynb
finetune_lawbot.ipynb
RAG.ipynb

📈 Future Enhancements
Multi-language support (Hindi, Telugu, etc.)
Legal case-law integration
Web & mobile deployment

