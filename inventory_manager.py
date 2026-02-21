import json


new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}


def read_inventory(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_inventory(path, inventory):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=4)


def print_inventory(inventory):
    for book in inventory:
        print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")


def main():
    path = "inventory.json"

    # Task 1 — Read the inventory and print count
    inventory = read_inventory(path)
    print(len(inventory))

    # Task 2 — Append new_book and save with indent=4
    inventory.append(new_book)
    write_inventory(path, inventory)

    # Task 3 — Read updated file and display formatted inventory
    updated = read_inventory(path)
    print_inventory(updated)


if __name__ == "__main__":
    main()
