# Colabs

## Overview
This repository contains a GitHub Actions workflow that automates the analysis of Jupyter Notebook files using Python scripts.

## Projects:
- Model-Earth:
  - Air
    - DCID data pipelines

## Workflow Steps
1. **Build Job**:
    - This job checks out the repository and runs a multi-line script to perform other actions such as testing and deployment.

2. **Analyze Notebooks Job**:
    - This job analyzes Jupyter Notebook files.
    - It checks out the repository.
    - Sets up Python environment with the required version.
    - Installs dependencies necessary for analysis (e.g., aiohttp, pandas, plotly, dash).
    - Runs the Python script (`analyze_notebooks.py`) to analyze the notebooks.

## Workflow Trigger
- The workflow is triggered on push or pull request events targeting the "main" branch.
- It can also be run manually from the Actions tab.
