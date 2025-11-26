"""
run the main app
"""
from .etc import Etc


def run() -> None:
    reply = Etc().run()
    print(reply)
