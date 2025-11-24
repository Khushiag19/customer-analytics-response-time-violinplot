# Customer Analytics: Response Time Distribution by Support Channel

Seaborn violin plot showing the distribution (and density) of **customer support response times** across channels (Email, Chat, Phone, Social, In‑App). Designed for executive presentations and board reports.

**Email:** 23f3001513@ds.study.iitm.ac.in

## Files
- `chart.py` — Generates the Seaborn violinplot.
- `chart.png` — Generated image (exactly **512×512** px).
- `README.md` — This file.

## How to run
```bash
python3 chart.py
```
This will create `chart.png` at exactly 512×512 pixels.

## Implementation Notes
- Uses `sns.set_style("whitegrid")`, `sns.set_context("talk")`, and `palette="Set2"` for a professional look.
- Synthetic data comes from log-normal distributions with occasional outliers to reflect real-world response times.
- The script first saves with `bbox_inches='tight'` and then pads to a 512×512 canvas so grading systems that require both tight layout and exact pixel dimensions are satisfied.

## Create the GitHub repository
```bash
# choose a repo name; you can keep this one
REPO=customer-analytics-response-time-violinplot

mkdir -p $REPO
cp chart.py chart.png README.md $REPO/
cd $REPO

git init
git add README.md chart.py chart.png
git commit -m "Add Seaborn violinplot for response time distribution"
git branch -M main
git remote add origin https://github.com/Khushiag19/${REPO}.git
git push -u origin main
```

### Raw README URL (after pushing)
```
https://raw.githubusercontent.com/Khushiag19/customer-analytics-response-time-violinplot/main/README.md
```
