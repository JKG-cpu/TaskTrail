from tasktrail import *

if __name__ == "__main__":
    tasktrail = TaskTrail()
    tasktrail.run()
    if getattr(tasktrail, "_quit_properly", False):
        cc()