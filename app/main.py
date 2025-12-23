import os


def move_file(command):
    parts = command.split()
    src = parts[1]
    dest = parts[2]

    if dest.endswith('/'):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)

    if dest_dir:
        path_acc = ""
        for folder in dest_dir.split('/'):
            if not folder:
                continue
            path_acc = os.path.join(path_acc, folder)
            if not os.path.exists(path_acc):
                os.mkdir(path_acc)

    with open(src, 'r') as f_src:
        content = f_src.read()

    with open(dest, 'w') as f_dest:
        f_dest.write(content)

    os.remove(src)
