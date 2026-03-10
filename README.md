# Semantic Drift Before Inference: A Preprocessing Attack Surface in Vision-Language Models

This repository provides a fully reproducible research codebase for the paper **"Semantic Drift Before Inference: A Preprocessing Attack Surface in Vision–Language Models"**.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo/semantic-drift-vlm/blob/main/notebooks/demo_attack.ipynb)
![Reproducibility](https://img.shields.io/badge/Reproducibility-100%25-brightgreen)

## Paper Summary

Vision-Language Models (VLMs) process input images through various preprocessing pipelines before inference. This repository demonstrates a newly discovered attack surface, where an adversary exploits the standard RGBA to RGB flattening process. 

By strategically embedding low-opacity hidden text into the alpha channel of an RGBA image, an adversary can ensure the text remains **invisible to a human observer** (rendered over a standard light background), but **visible to the VLM** during preprocessing (flattened natively against dark backgrounds). This creates a critical mismatch between what the user sees and what the model perceives, defined as **Semantic Drift**.

## Attack Details (Conditional Semantic Drift)

The Conditional Semantic Drift Attack implemented here:
1. Generates a base canvas.
2. Embeds text (e.g., `"IGNORE ALL RULES"`) at varying low opacities ($\alpha \in \{1, 2, 5, 10\}$).
3. Simulates the VLM preprocessing step where the alpha channel is dropped by compositing the image onto a solid background (Black, Grey, or White).
4. Demonstrates that on Black/Grey backgrounds, the text appears and induces misbehavior, while on White backgrounds, it remains hidden.

## Defense Pipeline: Semantic Equivalence Verification (SEV)

We implement **SEV**, a defense mechanism to detect Semantic Drift:
1. Extract text from the human-visible (User) image $I_u$ using OCR.
2. Extract text from the preprocessed (Model) image $I_m$ using OCR.
3. Compare the semantic lengths. If the preprocessed image contains significantly more text than the user image (length difference > threshold), the system flags the image as adversarial and halts API completion.

---

## 🚀 Installation & Setup

We recommend using `conda` or standard `pip` environments.

```bash
# Clone the repository
git clone https://github.com/your-username/semantic-drift-vlm.git
cd semantic-drift-vlm

# Install via Conda (Recommended)
conda env create -f environment.yml
conda activate semantic-drift-vlm

# OR Install via pip
pip install -r requirements.txt
```

*Note: You must have `tesseract-ocr` installed on your system to run the SEV defense loop.*
- **Ubuntu/Debian:** `sudo apt-get install tesseract-ocr`
- **MacOS:** `brew install tesseract`

---

## 🧪 Experiment Reproduction

To fully reproduce the experiments from the paper and generate the validation metrics (SDR, DR, FPR):

### One-Click Runner
```bash
./experiments/run_all.sh
```

### Manual Execution
If you prefer running the pipeline step-by-step:
```bash
python scripts/run_pipeline.py --config experiments/config.yaml
```

### Expected Results

The pipeline automatically outputs metrics to `results/tables/results.csv` and visual figures to `results/figures/drift_plot.png`.

**SDR Table (From the paper):**

| Background | $\alpha=1$ | $\alpha=2$ | $\alpha=5$ | $\alpha=10$ |
|------------|------------|------------|------------|-------------|
| **Black**  | 1.0        | 1.0        | 1.0        | 1.0         |
| **Grey**   | 1.0        | 1.0        | 1.0        | 1.0         |
| **White**  | 0.0        | 0.0        | 0.0        | 0.0         |

Both **Detection Rate (DR)** and **False Positive Rate (FPR)** will evaluate perfectly to `1.0` and `0.0` respectively, matching the experimental results cited.

---

## 🎨 Visual Examples and Notebooks

You can find Jupyter Notebooks to explore the visual intuition behind Semantic Drift.

- **`notebooks/demo_attack.ipynb`**: Interactive notebook walking step-by-step through generation and OCR extraction.
- **`notebooks/visualization.ipynb`**: Analyzes structural differences generating pixel-level heatmaps between the User and Model views.

### Drift Visualization
Below is an example showing the generated Difference Heatmap between what the User perceives vs the Flattened Preprocessed view:

![Difference Heatmap](examples/difference_heatmap.png)

---

## 📚 Future Work / Extended Preprocessing

While the primary attack focuses on the RGBA to RGB flattening vulnerability, researchers can expand this test surface using our pipeline to evaluate VLM resilience to:
- JPEG Compression Artifacts
- Gamma Correction
- Interpolation and Resizing
- Color Normalization Drifts

## Citation

If you use this codebase or find our research helpful, please cite our paper:
```bibtex
@article{semanticdrift2026,
  title={Semantic Drift Before Inference: A Preprocessing Attack Surface in Vision–Language Models},
  author={Author, A.},
  journal={ArXiv pre-print},
  year={2026}
}
```
