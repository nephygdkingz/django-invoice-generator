import os

IGNORE_FOLDERS = {'.git', 'venv', '__pycache__'}

def generate_tree(root_dir, prefix=""):
    entries = sorted(os.listdir(root_dir))
    entries = [e for e in entries if e not in IGNORE_FOLDERS]

    entries_count = len(entries)
    tree_lines = []

    for index, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        connector = "└── " if index == entries_count - 1 else "├── "

        if os.path.isdir(path):
            tree_lines.append(f"{prefix}{connector}{entry}/")
            extension = "    " if index == entries_count - 1 else "│   "
            tree_lines.extend(generate_tree(path, prefix + extension))
        else:
            tree_lines.append(f"{prefix}{connector}{entry}")
    return tree_lines

def save_tree_to_file(root_dir=".", filename="tree_clean.txt"):
    tree_lines = [f"{os.path.basename(os.path.abspath(root_dir))}/"]
    tree_lines.extend(generate_tree(root_dir))
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))
    print(f"Folder structure saved to {filename}")

if __name__ == "__main__":
    save_tree_to_file(root_dir=".")
