 yijia_ids706_miniProj9

## Python Template
This project demonstrates data manipulation and visualization in a cloud-hosted Jupyter Notebook (Google Colab).




## CI/CD Badge

## Colab URL 
https://colab.research.google.com/gist/yijiaduke/fab68c0b21c4d4eb39e7a410d32d9cb6/assn9.ipynb#scrollTo=px46MPFP1obJ

## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`lib.py`**: Contains utility functions like `load_dataset`, `calculate_statistics`,`create_histogram`, and `generate_visualizations`.
- **`test_lib.py`**: Contains tests for functions in `lib.py`.
- **`mini9.ipynb`**: Cloud-hosted Jupyter Notebook for data analysis and testing. 


## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj2.git
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
