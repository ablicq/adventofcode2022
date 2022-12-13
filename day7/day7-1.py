class TreeNode:
    parent = None
    children = {}
    tag = -1


working_dir = TreeNode()


def handle_cd(d):
    if d == "..":
        working_dir = working_dir.parent
    else:
        working_dir = working_dir.children[d]


def handle_ls():
    pass


def handle_cmd(*args):
    if args[0] == "cd":
        handle_cd(args[1])
    elif args[0] == "ls":
        handle_ls()


def handle_file(*args):
    if args[0] == "dir":
        new_dir = TreeNode()
        new_dir.parent = working_dir
        working_dir.children[args[1]] = new_dir
