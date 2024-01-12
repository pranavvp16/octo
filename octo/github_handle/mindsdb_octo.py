import mindsdb_sdk
import subprocess
import os
import time

from octo.templates.query_dicts import using_dict, using_dict_all


class MindsdbOcto:
    """Mindsdb class to interact with Mindsdb SDK"""

    def __init__(self):
        """
        Authenicating Mindsdb SDK with email and password
        """
        self.connection_string = "http://127.0.0.1:47334"

    def connect_local(self):
        """
        Connect to local installation of mindsdb
        """
        # Run shell command to start the local mindsdb server
        subprocess.Popen(
            ["python", "-m", "mindsdb"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def create_model(self, owner, repo, branch, all_files=False):
        project = self._get_project()

        if not all_files:
            using_dict["owner"] = owner
            using_dict["repo"] = repo
            using_dict["branch"] = branch
            using_dict["openai_api_key"], using_dict["github_token"] = self._get_keys()
            model = project.create_model(
                name=f"{owner}_{repo}".lower(),
                engine="llama_index",
                predict="answer",
                options=using_dict,
            )
        else:
            using_dict_all["owner"] = owner
            using_dict_all["repo"] = repo
            using_dict_all["branch"] = branch
            (
                using_dict_all["openai_api_key"],
                using_dict_all["github_token"],
            ) = self._get_keys()
            model = project.create_model(
                name=f"{owner}_{repo}".lower(),
                engine="llama_index",
                predict="answer",
                options=using_dict_all,
            )
        while True:
            if model.get_status() not in ("generating", "training"):
                print("\nFinished adding repository to knowledge base")
                break

        if model.get_status() == "error":
            return f"[bold][red]{model.data['error']}"

        return f"[bold][green]Model created successfully"

    def predict(self, df, owner, repo):
        project = self._get_project()
        model = project.get_model(f"{owner}_{repo}".lower())
        return model.predict(df)

    def _get_keys(self):
        """
        Get keys before model creation
        """
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        github_token = os.environ.get("GITHUB_TOKEN")

        if not openai_api_key or not github_token:
            raise Exception(
                "Please set OPENAI_API_KEY and GITHUB_TOKEN environment variables"
            )

        return openai_api_key, github_token

    def _get_project(self):
        server = mindsdb_sdk.connect(self.connection_string)
        project = server.get_project()
        return project
