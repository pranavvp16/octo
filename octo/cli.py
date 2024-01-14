from octo import Octo
from octo import ASCII_ART
from octo import __version__

from rich.console import Console
from rich import print as rprint
from rich.text import Text

import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="QA any Github repository")
subparsers = parser.add_subparsers(dest="command", help="Subcommands")

# Command: version
parser.add_argument("--version", action="store_true", help="Show version number")

# Command: Start Mindsdb server
parser_start = subparsers.add_parser("start", help="Start the Mindsdb server")
parser_stop = subparsers.add_parser("stop", help="Stop the Mindsdb server")

# Command: init
parser_init = subparsers.add_parser("init", help="Initialize a new repository")
parser_init.add_argument("repo", help="Repository name")
parser_init.add_argument("branch", help="Repository owner")
parser_init.add_argument("--all", help="Repository branch", action="store_true")

# Command: drop
parser_drop = subparsers.add_parser("drop", help="Drop a repository")
parser_drop.add_argument("repo", help="Repository name")

# Command: checkout
parser_checkout = subparsers.add_parser("checkout", help="Switch to a different repo")
parser_checkout.add_argument("repo", help="Repository to checkout")

# Command: tell
parser_tell = subparsers.add_parser("tell", help="Tell Octo to do something")
parser_tell.add_argument("action", help="Action to perform")

# Command: status
parser_status = subparsers.add_parser(
    "status", help="Show the status of the repository"
)

parser_list = subparsers.add_parser(
    "list", help="List all the models in the repository"
)


def main():
    console = Console()

    octo = Octo()
    octo._load_state()
    args = parser.parse_args()

    try:
        octo._get_project()
    except:
        if args.command == "start":
            with console.status("[bold green]Starting Mindsdb...", spinner="dots2"):
                    octo.start_local()
                    console.print(f"[bold][green]Started Mindsdb local server")
        else:
            console.print(
                "[bold][red]Error: Mindsdb server is not running. Use 'octo start' to start the server."
            )
            return

    if args.command == "stop":
        octo.stop_local()
        console.print(f"[bold][green]Stopped Mindsdb local server")

    if args.command == "init":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            console.print(
                "[bold][red]Error: Invalid repository name, format should be 'owner/repo'"
            )
            return
        with console.status("[bold green]Initializing repository...", spinner="dots2"):
            console.print(f"[bold][green] Creating model {owner}/{repo}")
            message = octo.init(repo, owner, args.branch, all_files=args.all)
            console.print(message)

    if args.command == "drop":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            console.print(
                "[bold][red]Error: Invalid repository name, format should be 'owner/repo'"
            )
            return
        project = octo._get_project()
        model_names = [i.name for i in project.list_models()]
        if f"{owner}_{repo}" not in model_names:
            console.print(f"[bold][red]Error: Model {owner}/{repo} does not exist")
            return
        else:
            project.drop_model(f"{owner}_{repo}")
            console.print(f"[bold][green]Deleted model {owner}/{repo}")

    if args.version:
        text = ASCII_ART.format(__version__)
        console.print(Text(text))

    if args.command == "checkout":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            rprint(
                "[bold][red]Error: Invalid repository name, format should be 'owner/repo'"
            )
            return
        message = octo.checkout(owner, repo)
        console.print(message)

    if args.command == "status":
        message = octo.status()
        console.print(message)

    if args.command == "tell":
        df = pd.DataFrame({"questions": [args.action]})
        with console.status("[bold green]Octo is typing...", spinner="dots2"):
            pred_df = octo.tell(df)
            answer = pred_df["answer"].iloc[0]
            # Filter string
            answer = answer.replace("\n", "")
            console.print(f"\n{answer}")
            return

    if args.command == "drop":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            rprint(
                "[bold][red]Error: Invalid repository name, format should be 'owner/repo'"
            )
            return
        message = octo.drop(owner, repo)
        console.print(message)

    if args.command == "list":
        model_names = octo.list_models()
        # Format the string
        model_names = [i.replace("_", "/") for i in model_names]
        with console.status("[bold green]Fetching models...", spinner="dots2"):
            for i in model_names:
                console.print(i)



if __name__ == "__main__":
    main()
