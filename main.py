import argparse
from scheduler import Scheduler
from alarm_manager import AlarmManager

def build_parser():
    parser = argparse.ArgumentParser(
        prog="alarm",
        description="CLI Alarm Clock"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new alarm"
    )

    add_parser.add_argument(
        "--datetime",
        required=True,
        help=(
            "ISO datetime "
            "(YYYY-MM-DDTHH:MM:SS)"
        ),
    )

    add_parser.add_argument(
        "--recurring",
        action="store_true",
        help="Repeat daily",
    )

    add_parser.add_argument(
        "--label",
        default="Alarm",
        help="Alarm label"
    )

    list_parser = subparsers.add_parser(
        "list",
        help="List alarms"
    )

    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove alarm"
    )

    remove_parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Alarm ID"
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Start scheduler"
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    manager = AlarmManager()

    if args.command == "add":
        manager.add_alarm(
            trigger_at=args.datetime,
            label=args.label,
            recurring=args.recurring,
        )

    elif args.command == "list":
        manager.list_alarms()

    elif args.command == "remove":
        manager.remove_alarm(args.id)

    elif args.command == "run":
        Scheduler(manager).run()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
