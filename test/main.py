# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


@pytest.fixture()
def correct_arguments_string_json() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.json"], "/home/user/file.json"


@pytest.fixture()
def noncorrect_arguments_string_json() -> list[str]:
    return ["/home/user/file.json"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
    assert e.type == SystemExit


def test_get_path_from_correct_arguments_json(
        correct_arguments_string_json: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string_json[0])
    assert path == correct_arguments_string_json[1]


def test_get_path_from_noncorrect_arguments_json(
        noncorrect_arguments_string_json: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string_json[0])
    assert e.type == SystemExit
