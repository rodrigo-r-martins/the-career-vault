from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="career-agent",
    version="0.1.0",
    py_modules=["main"],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "career-agent=main:cli",
        ],
    },
)

