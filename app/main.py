import os


def move_file(command: str) -> None:
    split_list = command.split()
    if len(split_list) == 3 and split_list[0] == "mv":
        source_file = split_list[1]
        destination_path = split_list[2]

        if not os.path.exists(source_file):
            return

        try:
            if "/" not in destination_path:
                os.replace(source_file, destination_path)
                os.remove(source_file)
            else:
                new_list = destination_path.split("/")
                file_name = new_list[-1]
                directory_path = "/".join(new_list[:-1])

                if not os.path.exists(directory_path):
                    os.makedirs(directory_path, exist_ok=True)

                destination_file = os.path.join(directory_path, file_name)
                os.replace(source_file, destination_file)
                os.remove(source_file)

        except Exception as e:
            print(f"An error occurred {e}")
