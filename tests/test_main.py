import os
import shutil

import pytest

from app.main import move_file


@pytest.fixture
def create_file(filename: str = "file.txt") -> str:
    content = "This is some\n content for\n the file."

    with open(filename, "w") as created_file:
        created_file.write(content)

    return filename


def test_file_renamed(create_file: callable) -> None:
    move_file("mv file.txt file1.txt")

    assert os.path.exists("file.txt") is False
    with open("file1.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    os.remove("file1.txt")


def test_should_work_when_directory_exists(create_file: callable) -> None:
    os.makedirs("dir")
    move_file(f"mv file.txt dir/file2.txt")

    with open("dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists("file.txt") is False

    shutil.rmtree("dir")


def test_should_create_multiple_directories(create_file: callable) -> None:
    move_file(f"mv file.txt first_dir/second_dir/file2.txt")

    assert os.path.exists("first_dir/second_dir/file2.txt") is True
    assert os.path.exists("file.txt") is False

    with open("first_dir/second_dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    shutil.rmtree("first_dir")


def test_should_create_multiple_directories_when_they_exist(create_file: callable) -> None:
    os.makedirs("first_dir/second_dir")
    move_file(f"mv file.txt first_dir/second_dir/third_dir/file2.txt")

    with open("first_dir/second_dir/third_dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists("file.txt") is False

    shutil.rmtree("first_dir")


# Novos testes para validação de erros


def test_invalid_command_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Invalid command format"):
        move_file("cp file.txt file2.txt")


def test_missing_arguments_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Invalid command format"):
        move_file("mv file.txt")


def test_non_existent_source_raises_file_not_found_error() -> None:
    with pytest.raises(FileNotFoundError, match="Source file not found"):
        move_file("mv non_existent.txt destination.txt")


def test_move_to_directory_with_trailing_slash(create_file: callable) -> None:
    os.makedirs("target_dir")
    move_file("mv file.txt target_dir/")

    assert os.path.exists("target_dir/file.txt") is True
    assert os.path.exists("file.txt") is False

    with open("target_dir/file.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    shutil.rmtree("target_dir")