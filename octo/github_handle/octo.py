import argparse
import os
import json

class Octo:
    def __init__(self):
        self.repo_initialized = False
        self.owner = None
        self.repo = None
        self.branch = "master"

    def init(self, repo, owner, branch):
        if not os.path.exists(".octo"):
            os.makedirs(".octo")
            print("Initialized empty repository.")
            self.repo = repo
            self.owner = owner
            if branch:
                self.branch = branch
            self.repo_initialized = True
            self._save_state()
        elif self.repo == repo and self.owner == owner and self.branch == branch:
            print("Repository already initialized.")
            self.repo_initialized = True
        else:
            self.repo = repo
            self.owner = owner
            self.branch = branch
            self.repo_initialized = True
            self._save_state()

    def checkout(self, repo, owner, branch):
        self.owner = owner
        self.branch = branch
        self.repo = repo
        self._save_state()
        if not self.repo_initialized:
            print("Error: Repository not initialized. Use 'octo init' to initialize.")
            return

        self.repo = repo
        print(f"Switched to repo '{repo}'.")
        self.status()

    def status(self):
        print(f"On branch {self.branch}")
        print(f"Owner: {self.owner}")
        print(f"Repo: {self.repo}")

    def _save_state(self):
        state = {
            "repo": self.repo,
            "owner": self.owner,
            "branch": self.branch,
        }
        with open(".octo/state.json", "w") as f:
            json.dump(state, f)

    def _load_state(self):
        if os.path.exists(".octo/state.json"):
            with open(".octo/state.json", "r") as f:
                state = json.load(f)
            self.repo = state["repo"]
            self.owner = state["owner"]

