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
    #     'mindsdb_llama_index>=23.12.4.2',
    #     'mindsdb_sdk==2.0.0',
    #     'openai==1.6.1',
    #     'llama_index==0.9.27',
    #     'llama_hub==0.0.67',
    #],
    #dependency_links=["https://github.com/pranavvp16/mindsdb.git@llama_index#egg=mindsdb_llama_index-23.12.4.2"]
)