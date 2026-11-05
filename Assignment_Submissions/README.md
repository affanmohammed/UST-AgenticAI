# 📥 UST AI Agents Orchestrator — Assignment Submissions Hub

This directory is the central collection repository for all participant weekly assignment submissions.

---

## 📂 Directory Layout

```text
Assignment_Submissions/
├── Week_01/
│   ├── UST_CAND_001_Week_01_Assignment.ipynb
│   ├── UST_CAND_002_Week_01_Assignment.ipynb
│   └── ...
├── Week_02/
├── Week_03/
├── Week_04/
├── Week_05/
└── Week_06/
```

---

## 📝 Participant Submission Guidelines

1. **File Naming Convention**:
   `<Candidate_ID>_Week_XX_Assignment.ipynb`
   - Example for Candidate `UST-CAND-042` submitting Week 1:
     `Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb`

2. **Submission Workflow**:
   - Create your feature/submission branch:
     ```bash
     git checkout -b submission/UST-CAND-042-week01
     ```
   - Copy your completed notebook:
     ```bash
     cp UST_Assignments/Week_01_Assignment/Week_01_Assignment.ipynb Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb
     ```
   - Run the local auto-evaluator to verify your score:
     ```bash
     python UST_Assignments/Week_01_Assignment/evaluate_weekly_assignment.py Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb --candidate UST-CAND-042
     ```
   - Commit and push to GitHub:
     ```bash
     git add Assignment_Submissions/Week_01/UST_CAND_042_Week_01_Assignment.ipynb
     git commit -m "feat(submission): Week 1 Assignment for UST-CAND-042"
     git push origin submission/UST-CAND-042-week01
     ```
   - Open a Pull Request (PR) to branch `main`.

3. **Security Check**:
   - **NEVER commit `.env` or any file containing API keys.**
   - All `.env` files are ignored by repository `.gitignore`.

