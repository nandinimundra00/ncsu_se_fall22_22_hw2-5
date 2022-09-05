import csv
from ntpath import join
import os
import re
from data.constants import getConstant
import sys


# Todo : Move methods into their respective files
def coerce(s: str) -> int | float | bool | str:
    """
    Parse 'the' config settings from 'help'
    @s: string input
    """
    try:
        def fun(s1: str) -> bool | str:
            """
            Converts incoming string into either int, float or bool based on it's type
            @s1: string input
            """
            if s1 == 'true' or s1.lower() == 'true':
                return True
            if s1 == 'false' or s1.lower() == 'false':
                return False
            return s1
        val = s
        try:
            val = int(s)
        except ValueError:
            try:
                val = float(s)
            except ValueError:
                # val = fun(s.strip())  Can run inbuilt strip to remove leading and trailing spaces, but using implementation similar to lua code
                val = fun(re.search('^\s*(.+?)\s*$', s).group(1))
        return val
    except Exception as e:
        print('Some error occurred in coerce function. Please try again. Error: ', e)
        exit()


def getValuesFromHelp(help: str) -> dict:
    """
    Pull help from constants and parse values into 'the'
    @help: help string from constants
    """
    try:
        matchedVals = re.findall('\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', help)
        updatedThe = {}
        for val in matchedVals:
            updatedThe[val[0]] = coerce(val[1])
        return updatedThe
    except Exception as e:
        print('Some error occurred in getValuesFromHelp function. Please try again. Error: ', e)
        exit()


def cli(t: dict, help: str) -> dict:
    """
    Update value in 'the' based on command line arguments. Print 'help' string if user enters help options
    @t: 'the' object
    @help: help string from constants
    """
    try:
        tKeys = list(t.keys())
        for key in tKeys:
            val = str(t[key])
            args = sys.argv
            for i in range(1, len(args)):
                if args[i] == '-' + key[0:1] or args[i] == '--' + key:
                    val = val == "False" and "True" or val == "True" and "False" or args[i + 1]
            t[key] = coerce(val)
        if t['help'] == True:
            print('\n', help, '\n')
            exit()
        return t
    except Exception as e:
        print('Some error occurred in cli function. Please try again. Error: ', e)
        exit()


def readFromCSV(fname: str, the: dict, func) -> None:
    """
    Read content from CSV file and run a custom function on each row
    @fname: file path with file name
    @the: 'the' object
    @func: custom user function
    """
    try:
        sep = the['Seperator']
        currentWorkingPath = os.path.dirname(__file__)
        relativePath = os.path.join(currentWorkingPath, fname)
        with open(relativePath, 'r') as file:
            reader = csv.reader(file, delimiter=sep)
            for row in reader:
                func(row)
    except Exception as e:
        print('Some error occurred in readFromCSV function. Please try again. Error: ', e)
        exit()


def o(t: int | float | bool | str | dict) -> str:
    """
    Print values for a column or dict
    @t: input to be printed
    """
    try:
        if type(t) != dict:
            return str(t)

        def show(k, v):
            """
            Ignore the values for keys starting with '_', else format the output in the form ':key val' or 'val'
            @k: key
            @v: val
            """
            if str(k).find('^_') == -1:
                v = o(v)
                return len(t) == 0 and format(':{} {}', k, v) or str(v)
        valArr = []
        counter = 0
        tKeys = list(t.keys())
        for key in tKeys:
            valArr[counter] = show(key, t[key])
        if len(t) == 0:
            valArr.sort()
        return '{' + ' '.join(str(val) for val in valArr) + '}'
    except Exception as e:
        print('Some error occurred in o function. Please try again. Error: ', e)
        exit()


def oo(t: dict) -> dict:
    """
    Prints input object
    @t: input object
    """
    try:
        print(o(t))
        return t
    except Exception as e:
        print('Some error occurred in oo function. Please try again. Error: ', e)
        exit()

# Todo : Remove this once other user defined functions are ready


def test(row: list) -> None:
    """
    Test function to use as user-defined function
    @row: A single row from the CSV file
    """
    return None


def main():
    """
    Main function
    """
    try:
        help = getConstant('help')
        the = {}
        the = getValuesFromHelp(help)
        the = cli(the, help)
        dataSet = readFromCSV('../data/input.csv', the, test)
    except Exception as e:
        print('Something went wrong in the main function. Please try again', e)
        exit()


if __name__ == "__main__":
    main()
