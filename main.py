import argparse
from utils import *
from datetime import datetime

tasks = load_tasks()

def main():
   # Create the parser
    parser = argparse.ArgumentParser(description="A simple CLI example")
    subparser = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparser.add_parser("add", help="Add new task")
    add_parser.add_argument("add", nargs="+",type=str, help="Insert a new task by using the command add 'task'")

    list_parser = subparser.add_parser("list", help="List all tasks")
    list_parser.add_argument("list", nargs="?", type=str, help="List all tasks")

    clear_parser = subparser.add_parser("clear", help="Clear all tasks")
    clear_parser.add_argument("clear", nargs="?", type=str, help="Clear all tasks")

    done_parser = subparser.add_parser("done", help="Update a task")
    done_parser.add_argument("done", nargs="?", type=int, help="Update a task")

    delete_parser = subparser.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("delete", nargs="?", type=int, help="Delete a task")

    args = parser.parse_args()

    if args.command == 'add':
        task_text = " ".join(args.add)
        tasks.append({ "task": task_text, "completed": False, "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S") })
        save_tasks(tasks)
        print(f"Task added: {task_text}")
    elif args.command == 'list':
        list_task()
    elif args.command == 'clear':
        clear_task()
        print("All tasks cleared.")
    elif args.command == "done":
        done_task(int(args.done))
    elif args.command == "delete":
        delete_task(int(args.delete))

if __name__ == "__main__":
    main()