import argparse
import subprocess


def my_supervisorctl():
    print("my_supervisorctl")

def my_supervisorctl_foo():
    print("foo")

def my_supervisorctl_bar():
    print("bar")

__all__ = ['my_supervisorctl, my_supervisorctl_foo, my_supervisorctl_bar']
