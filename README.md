# yijia_ids706_miniProj9

## Python Template

This project demonstrates data manipulation and visualization in a cloud-hosted Jupyter Notebook (Google Colab), utilizing Python to perform basic data analysis and visualization tasks.

## CI/CD Badge

[![CI](https://github.com/nogibjj/yijia_ids706_miniProj9/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj9/actions/workflows/ci.yml)

## Colab URL 

You can access the notebook via Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nogibjj/yijia_ids706_miniProj9/blob/main/main.ipynb)

## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`lib.py`**: Contains utility functions like `load_dataset`, `calculate_statistics`, `create_histogram`, and `generate_visualizations`.
- **`test_lib.py`**: Contains tests for functions in `lib.py`.
- **`main.ipynb`**: Cloud-hosted Jupyter Notebook for data analysis and testing. 


## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj9.git
```

### 2. Open the Repository in CodeSpace

- Open the repository in GitHub Codespaces
- Wait for the container setup to complete to ensure a consistent environment.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Ruff.
- make test: Runs all tests in test_lib.py.


## CI/CD Setup
- Location: .github/workflows/
- Actions: Automatically runs setup, lint, format, and test actions, ensuring continuous integration and code quality.
