from setuptools import setup, find_packages

setup(
    name="octo",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "octo = octo.cli:main",
        ],
    },
    # install_requires=[
    #     'rich',
    #     'mindsdb_sdk',
    #     'openai',
    #     'mindsdb'
    # ],
    # dependency_links=["https://github.com/pranavvp16/mindsdb.git@llama_index#egg=mindsdb-llama_index"]
)