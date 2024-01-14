# Octo: AI-Powered Git Companion
<img src="media/logo-no-background.png">
Octo seamlessly blends the power of artificial intelligence with the familiarity of Git, empowering you to interact with your repositories in a whole new way. Whether you're a seasoned developer or just getting started with Git, Octo offers innovative features to streamline your workflow and enhance your productivity.



## Installation
Create a virtual environment with python venv or conda

Install octo with pip

```bash
  pip install -r requirements.txt
```
```bash 
  pip install .
```
This will successfully install octo package.


**Environment variables**

Firstly you need to have `OPENAI_API_KEY` and `GITHUB_TOKEN` and set the environment variables `OPENIAI_API_KEY` and `GITHUB_TOKEN` respectively.

```bash
$ echo "export OPENAI_API_KEY=<KEY>" >> ~/.bashrc
```
```bash 
$ echo "export GITHUB_TOKEN=<TOKEN>" >> ~/.bashrc
```

## Demo

**Commands**

For each command to work *octo* is prefix.

- --help: Information about usage of octo
- --version: to display the version of octo
- start: To establish a connection with MindsDB server
- init: Initialize a repo
- status: to check the status of octo
- tell: Asking question realted to the repo
- checkout: To change the working repo 
- drop: To remove a model 
- list: To display all the models present 
- stop: to disconnect the MindsDB server 



## Run Locally

Clone the project

```bash
  git clone https://github.com/pranavvp16/octo.git
```

Go to the project directory

```bash
  cd octo
```

Install dependencies

```bash
  pip install -r requirements.txt
```
```bash
  pip install git+https://github.com/pranavvp16/mindsdb.git@llama_index
```

```bash
  pip install .
```


**Start the Companion**

`start` command to start the mindsdb server locally
```bash
  octo start
```
`init` command to initialize the repo
```bash
  octo init <GitHubUsername>/<repo> <branch_name>
```
`status` command to check the status of the octo 
```bash
  octo status
```
`tell` command for asking questions about the repo 
```bash
  octo tell "<Your Question>"
```
`checkout` command to change the working repo
```bash
  octo checkout <GitHubUsername>/<repo>
```
`drop` command to remove a model
```bash
  octo drop <GitHubUsername>/<repo>
```
`list` command to display all the models initialized 
```bash
  octo list
```
`stop` command to terminate the mindsdb server
```bash
  octo stop 
```
## Tech Stack

Python

MindsDB





## Authors

- [Pranav Prajapati](https://github.com/pranavvp16)
- [Vedant Agrawal](https://github.com/vedantag17)



### License
octo is being licensed under the [MIT License](https://github.com/pranavvp16/octo/blob/master/LICENSE).

<img src="media/badge-dark.svg#gh-dark-mode-only" width=350 height=90>
<img src="media/badge-light.svg#gh-light-mode-only" width=350 height=90>
