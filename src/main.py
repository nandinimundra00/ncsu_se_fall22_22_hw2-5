import os
from src.misc import Misc
from tst.testEngine import Tests


def main():
    """
    Main function
    """
    # Find and store environment variables
    b4 = {}
    envs = dict(os.environ)
    for key in list(envs.keys()):
        b4[key] = envs[key]
    # Initiate the misc functions class object
    miscObj = Misc()
    fails = Tests(miscObj).runTests()
    miscObj.rogues(b4)
    print('\nNumber of failed tests: ', fails)


if __name__ == "__main__":
    main()
