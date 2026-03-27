import os
import shutil
from os import makedirs
from os.path import isfile, join


def move_file(command) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "mv":
        return

    source_filename, target_filename = split_command[1], split_command[2]

    source_filename = os.path.abspath(source_filename)
    target_filename = os.path.abspath(target_filename)

    if not os.path.exists(source_filename):
        return

    if isfile(target_filename):
        shutil.move(source_filename, target_filename)
        return

    target_dirname = os.path.dirname(target_filename)

    if target_dirname and not os.path.exists(target_dirname):
        makedirs(join(target_dirname), exist_ok=True)

    shutil.move(source_filename, target_filename)
