from octo import Octo
import argparse
import pandas as pd


def main():
    git = Octo()
    git._load_state()
    git.connect_local()

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

    args = parser.parse_args()

    if args.command == "init":
        owner = args.repo.split("/")[0]
        repo = args.repo.split("/")[1]
        git.init(repo, owner, args.branch, all_files=args.all)

    elif args.command == "checkout":
        owner = args.repo.split("/")[0]
        repo = args.repo.split("/")[1]
        git.checkout(owner, repo)

    elif args.command == "status":
        git.status()

    elif args.command == "tell":
        df = pd.DataFrame({"questions": [args.action]})
        pred_df = git.tell(df)
        print(pred_df["answer"])


if __name__ == "__main__":
    main()
