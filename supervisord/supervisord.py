import argparse
import subprocess

def my_supervisord():
    print("my_supervisord")

def my_supervisord_foo():
    print("foo")

def my_supervisord_bar():
    print("bar")

__all__ = ['my_supervisord, my_supervisord_foo, my_supervisord_bar']