from octo import Octo
from rich.console import Console
from rich import print as rprint
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Simple Git-like CLI tool")
subparsers = parser.add_subparsers(dest="command", help="Subcommands")

# Command: init
parser_init = subparsers.add_parser("init", help="Initialize a new repository")
parser_init.add_argument("repo", help="Repository name")
parser_init.add_argument("branch", help="Repository owner")
parser_init.add_argument("--all", help="Repository branch", action="store_true")

# Command: checkout
parser_checkout = subparsers.add_parser(
    "checkout", help="Switch to a different branch"
)
parser_checkout.add_argument("repo", help="Branch to checkout")

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

    git = Octo()
    git._load_state()
    git.connect_local()

    args = parser.parse_args()

    if args.command == "init":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            rprint("[bold][red]Error: Invalid repository name, format should be 'owner/repo'")
            return
        with console.status("[bold green]Initializing repository...", spinner="dots2"):
            rprint(f"[bold][blue] Starting Mindsdb local server")
            rprint(f"[bold][green] Creating model {owner}/{repo}")
            message = git.init(repo, owner, args.branch, all_files=args.all)
            rprint(message)

    elif args.command == "checkout":
        try:
            owner = args.repo.split("/")[0]
            repo = args.repo.split("/")[1]
        except:
            rprint("[bold][red]Error: Invalid repository name, format should be 'owner/repo'")
            return
        message = git.checkout(owner, repo)
        console.log(message)

    elif args.command == "status":
        message = git.status()
        console.log(message)

    elif args.command == "tell":
        df = pd.DataFrame({"questions": [args.action]})
        with console.status("[bold green]Octo is typing...", spinner="dots2"):
            pred_df = git.tell(df)
            answer = pred_df["answer"].iloc[0]
            # Filter string
            answer = answer.replace("\n", "")
            rprint(answer)

    elif args.command == "list":
        model_names = git.list_models()
        # Format the string
        model_names = [i.replace("_","/") for i in model_names]
        with console.status("[bold green]Fetching models...", spinner="dots2"):
            for i in model_names:
                rprint(i)



if __name__ == "__main__":
    main()
