class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = {}
        self.size = 0
        self.is_dir = True


root = TreeNode()


def handle_cd(working_dir, d):
    if d == "..":
        return working_dir.parent
    elif d == "/":
        return root
    else:
        return working_dir.children[d]


def handle_ls(working_dir):
    return working_dir


def handle_cmd(working_dir, *args):
    if args[0] == "cd":
        return handle_cd(working_dir, args[1])
    elif args[0] == "ls":
        return handle_ls(working_dir)


def handle_file(working_dir, *args):
    if args[0] == "dir":
        new_dir = TreeNode()
        new_dir.parent = working_dir
        new_dir.is_dir = True
        working_dir.children[args[1]] = new_dir
    else:
        new_file = TreeNode()
        new_file.parent = working_dir
        new_file.size = int(args[0])
        new_file.is_dir = False
        working_dir.children[args[1]] = new_file
    return working_dir


def handle_line(working_dir, line):
    parts = line.split()
    if parts[0] == "$":
        return handle_cmd(working_dir, *parts[1:])
    else:
        return handle_file(working_dir, *parts)


def compute_sizes(node: TreeNode):
    total_size = 0
    for child in node.children.values():
        compute_sizes(child)
        total_size += child.size
    node.size += total_size


def compute_total_size(node: TreeNode, total_size):
    for child in node.children.values():
        total_size = compute_total_size(child, total_size)
    if node.is_dir and node.size <= 100000:
        total_size += node.size
    return total_size


working_dir = root
with open("day7/input.txt", "r") as file:
    for line in file:
        working_dir = handle_line(working_dir, line)

compute_sizes(root)
print(compute_total_size(root, 0))
