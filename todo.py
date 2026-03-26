#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from datetime import datetime

TASKS_FILE = Path("tasks.json")


def load_tasks():
    """タスク一覧を読み込む"""
    if TASKS_FILE.exists():
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """タスク一覧を保存"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(title):
    """タスクを追加"""
    tasks = load_tasks()
    task_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({
        "id": task_id,
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat()
    })
    save_tasks(tasks)
    print(f"✓ タスクを追加しました (ID: {task_id})")


def complete_task(task_id):
    """タスクを完了マーク"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✓ タスク '{task['title']}' を完了しました")
            return
    print(f"✗ ID {task_id} のタスクが見つかりません")


def list_tasks():
    """タスク一覧を表示"""
    tasks = load_tasks()
    if not tasks:
        print("タスクはありません")
        return

    print("\n【タスク一覧】")
    for task in tasks:
        status = "✓" if task["completed"] else "☐"
        print(f"{status} [{task['id']}] {task['title']}")
    print()


def main():
    if len(sys.argv) < 2:
        print("使い方:")
        print("  python todo.py add <タスク名>     - タスクを追加")
        print("  python todo.py complete <ID>      - タスクを完了")
        print("  python todo.py list                - タスク一覧表示")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("エラー: タスク名を指定してください")
            sys.exit(1)
        add_task(" ".join(sys.argv[2:]))
    elif command == "complete":
        if len(sys.argv) < 3:
            print("エラー: タスクIDを指定してください")
            sys.exit(1)
        complete_task(int(sys.argv[2]))
    elif command == "list":
        list_tasks()
    else:
        print(f"エラー: 不明なコマンド '{command}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
