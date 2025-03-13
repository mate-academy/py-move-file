import os


def move_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3 and ls[0] == "mv":
        source_file = ls[1]
        destination_path = ls[2]

        if not os.path.exists(source_file):
            return

        try:
            if "/" not in destination_path:
                os.replace(source_file, destination_path)
            else:
                new_list = destination_path.split("/")
                file_name = new_list[-1]
                directory_path = "/".join(new_list[:-1])

                if not os.path.exists(directory_path):
                    os.makedirs(directory_path)

                destination_file = os.path.join(directory_path, file_name)
                os.replace(source_file, destination_file)

        except Exception as e:
            print(f"An error occurred {e}")
