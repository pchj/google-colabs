import nbformat
from nbconvert import PythonExporter
import glob

# Function to analyze a Jupyter Notebook
def analyze_notebooks():
    notebook_files = glob.glob("*.ipynb")  # Find all notebook files in the current directory
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
