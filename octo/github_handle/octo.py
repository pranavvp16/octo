import os
import json
from octo.github_handle.mindsdb_github import Mindsdb_Github


class Octo(Mindsdb_Github):
    def __init__(self):
        super().__init__()
        self.repo_initialized = False
        self.owner = None
        self.repo = None
        self.branch = "master"

    def init(self, repo, owner, branch, all_files=False):
        if not os.path.exists(".octo"):
            os.makedirs(".octo")
            print("Initialized empty repository.")
            self.repo = repo
            self.owner = owner
            if branch:
                self.branch = branch
            self.repo_initialized = True
            self.create_model(self.owner, self.repo, self.branch, all_files=all_files)
            self._save_state()
        elif self.repo == repo and self.owner == owner and self.branch == branch:
            print("Repository already initialized.")
            self.repo_initialized = True
        else:
            self.repo = repo
            self.owner = owner
            self.branch = branch
            self.repo_initialized = True
            self.create_model(self.owner, self.repo, self.branch, all_files=all_files)
            self._save_state()

    def checkout(self, repo, owner):
        self.owner = owner
        self.repo = repo
        model_names = [i.name for i in self._get_project().list_models()]
        if f"{owner}_{repo}" not in model_names:
            print("Error: Repository not initialized. Use 'octo init' to initialize.")
        else:
            print(f"Switched to repo '{owner}/{repo}'.")
            self.status()
            self._save_state()

    def status(self):
        print(f"On branch {self.branch}")
        print(f"Owner: {self.owner}")
        print(f"Repo: {self.repo}")

    def tell(self, df):
        pred = self.predict(df, self.owner, self.repo)
        return pred

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
            self.branch = state["branch"]
