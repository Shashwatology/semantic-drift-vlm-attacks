#!/usr/bin/env bash
# run_all.sh
# End-to-end experiment reproducer

echo "========================================================="
echo " Reproducing Paper: Semantic Drift Before Inference"
echo "========================================================="

# Ensure we're running from the root of the repository
cd "$(dirname "$0")/.."

# Provide execution access
chmod +x scripts/run_pipeline.py

# Run the python pipeline
python scripts/run_pipeline.py --config experiments/config.yaml

echo "========================================================="
echo " Done! Check results/tables/results.csv and results/figures/drift_plot.png"
echo "========================================================="
