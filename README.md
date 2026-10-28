# LawBot — Indian Legal Q&A Research and Demo

A legal-domain learning project combining data-preparation, fine-tuning and RAG notebooks with a Streamlit Q&A demonstration.

## Why this project matters

Domain-specific AI requires careful data preparation and a clear account of how answers are produced. This repository explores those stages for Indian legal material.

## What is implemented

| Component | Location | Role |
| --- | --- | --- |
| Data preparation | `LawBot/LowBot_Demo/preprocessing_report.ipynb` | Preparing legal Q&A data |
| Fine-tuning experiment | `LawBot/LowBot_Demo/finetune_lawbot.ipynb` | Model training workflow |
| Retrieval experiment | `LawBot/LowBot_Demo/RAG.ipynb` | Notebook-based RAG exploration |
| Streamlit demo | `LawBot/LowBot_Demo/LLM_LLJ/LLM_LLJ/app.py` | Substring matching against JSON Q&A files |
| Project report | `LawBot/LowBot_Demo/LawBot_Report.docx` | Supporting documentation |

The runnable Streamlit app searches curated question–answer pairs; it does not invoke the fine-tuned model or notebook RAG pipeline.

## Run the demo

```bash
git clone https://github.com/Arjun1443/Law-Bot.git
cd Law-Bot/LawBot/LowBot_Demo/LLM_LLJ/LLM_LLJ
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

**Setup requirement:** the current app contains a machine-specific Windows data path in `load_qaa_data()`. Change it to the local `data/` directory before starting. Review the notebook-specific dependency and dataset requirements separately.

## Skills demonstrated

Python · Streamlit · JSON/JSONL data preparation · legal-domain Q&A · fine-tuning and retrieval experiments

## Limitations

This is educational material, not legal advice. Dataset currency, completeness, and answer accuracy are not established by the presence of a matching Q&A pair. Model and retrieval experiments require their own evaluation; no accuracy improvement is claimed here without a reproducible comparison.
