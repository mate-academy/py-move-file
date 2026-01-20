import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv" and len(command) == 3:
        try:
            mv, file1_name, destination = command
            if destination.endswith("/"):
                raise ValueError("Enter correct path and file name!")
            dirs = destination.split("/")[:-1]
            file2_name = destination.split("/")[-1]
            if os.path.exists(destination):
                raise FileExistsError(f"File {file2_name} already exists.")

            dir_path = ""
            for folder in dirs:
                dir_path = os.path.join(dir_path, folder)
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

            dir_path = os.path.join(dir_path, file2_name)
            with open(file1_name, "r") as source, open(dir_path, "w") as clone:
                clone.write(source.read())
            os.remove(file1_name)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
