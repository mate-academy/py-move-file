# write your code here
import os


def move_file(command: str) -> None:
    blocks = command.split()
    if len(blocks) > 2 and blocks[0] == "mv":
        current_file_name = blocks[1]
        new_file_name = blocks[2]

        if "/" in new_file_name:

            new_file_blocks = new_file_name.split("/")

            if not os.path.isdir("/".join(new_file_blocks[:-1])):
                os.makedirs("/".join(new_file_blocks[:-1]))

        os.rename(current_file_name, new_file_name)
