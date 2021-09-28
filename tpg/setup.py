from setuptools import setup, find_packages

# Classifiers: https://pypi.org/classifiers/

with open("README.md", "r") as readme:
    long_desc = readme.read()

setup(
    name="tpg",
    version="0.1.0",
    description="Library for two player games with evolutionary game theory",
    url="https://github.com/HammerAPI/TwoPlayerGames",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author=[
        "Daniel Hammer",
        "Nicholas O'Kelley",
        "Andrew Penland",
        "Andrew Shelton"
    ],
    author_email=[
        "hammerapi@gmail.com",
        "okelleynp@gmail.com",
        "ashelt822@gmail.com"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["python", "evolution", "evolutionary game theory", "two player games", "game theory"],
    packages=find_packages()
)
