from setuptools import setup, find_packages

setup(
    name="octo",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "octo = octo.check_cli:main",
        ],
    }
)