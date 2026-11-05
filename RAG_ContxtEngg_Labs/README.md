# 🚀 Production-Grade Advanced RAG Architecture: 2-Day Masterclass
### Hands-On Technical Lab Series & Production Engineering Guide

Welcome to the **Advanced Retrieval-Augmented Generation (RAG) Masterclass**. This curriculum is purpose-built for AI engineers, data scientists, and architects who are already familiar with basic naive RAG and are now engineering **production-grade, resilient, secure, and observable RAG systems** for high-stakes enterprise applications (energy, engineering, compliance, and industrial operations).

---

## 🗺️ Masterclass Curriculum & Lab Map

### 📅 Day 1: Complex Ingestion & Advanced Retrieval Engineering
| Lab ID | Module / Focus | Key Challenges Solved | Primary Tooling |
| :--- | :--- | :--- | :--- |
| **[Lab 01](./Lab_01_Multimodal_Document_Parsing.ipynb)** | **Multimodal Document Parsing** | Loss of table structures in scanned PDFs; ignoring visual plots, schematics, and charts in technical manuals. | PyMuPDF, Vision-Language Models (Ollama LLaVA / Llama-3.2-Vision / OpenAI `gpt-4o-mini`), Markdown serialization. |
| **[Lab 02](./Lab_02_Advanced_Chunking_Strategies.ipynb)** | **Advanced Chunking Strategies** | Naive fixed token splits severing contextual meaning and fragmenting data tables. | Semantic Chunking (cosine gradient threshold), Parent-Document / Hierarchical Retrieval, Sentence-Window Retrieval. |
| **[Lab 03](./Lab_03_Production_Vector_Stores.ipynb)** | **Production Vector Stores** | Scalability bottlenecks, lack of payload schema validation, slow pre-filtered searches in massive enterprise datasets. | Qdrant (HNSW Graph, Payload indexing), Dense Vector Ingestion, Strict Boolean & Range metadata filtering. |
| **[Lab 04](./Lab_04_Production_Similarity_Search_Benchmarking.ipynb)** | **Production Similarity Search & Benchmarking** | Flat exact vs approximate retrieval trade-offs; memory exhaustion with dense float32 vectors. | HNSW vs IVF-PQ vs Flat indexing, Scalar Quantization (int8), Latency (p50/p95/p99) vs Recall@K benchmarking. |
| **[Lab 05](./Lab_05_NextGen_Reranking_and_Query_Transformation.ipynb)** | **Next-Gen Re-Ranking & Query Transformation** | Vocabulary mismatch, vague/multi-intent user queries, first-pass retrieval noise. | HyDE (Hypothetical Document Embeddings), Multi-Query Expansion, Reciprocal Rank Fusion (RRF), Cross-Encoder Re-Ranking (`bge-reranker`). |

---

### 📅 Day 2: Agentic Orchestration, Security & Observability
| Lab ID | Module / Focus | Key Challenges Solved | Primary Tooling |
| :--- | :--- | :--- | :--- |
| **[Lab 06](./Lab_06_GraphRAG_Architecture.ipynb)** | **GraphRAG Architecture** | Vector search inability to traverse multi-hop entity relationships and global thematic questions. | Knowledge Graphs, Entity & Relation Triple Extraction, NetworkX, Neo4j Cypher schemas, Hybrid Vector + Graph Traversal. |
| **[Lab 07](./Lab_07_Agentic_RAG_Workflows_LangGraph.ipynb)** | **Agentic RAG Workflows** | Passive, brittle linear RAG pipelines that hallucinate when documents are missing or query is ambiguous. | LangGraph state machines, Corrective RAG (CRAG), Self-RAG, Retrieval Grading Nodes, Query Re-writing, Web fallback. |
| **[Lab 08](./Lab_08_Security_Privacy_and_Guardrails.ipynb)** | **Security, Privacy & Guardrails** | Prompt injection attacks, system prompt leakage, PII/compliance violations, ungrounded hallucinated output. | Reversible PII Anonymization (Presidio/regex engine), Canary token injection detection, Pydantic Structured Output Guardrails. |
| **[Lab 09](./Lab_09_Automated_System_Evaluation_Ragas.ipynb)** | **Automated System Evaluation** | Eyeball testing; lack of quantitative metrics for retrieval quality vs generation faithfulness. | RAG Triad (Context Relevance, Faithfulness/Groundedness, Answer Relevance), Recall@K, LLM-as-a-Judge with Ollama & OpenAI. |
| **[Lab 10](./Lab_10_MLflow_Observability_Tracing_Production.ipynb)** | **MLflow Observability & Tracing** | Production blind spots, retrieval latency bottlenecks, untracked prompt drift, and missing execution traces. | Local MLflow Tracking Server, OpenTelemetry span instrumentation, Node-level latency profiling, Production API packaging. |

---

## 🛠️ Environment Prerequisites & Setup

### 1. Python Environment
Ensure Python 3.10+ is installed. Install all required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Local Open-Source LLMs via Ollama
The entire workshop is designed to run **100% locally and offline** using the **Ollama** engine:
```bash
# Verify Ollama is running
ollama --version

# Pull recommended open-source models:
ollama pull llama3.2:1b          # Fast local instruction & agent reasoning model
ollama pull nomic-embed-text     # High-performance 768-dim dense embedding model
ollama pull qwen2.5:3b           # Optional alternative high-accuracy local judge
```

### 3. Primary Cloud Frontier Model (Anthropic Claude)
All labs use **Anthropic Claude** (e.g. `claude-sonnet-4-6` or `claude-3-5-sonnet-latest`) as the primary cloud reasoning and vision engine.
Configure your key in `.env`:
```ini
ANTHROPIC_API_KEY=sk-ant-api03-...
ANTHROPIC_MODEL=claude-sonnet-4-6
```
*Note: If `ANTHROPIC_API_KEY` is not present or offline, the unified engine automatically falls back to local Ollama models (`llama3.2:1b` / `qwen3.8:27b`). All fake canned mock fallbacks have been removed so you get 100% genuine model responses.*

### 4. Run Pre-Flight Diagnostics
Run the diagnostic script before starting the labs:
```bash
python setup_test.py
```

---

## 📂 UST Client Data Directory Structure
All labs operate on realistic enterprise datasets for **UST Global (UST)** developed with **UST Global**, located in `./data/sample_documents/`:
- `turbomachinery_manual.md`: Comprehensive 10+ page technical operational manual with thermodynamic curves, multi-stage compressor envelopes, ASCV anti-surge modulation algorithms, dry gas seal thresholds, and SIL-3 ESD matrices.
- `incident_reports.json`: 25+ structured industrial incident reports across Fahud, Marmul, Nimr, Lekhwair, Yibal, Harweel, and Qarn Alam.
- `esg_regulatory_compliance.txt`: 8-10 page corporate governance, decarbonization, net-zero methane LDAR targets, and statutory compliance executive registry with realistic PII for privacy/security labs.
- `scada_telemetry.csv`: 289-row multi-station SCADA telemetry log covering suction/discharge pressures, bearing vibrations, temperatures, and alarm thresholds.
- `telemetry_monitor.py`: Production telemetry monitoring service with sliding window analytics and automated event dispatching.
- `compressor_curve.png`: Compressor performance curve map for multimodal vision LLM analysis.

---

## 💡 How to Navigate & Launch Labs
1. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter lab
   ```
2. Open `Lab_01_Multimodal_Document_Parsing.ipynb` to begin Day 1.
3. Use the companion interactive visual portal [`../rag_masterclass_hub.html`](../rag_masterclass_hub.html) to explore interactive animations, vector math calculators, and architecture diagrams alongside your code!
