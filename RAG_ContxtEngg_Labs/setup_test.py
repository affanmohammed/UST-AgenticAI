"""
Production-Grade Advanced RAG Masterclass: Environment Pre-Flight Verification Script
Run this script before beginning Day 1 and Day 2 Labs.
Usage: python setup_test.py
"""

import os
import sys
import json
import tempfile

# Configure sandboxed cache directories for Torch, HuggingFace, Unsloth, and Matplotlib
temp_dir = tempfile.gettempdir()
os.environ["MPLCONFIGDIR"] = os.path.join(temp_dir, "matplotlib")
os.environ["TORCH_HOME"] = os.path.join(temp_dir, "torch")
os.environ["HF_HOME"] = os.path.join(temp_dir, "hf")
os.environ["TORCHINDUCTOR_CACHE_DIR"] = os.path.join(temp_dir, "torch_inductor")
os.environ["UNSLOTH_CACHE_DIR"] = os.path.join(temp_dir, "unsloth")

# Ensure UTF-8 output encoding for Windows command line compatibility
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def log(msg):
    print(msg, flush=True)

def check_python_version():
    log(f"[*] Python Version: {sys.version.split()[0]}")
    if sys.version_info < (3, 10):
        log("  [!] Warning: Python 3.10+ recommended.")
    else:
        log("  [OK] Python version compatible.")

def check_packages():
    log("\n[*] Checking Core Libraries:")
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("sentence_transformers", "SentenceTransformers"),
        ("chromadb", "ChromaDB"),
        ("qdrant_client", "Qdrant Client"),
        ("rank_bm25", "Rank BM25"),
        ("langchain", "LangChain"),
        ("langgraph", "LangGraph"),
        ("networkx", "NetworkX"),
        ("pydantic", "Pydantic V2"),
        ("mlflow", "MLflow"),
    ]
    for mod_name, label in packages:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "installed")
            log(f"  [OK] {label:22} : {ver}")
        except Exception as e:
            log(f"  [X]  {label:22} : FAILED TO LOAD ({e})")

def check_ollama():
    print("\n[*] Checking Ollama Engine & Models:")
    try:
        import ollama
        client = ollama.Client()
        models_resp = client.list()
        models = [m.model for m in models_resp.models] if hasattr(models_resp, 'models') else []
        print("  [OK] Ollama Service is online and reachable!")
        print(f"  [*] Available Local Models: {models}")
        if not models:
            print("  [!] Recommendation: run 'ollama pull llama3.2:1b' and 'ollama pull nomic-embed-text'")
    except Exception as e:
        print(f"  [!] Ollama connection failed or service not running: {e}")
        print("      To start Ollama: open Ollama app or run 'ollama serve' in your terminal.")

def check_anthropic():
    print("\n[*] Checking Anthropic API Key & Model Configuration:")
    # Load .env if present
    env_paths = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Labs", ".env")
    ]
    for ep in env_paths:
        if os.path.exists(ep):
            try:
                with open(ep, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            k, v = line.split("=", 1)
                            k, v = k.strip(), v.strip().strip("'").strip('"')
                            if k not in os.environ and v:
                                os.environ[k] = v
            except Exception:
                pass

    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6").strip()
    if api_key and (api_key.startswith("sk-ant-") or len(api_key) > 20):
        masked = api_key[:8] + "..." + api_key[-4:]
        print(f"  [OK] ANTHROPIC_API_KEY detected: {masked}")
        print(f"  [*] Primary Frontier Model: {model}")
    else:
        print("  [!] ANTHROPIC_API_KEY not configured. Local Ollama models will be used as backup.")

def check_data_assets():
    print("\n[*] Checking Workshop Sample Datasets:")
    # Prioritize local lab directory first
    local_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "sample_documents")
    parent_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "sample_documents")
    
    data_dir = local_data_dir if os.path.exists(local_data_dir) else parent_data_dir
    print(f"  [*] Data Directory: {data_dir}")
    expected_files = [
        "turbomachinery_manual.md",
        "incident_reports.json",
        "esg_regulatory_compliance.txt",
        "scada_telemetry.csv",
        "telemetry_monitor.py",
        "compressor_curve.png"
    ]
    if os.path.exists(data_dir):
        for f in expected_files:
            fp = os.path.join(data_dir, f)
            if os.path.exists(fp):
                sz = os.path.getsize(fp)
                print(f"  [OK] Found {f:32} ({sz:6d} bytes)")
            else:
                print(f"  [X]  Missing {f}")
    else:
        print(f"  [X]  Data directory not found at {data_dir}")

if __name__ == "__main__":
    print("=" * 65)
    print(" ADVANCED RAG MASTERCLASS - ENVIRONMENT PRE-FLIGHT CHECK")
    print("=" * 65)
    check_python_version()
    check_packages()
    check_anthropic()
    check_ollama()
    check_data_assets()
    print("\n" + "=" * 65)
    print(" Verification complete. Open Jupyter and begin Lab 01!")
    print("=" * 65)
