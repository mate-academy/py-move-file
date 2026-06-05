import os
import shutil


def move_file(command: str) -> None:
    command_line = command.split(" ")
    if len(command_line) == 3:
        source = command_line[1]
        dest = command_line[2]

        if command_line[0] == "mv":
            filename = os.path.basename(source)

            if dest.endswith("/") or os.path.isdir(dest):
                final_dest = os.path.join(dest, filename)
            else:
                final_dest = dest

            parent_dir = os.path.dirname(final_dest)

            if (parent_dir
                    and not os.path.isdir(parent_dir)
                    and not os.path.isfile(parent_dir)):
                parts = parent_dir.split(os.sep)
                for i in range(len(parts)):
                    path = os.sep.join(parts[:i + 1])
                    if not os.path.exists(path):
                        os.mkdir(path)

            if os.path.exists(final_dest):
                os.remove(final_dest)

            shutil.copy(source, final_dest)
            os.remove(source)
