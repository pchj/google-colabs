import nbformat
from nbconvert import PythonExporter
import sys

# Function to analyze Jupyter Notebooks
def analyze_notebooks(notebook_files):
    for notebook_path in notebook_files:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        exporter = PythonExporter()
        code, _ = exporter.from_notebook_node(nb)
        # Perform analysis on the notebook code or extract relevant information
        print(f"Analysis for notebook: {notebook_path}")
        print(code)  # Example: Print Python code extracted from the notebook
        print("\n")

# Main function
if __name__ == "__main__":
    notebook_files = sys.argv[1:]  # Get list of notebook file paths from command line arguments
    analyze_notebooks(notebook_files)
import nbformat
from nbconvert import PythonExporter
import glob

# Function to analyze a Jupyter Notebook
def analyze_notebooks():
    notebook_files = glob.glob("*.ipynb")  # Find all notebook files in the current directory
    notebook_files = [file for file in notebook_files if file != "output.ipynb"]  # Exclude output.ipynb
    for notebook_path in notebook_files:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        exporter = PythonExporter()
        code, _ = exporter.from_notebook_node(nb)
        # Perform analysis on the notebook code or extract relevant information
        print(f"Analysis for notebook: {notebook_path}")
        print(code)  # Example: Print Python code extracted from the notebook
        print("\n")

# Example usage
if __name__ == "__main__":
    analyze_notebooks()
