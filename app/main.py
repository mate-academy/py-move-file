import os


def move_file(command: str) -> None:
    command_listed = command.split(" ")
<<<<<<< HEAD

    source_file_path = command_listed[1]
    destination = command_listed[2]
=======
    source_file = command_listed[1]
>>>>>>> 7395f9834185424176f9d6c4eb622b99a0286f11

    if command_listed[0] != "mv" or len(command_listed) != 3:
        return

<<<<<<< HEAD
    destination_dir, destination_file_name = os.path.split(destination)

    if destination.endswith("/"):
        destination_dir = destination
        destination_file_name = os.path.basename(source_file_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    if source_file_path != destination:
        try:

            with open(source_file_path, "r") as source_file:
                content = source_file.read()

            with open(
                    os.path.join(destination_dir, destination_file_name), "w"
            ) as destination_file:
                destination_file.write(content)

            os.remove(source_file_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        os.rename(
            source_file_path,
            os.path.join(destination_dir, destination_file_name)
        )
=======
    file_path, file_name = os.path.split(command_listed[2])

    if file_path:
        os.makedirs(file_path, exist_ok=True)

    if source_file != command_listed[2]:

        with open(f"{source_file}", "r") as f:
            info = f.read()

        with open(os.path.join(file_path, file_name), "w") as nf:
            nf.write(info)

        os.remove(source_file)

    else:
        os.rename(source_file, file_name)
>>>>>>> 7395f9834185424176f9d6c4eb622b99a0286f11
