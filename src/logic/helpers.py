from os import name, system

__all__ = [
    "cc"
]

def cc():
    system("cls" if name == "nt" else "clear")