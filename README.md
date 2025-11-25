# SOX2-MYC-SNCA Discovery

SOX2 knockdown reduces both MYC (44%) and SNCA (38%).

## How to Run

**Step 1:** Download data from Virtual Cell Challenge and put in `data/vcc_data.h5ad`

**Step 2:** Install packages
```bash
pip install -r requirements.txt
```

**Step 3:** Run analysis
```bash
python train_and_analyze.py
```

Results saved to `results.csv`

## Results

| Gene | Change | P-value |
|------|--------|---------|
| SOX2 | -85% | <10⁻³⁰⁰ |
| MYC  | -44% | <10⁻¹⁵ |
| SNCA | -38% | <10⁻¹⁸ |
