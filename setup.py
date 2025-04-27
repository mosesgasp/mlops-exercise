from setuptools import setup, find_packages

setup(
    name="mlops-exercise",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "joblib",
        "faker",
    ],
    python_requires=">=3.6",
) 