import os

import pytest
from unittest import mock

from app.ugen import read_input, generate_usernames


def test_read_input(tmpdir):
    filepath1 = os.path.join(tmpdir, "test1.txt")
    filepath2 = os.path.join(tmpdir, "test2.txt")
    input_paths = [filepath1, filepath2]

    # write to both files
    file1 = open(filepath1, 'w')
    file1.write("Hello how are you. Why are you here?")
    file1.close()

    file2 = open(filepath2, 'w')
    file2.write("Yes I am. And you are not here.")
    file2.close()

    # Was the list created

    assert read_input(input_paths) == ["Hello how are you.", "Why are you here?",
                                       "Yes I am.", "And you are not here."]

# If you can provide some sample inputs for the lines list I can test them here
lines = ["tkhara:why:here", "hello:not:guy", "why:peter:gimme"]


@mock.patch("app.ugen.random.randint")
def test_generate_usernames(mock_rand_int):
    mock_rand_int.return_value = 3
    print(generate_usernames(lines))
    # If you can provide some sample expected outputs based on the lines input I can
    # test them here
