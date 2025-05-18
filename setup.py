from setuptools import setup, find_packages

setup(
    name="forex-bot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "forex-bot=src.main:main",
        ],
    },
    python_requires=">=3.8",
)
