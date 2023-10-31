

This script visualizes a list of URLs in a tree-like structure.

## 📜 Description

Given a text file (`urls.txt`) containing URLs, this script will visualize the hierarchical structure of the URLs in a tree format and save it in an output file (`output.txt`).

## 📌 Features

- Removes `https://` and `http://` prefixes from URLs.
- Represents URL path segments as tree nodes.
- Outputs the visual tree to `output.txt`.

## 🚀 Usage

1. Place your URLs in a file named `urls.txt`.
2. Run the script.
3. Check the `output.txt` file for the visualized tree of URLs.

## 📄 Script Overview

- The script uses `defaultdict` to create a recursive tree structure.
- The `tree()` function initializes the tree.
- The `add()` function populates the tree with URL paths.
- The `print_tree()` function is a recursive function to print the tree in a formatted manner.
- The `visualize_urls_in_tree()` function reads the `urls.txt` file, processes the URLs, and writes the tree visualization to `output.txt`.

## 📥 Input Format

The input file (`urls.txt`) should contain one URL per line. For example:


```
https://example.com/path1/path2 
https://example.com/path1/path3

```

## 📤 Output Example

The output (`output.txt`) for the above input will look something like:

```
example.com
|-- path1
|   |-- path2
|   |-- path3

```
## 📚 Dependencies

- Python's built-in libraries: `collections`

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests. Any feedback is welcome!