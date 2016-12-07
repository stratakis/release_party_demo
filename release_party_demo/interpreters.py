import os


def get_py_interpreters():
    python_interpreters = {"python3.5",
                           "python3.4",
                           "python3.3",
                           "python2.7",
                           "python2.6",
                           "pypy",
                           "pypy3",
                           "jython",
                           "micropython"}

    for ex in os.listdir("/usr/bin"):
        if ex in python_interpreters:
            yield(ex)


def main():
    print("Installed python interpretes:")
    for interpreter in get_py_interpreters():
        print("  * {0}".format(interpreter))
