# 🏆 UST AI Agents Orchestrator — Weekly Graded Assignments & Official Auto-Evaluation Hub

This folder contains the **6 Weekly Graded Assignments** (`Week_01_Assignment` through `Week_06_Assignment`) and the **Automated Rubric Evaluation Pipeline** strictly aligned with:
1. [`AI_Agents_Orchestrator_Lab_Rubric_and_Scoring_GuideOct22.docx`](../AI_Agents_Orchestrator_Lab_Rubric_and_Scoring_GuideOct22.docx)
2. [`AI_Agents_Orchestrator_Auto_Evaluation_Scoring_GuideOct22.xlsx`](../AI_Agents_Orchestrator_Auto_Evaluation_Scoring_GuideOct22.xlsx)
3. [`AI_Agents_Orchestrator_Vendor_TOC_V2.xlsx`](../AI_Agents_Orchestrator_Vendor_TOC_V2.xlsx)

## Quick Commands
```powershell
# 1. Evaluate a single week's assignment:
cd Week_01_Assignment
python evaluate_weekly_assignment.py --file candidate_submission_template.md --candidate UST-CAND-001

# 2. Generate the Consolidated 6-Week Program Scorecard (Section 4 Specification):
cd ..
python evaluate_all_weeks_and_program_scorecard.py --candidate UST-GOLD-001
```
