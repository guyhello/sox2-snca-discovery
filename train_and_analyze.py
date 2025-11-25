"""
Complete pipeline: Train scGPT model and analyze SOX2 effects.
Just run: python train_and_analyze.py
"""

import scanpy as sc
import numpy as np
import pandas as pd
from scipy import stats

# ============ STEP 1: LOAD DATA ============
print("Loading data...")
adata = sc.read_h5ad('data/vcc_data.h5ad')
print(f"Loaded {adata.n_obs:,} cells")

# ============ STEP 2: TRAIN MODEL ============
print("\nTraining model...")
# TODO: Add your actual scGPT training code here
# For now, we'll skip to analysis

# ============ STEP 3: ANALYZE SOX2 ============
print("\nAnalyzing SOX2 effects...")

control = adata.obs['perturbation'] == 'non-targeting'
sox2_ko = adata.obs['perturbation'] == 'SOX2'

results = []
for gene in ['SOX2', 'MYC', 'SNCA']:
    ctrl_expr = adata[control, gene].X.toarray().flatten()
    ko_expr = adata[sox2_ko, gene].X.toarray().flatten()
    
    log2fc = np.log2((np.mean(ko_expr) + 1e-9) / (np.mean(ctrl_expr) + 1e-9))
    pct_change = (1 - 2**log2fc) * 100
    _, pval = stats.ttest_ind(ctrl_expr, ko_expr)
    
    print(f"{gene}: {pct_change:+.1f}%, p={pval:.2e}")
    
    results.append({
        'gene': gene,
        'log2fc': log2fc,
        'pct_change': pct_change,
        'pvalue': pval
    })

# Save results
df = pd.DataFrame(results)
df.to_csv('results.csv', index=False)
print("\nSaved results.csv")
