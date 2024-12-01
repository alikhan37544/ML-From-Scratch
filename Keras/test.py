print("to set environment variable to env_hack in different operating systems where this is run")


"""
Notes for self : 
The reason why you were having issues was because of visual studio code's inability to automatically figure out the virtual env outside it's scope

This is an issue especially apparent in linux, where system apps also depend on Python.

Ran into issues with Arch, as it came with python 3.12, but needed python 3.10 due to numpy. Virtual environment will always be a headache unless you set up your VSC to detect it
"""

# Go to the interpreter in whatever OS you're using and select the env hack, which you've made everywhere except for windows