import os


def move_file(command: str) -> None:
    command = [command for command in command.split(" ")]
    action = command[0]
    source_file_option = command[1]
    target_file_option = command[2]
    target_type = None
    target_folders_path = None
    if "/" in target_file_option:
        target_folders_path = target_file_option.rsplit("/", 1)[0]
        target_type = "folder"
    if "/" not in target_file_option:
        target_folders_path = target_file_option
        target_type = "file"

    try:
        path_exist = os.path.exists(target_folders_path)
        if action == "mv" and target_type == "file":
            with (open(source_file_option, "r") as source_file_obj,
                  open(target_file_option, "w") as target_file_obj):
                source_file_data = source_file_obj.read()
                target_file_obj.write(source_file_data)
                os.remove(source_file_option)

        if action == "mv" and path_exist and target_type == "folder":
            with (open(source_file_option, "r") as source_file_obj,
                  open(target_file_option, "w") as target_file_obj):
                source_file_data = source_file_obj.read()
                target_file_obj.write(source_file_data)
                os.remove(source_file_option)

        if action == "mv" and not path_exist and target_type == "folder":
            os.makedirs(target_folders_path)

            with (open(source_file_option, "r") as source_file_obj,
                  open(target_file_option, "w") as target_file_obj):
                source_file_data = source_file_obj.read()
                target_file_obj.write(source_file_data)
                os.remove(source_file_option)

        if action != "mv":
            print(f"Wrong action is used{action}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Used file is not found")
    except IOError as e:
        print(f"Error: {e}")
        print("Read/Write error happened")
