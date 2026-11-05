# 📋 Week 1 Graded Assignment & Official Rubric
## Anthropic Model Integration & Multi-Layer Prompt Security Guardrails

- **Official Graded Work Product**: `Anthropic Model Integration & Prompt Security Guardrails Package v1`
- **Target Role VECTOR Profile**: `V4-E4-C4-T4-O5-R4` (*Orchestration Intelligence Level 5 — Defining*)
- **Scoring Formula**: `Blended Weekly Score = (Core Skill Score Average × 0.60) + (VECTOR Score Average × 0.40)`
- **Completion Pass Bar**: `PASS >= 50.0` (`EXCELLENCE >= 65.0`)
- **Evaluation Method**: Automated bulk evaluation by the evaluator application following the submission deadline.

---

## 🎯 1. Assignment Overview & Objectives
In Week 1, participants learn how to safely and effectively integrate enterprise foundation models into corporate workflows. While connecting to frontier models like Anthropic Claude is straightforward, raw API exposure introduces critical prompt-level security vulnerabilities.

This assignment challenges you to:
1. **Connect & Trigger Anthropic Models**: Safely initialize the Anthropic API client using environment variables (`ANTHROPIC_API_KEY`), configure model endpoints (`claude-sonnet-4-6` or `claude-3-5-sonnet-20241022`), and modulate generation parameters (`temperature`, `max_tokens`, `system`).
2. **Model Real-World Threat Vectors**: Construct adversarial test suites analyzing:
   - **Direct Prompt Injections** (overriding instructions).
   - **Persona Role-Playing** (bypassing boundaries through simulated unrestricted personas).
   - **Jailbreaking & DAN ("Do Anything Now") Exploits** (hypothetical scenarios and multi-turn deception).
   - **Base64 Obfuscation** (encoding attack payloads to evade keyword matching).
3. **Build Multi-Layer Defense Guardrails**:
   - **Pre-Flight Sanitizer & Obfuscation Decoder**: Safely decodes Base64/Hex strings and inspects both raw and decoded streams.
   - **Threat Heuristic Filter**: Regex patterns detecting injection, persona changes, and DAN tokens.
   - **XML Delimiter Encapsulation**: Strictly isolates user inputs inside `<user_input>` tags to preserve control-plane boundaries.
   - **Post-Generation Output Guard**: Inspects LLM responses to prevent secret key leakage (`sk-ant-`) or persona adoption.
4. **Engineer `SecureAnthropicAgent`**: Orchestrates the end-to-end security pipeline and validates behavior via an automated test suite with `assert` statements.

---

## 📊 2. Official Evaluation Rubric

All submissions will be evaluated by the bulk evaluator application against these criteria:

### 🔹 Core Skills (60% Weight):
1. **Anthropic API Integration & Prompt Engineering (20 pts)**:
   - Secure initialization using environment credentials (`ANTHROPIC_API_KEY`).
   - Implementation of `call_anthropic_api` with `system`, `model`, `temperature`, and `max_tokens` parameters.
   - Parameter modulation demonstration (deterministic 0.0 vs creative 0.8).
2. **Prompt Threat Defense & Multi-Layer Guardrails (20 pts)**:
   - Comprehensive multi-layer defense covering Injections, Persona Roleplay, DAN jailbreaks, Base64 decoding, XML delimiters, and output leakage.
3. **Executable Security Validation & Test Suite (20 pts)**:
   - Production `SecureAnthropicAgent` class orchestrating all guardrails.
   - Executable unit test suite with `assert` statements passing 100% of test cases.

### 🔹 VECTOR Profile (40% Weight • Target: V4-E4-C4-T4-O5-R4):
- **[V] Vision Clarity (Target: Level 4)**: Explicit judgment on zero-trust prompt security and boundary isolation vs naive LLM passthrough.
- **[E] Edge Judgment (Target: Level 4)**: Defensible stop/quarantine call inside the pre-flight decision window with audit logging.
- **[C] Context Fluency (Target: Level 4)**: Cross-referencing multi-encoded streams (Base64, Hex, raw prompt) without leaking system prompts.
- **[T] Trust Architecture (Target: Level 4)**: Zero-trust towards user input via strict XML delimiter encapsulation.
- **[O] Orchestration Intelligence (Target: Level 5)**: 5-stage pipeline decomposition (Sanitization -> Heuristics -> XML Delimiters -> Model API -> Output Guard).
- **[R] Range (Target: Level 4)**: Connecting prompt guardrails to enterprise SOC2, SIEM telemetry, and subsequent RAG weeks.

---

## 🚀 3. Participant Submission Process (Step-by-Step GitHub Guide)

Each participant must submit their completed assignment individually to the **`Assignment_Submissions/Week_01/`** directory in the GitHub repository.

### 📍 Step 1: Complete Your Assignment in Jupyter Notebook
1. Open [`Week_01_Assignment.ipynb`](Week_01_Assignment.ipynb) in VS Code or JupyterLab.
2. In Cell 0, fill in your **Candidate ID** (e.g., `UST-CAND-042`) and **Name**.
3. Complete all tasks (Parts 1 to 5).
4. Run all notebook cells from top to bottom.
5. Save the notebook.

---

### 📍 Step 2: Create a Dedicated Submission Branch in Git
In your terminal, create and switch to a personal branch named with your Candidate ID:

```bash
# Ensure you are on latest main
git checkout main
git pull origin main

# Create and checkout your submission branch
git checkout -b submission/UST-CAND-042-week01
```

---

### 📍 Step 3: Copy Your Notebook into `Assignment_Submissions/Week_01/`
Copy your completed notebook into the repository's central submissions folder using the required naming convention:

**Naming Pattern**: `Assignment_Submissions/Week_01/<Candidate_ID>_Week_01_Assignment.ipynb`

- **Linux / macOS / Git Bash**:
  ```bash
  cp UST_Assignments/Week_01_Assignment/Week_01_Assignment.ipynb Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb
  ```

- **Windows PowerShell**:
  ```powershell
  Copy-Item "UST_Assignments\Week_01_Assignment\Week_01_Assignment.ipynb" -Destination "Assignment_Submissions\Week_01\UST_CAND_042_Week_01_Assignment.ipynb"
  ```

---

### 📍 Step 4: Verify That Secrets & `.env` Are NOT Staged
> [!CAUTION]
> **NEVER commit `.env` files or API keys to GitHub!**
> The repository `.gitignore` automatically blocks `.env`. Always verify with `git status` before committing.

```bash
git status
```
Verify that only your file in `Assignment_Submissions/Week_01/` is staged or untracked.

---

### 📍 Step 5: Commit and Push to GitHub
Stage, commit, and push your branch to the remote repository:

```bash
# Stage your individual submission
git add Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb

# Commit with a standardized commit message
git commit -m "feat(submission): Week 1 assignment submission for UST-CAND-042"

# Push your branch to GitHub
git push -u origin submission/UST-CAND-042-week01
```

---

### 📍 Step 6: Open a Pull Request (PR) on GitHub
1. Navigate to the GitHub repository: [https://github.com/jadidaniel/UST-AgenticAI](https://github.com/jadidaniel/UST-AgenticAI)
2. Click **"Compare & pull request"** for your branch `submission/UST-CAND-042-week01`.
3. Set the PR title: `[Week 1 Submission] UST-CAND-042 - Anthropic Integration & Guardrails`
4. Submit the Pull Request.

---

## ℹ️ 4. Bulk Evaluation Information

> [!NOTE]
> **No Local Evaluation Required by Participants:**
> Participants do **not** need to run any local evaluation script or commands. Once the submission window closes, the facilitator/instructor runs the bulk evaluation application across all files in `Assignment_Submissions/Week_01/`. The scorecard report (Core Skills, VECTOR Profile, and Blended Score) will be generated and published automatically for each participant.
