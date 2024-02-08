from enum import Enum
import pants.api
import pants.ui
import sys

def _init():
    ostype = sys.platform

    match ostype:
        case "windows":
            pass
        case "darwin":
            print('test')

if __name__ == "__main__":
    _init()