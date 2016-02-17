# This is not purely the result of trial and error.

from setuptools import setup, find_packages

setup(
    name="git-commit-filter",
    version="0.1",
    packages=find_packages(),
    install_requires=['pygit2>=0.23.3'],
    entry_points={
        "console_scripts": [
            "git-commit-filter = commitfilter.__main__:main",
        ],
    },

    author="Dongyuan Liu",
    author_email="liu.dongyuan@gmail.com",
    description="Find interesting commits.",
    license="MIT",
    keywords="git commit filter line code",
    url="https://github.com/xhacker/git-commit-filter",
)
