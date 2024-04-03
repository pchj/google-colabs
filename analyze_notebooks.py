import nbformat
from nbconvert import PythonExporter

# Function to analyze a Jupyter Notebook
def analyze_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    code, _ = exporter.from_notebook_node(nb)
    # Perform analysis on the notebook code or extract relevant information
    print(code)  # Example: Print Python code extracted from the notebook

# Example usage
if __name__ == "__main__":
    analyze_notebook("GDC_Parameters.ipynb")  # Replace with your notebook path
