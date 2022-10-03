import os
import shutil


def move_file(command: str) -> None:
    try:
        source_path = command.split()[1]
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"No such file or directory:"
                                    f"'{source_path}'")
        destination_path = command.split()[2]
        if os.path.exists(destination_path):
            new_location = shutil.move(source_path, destination_path)
        else:
            destination_path_dir = '/'.join(destination_path.split("/")[0:-1])
            os.makedirs(destination_path_dir)
            new_location = shutil.move(
                source_path,
                destination_path_dir + "/" + destination_path.split("/")[-1]
            )
        print("The {0} is moved to the location, {1}".format(source_path,
                                                             new_location))
    except FileNotFoundError as e:
        print(e)
