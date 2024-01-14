import os
import json
from octo.github_handle.mindsdb_octo import Mindsdb_Github


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
            self.repo = repo
            self.owner = owner
            self.branch = branch
            self.repo_initialized = True
            message = self.create_model(
                self.owner, self.repo, self.branch, all_files=all_files
            )
            self._save_state()
        elif (
            self.repo.lower() == repo
            and self.owner.lower() == owner
            and self.branch.lower() == branch
        ):
            message = f"[bold][blue]Repository already initialized."
            self.repo_initialized = True
        else:
            self.repo = repo
            self.owner = owner
            self.branch = branch
            self.repo_initialized = True
            message = self.create_model(
                self.owner, self.repo, self.branch, all_files=all_files
            )
            self._save_state()
        return message

    def checkout(self, owner, repo):
        self.owner = owner
        self.repo = repo
        model_names = [i.name for i in self._get_project().list_models()]
        if f"{owner}_{repo}" not in model_names:
            return f"[bold][red]Error: Repository not initialized. Use 'octo init' to initialize."
        else:
            self.status()
            self._save_state()
            return f"[bold][green]Switched to repo '{owner}/{repo}'."

    def status(self):
        return f"[bold][green]On branch {self.branch}\n[bold][blue]Repository: {self.owner}/{self.repo}"

    def list_models(self):
        model_names = [i.name for i in self._get_project().list_models()]
        return model_names

    def tell(self, df):
        pred = self.predict(df, self.owner, self.repo)
        return pred

    def drop(self, owner, repo):
        project = self._get_project()
        model_names = [i.name for i in project.list_models()]
        if f"{owner}_{repo}" not in model_names:
            return f"[bold][red]Error: Model {owner}/{repo} does not exist"
        else:
            project.drop_model(f"{owner}_{repo}")
            return f"[bold][green]Deleted model {owner}/{repo}"

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

