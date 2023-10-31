from collections import defaultdict

def tree():
    return defaultdict(tree)

def add(t, paths):
    for path in paths:
        t = t[path]

def print_tree(t, indent="", prefix="", file=None):
    first = True
    for k, v in t.items():
        if first:
            print(indent + prefix + k, file=file)
            first = False
        else:
            print(indent + "|-- " + k, file=file)
        if isinstance(v, dict):
            print_tree(v, indent + "|   ", "|-- ", file=file)

def visualize_urls_in_tree(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    t = tree()
    for line in lines:
        line = line.strip().replace("https://", "").replace("http://", "")
        paths = line.split("/")
        add(t, paths)

    with open("output.txt", "w") as out:
        print_tree(t, file=out)

if __name__ == "__main__":
    visualize_urls_in_tree("urls.txt")
