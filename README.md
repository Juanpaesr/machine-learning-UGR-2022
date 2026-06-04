# Machine Learning — Portfolio (UGR)

Jupyter notebooks from the **Machine Learning** course (University of Granada, 2022–23).  
Author: **Juan Pablo Escudero Ramírez**

This repository covers foundational Python/NumPy work, iterative optimization and linear regression on digit features, hypothesis complexity and linear classifiers (PLA, pocket, logistic regression), and scikit-learn model tuning on a real-world regression dataset.

Each notebook includes custom implementations, documented decisions in markdown, and embedded outputs (plots and metrics).

## Projects

### [P0.ipynb](P0.ipynb) — Python, Matplotlib and NumPy

Introductory exercises with scikit-learn toy datasets: Iris, Breast Cancer, and Wine. Data loading, scatter plots, histograms, and basic NumPy operations.

### [P1.ipynb](P1.ipynb) — Iterative Optimization and Linear Regression

Gradient descent on synthetic and digit-derived features, pseudoinverse regression, SGD, and perceptron-based classification (digits 1 vs 5). Includes error analysis and decision boundary visualization.

### [P2.ipynb](P2.ipynb) — Hypothesis Complexity and Linear Models

VC dimension experiments with noise, linear classification with PLA, pocket algorithm, and logistic regression with stochastic gradient descent. Comparison of training and test errors with generalization bounds.

### [P3.ipynb](P3.ipynb) — Linear Model Tuning (Regression)

Exploratory analysis and linear regression on the **Online News Popularity** dataset. Ridge and Lasso regularization, cross-validation, and hyperparameter search with scikit-learn.

## Notebooks at a glance

| File | Summary |
|------|---------|
| [P0.ipynb](P0.ipynb) | NumPy, Matplotlib, sklearn toy datasets |
| [P1.ipynb](P1.ipynb) | Gradient descent, pseudoinverse, PLA, digit features |
| [P2.ipynb](P2.ipynb) | VC dimension, PLA, pocket, logistic regression |
| [P3.ipynb](P3.ipynb) | Ridge/Lasso tuning on Online News Popularity |

Helper module: [paths.py](paths.py).

## Requirements

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python build_data.py        # digit .npy files in data/
python download_data.py     # OnlineNewsPopularity.csv (~24 MB)
```

## How to run

1. Clone the repository.
2. Install dependencies and generate digit feature files (`build_data.py`).
3. Open any notebook in Jupyter Lab, VS Code/Cursor, or Google Colab.
4. Data files live in [`data/`](data/). The `paths.py` module detects the project root and resolves paths via `get_data()`.

```python
from paths import ROOT, get_data
import pandas as pd

df = pd.read_csv(get_data("OnlineNewsPopularity.csv"))
```

## Structure

```
AA/
├── P0.ipynb … P3.ipynb
├── paths.py
├── build_data.py
├── data/
│   ├── X_train.npy, y_train.npy, X_test.npy, y_test.npy
│   └── OnlineNewsPopularity.csv
├── requirements.txt
└── README.md
```

## Notes

- Notebooks keep **outputs** (plots and results) for visualization on GitHub.
- Unimplemented bonus sections (Newton's method in P1, digit classification bonus in P2) were removed.
- Digit features in `data/*.npy` are regenerated from MNIST via `build_data.py` (intensity + symmetry); results may differ slightly from the original Colab run.
- `OnlineNewsPopularity.csv` is from the [UCI repository](https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity).

## Topics

`machine-learning` · `numpy` · `matplotlib` · `scikit-learn` · `gradient-descent` · `linear-regression` · `perceptron` · `logistic-regression` · `vc-dimension` · `ridge` · `lasso` · `python` · `jupyter` · `ugr`

## License

Academic material for portfolio purposes. Do not submit as coursework without adaptation.
