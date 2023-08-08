import os
import subprocess
import sys

sys.path.insert(1, '/home/codio/workspace')
from exerc import collaborative_chat_gpt


def test_collaborative_chat_gpt():
    try:
        response = collaborative_chat_gpt("What is the capital of France?")
        assert isinstance(response, str), "Output should be a string"
        assert "paris" in response.lower(), "Output should contain the word 'Paris'"
        print("Test passed!")
    except Exception as e:
        print(f"Test failed with error: {e}")

test_collaborative_chat_gpt()
