from data.constants import getConstant
import re
import sys
import os


'''
Misc class handles all the utility functions
'''


class Misc:
    def __init__(self) -> None:
        """
        Constructor to assing initial values
        """
        self.help = getConstant('help')
        tempThe = self.getValuesFromHelp()
        self.the = self.cli(tempThe)

    def getValuesFromHelp(self) -> dict:
        """
        Pull help from constants and parse values into 'the'
        """
        matchedVals = re.findall('\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', self.help)
        updatedThe = {}
        for val in matchedVals:
            updatedThe[val[0]] = self.coerce(val[1])
        return updatedThe

    def cli(self, t: dict) -> dict:
        """
        Update value in 'the' based on command line arguments. Print 'help' string if user enters help options
        @t: 'the' object
        """
        tKeys = list(t.keys())
        args = sys.argv
        found = False
        for key in tKeys:
            val = str(t[key])
            for i in range(1, len(args)):
                if args[i] == '-' + key[0:1] or args[i] == '--' + key:
                    found = True
                    val = val == "False" and "True" or val == "True" and "False" or args[i + 1]
            t[key] = self.coerce(val)
        if t['help'] == True or found == False:
            print('\nIncorrect flag entered. Refer the help string below for correct usage details:') if found == False else None
            print('\n', self.help, '\n')
            exit()
        return t

    def coerce(self, s: str) -> int | float | bool | str:
        """
        Parse 'the' config settings from 'help'
        @s: string input
        """
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
            val = float(s)
            if val == int(val):
                val = int(val)
        except ValueError:
            # val = fun(s.strip())  Can run inbuilt strip to remove leading and trailing spaces, but using implementation similar to lua code
            val = fun(re.search('^\s*(.+?)\s*$', s).group(1))
        return val

    def o(self, t: int | float | bool | str | dict) -> str:
        """
        Print values for a column/list or dict
        @t: input to be printed
        """
        if type(t) != dict and type(t) != list:
            return str(t)

        def show(k, v):
            """
            Ignore the values for keys starting with '_', else format the output in the form ':key val' or 'val'
            @k: key
            @v: val
            """
            if str(k).find('_') != 0:
                v = self.o(v)
                return type(t) == dict and ':' + str(k) + ' ' + str(self.coerce(v)) or str(v)
        valArr = []
        if type(t) == dict:
            for key in list(t.keys()):
                showOutput = show(key, t[key])
                if (showOutput):
                    valArr.append(showOutput)
                valArr.sort()
        elif type(t) == list:
            valArr = t
        return '{' + ' '.join(str(val) for val in valArr) + '}'

    def oo(self, t: dict) -> dict:
        """
        Prints input object
        @t: input object
        """
        print(self.o(t))
        return t

    def rogues(self, b4: dict):
        """
        Find rogue locals
        @b4: Dictionary of environment variables at the beginning of the run
        """
        envs = dict(os.environ)
        for key in list(envs.keys()):
            if not b4[key]:
                print('?', key, type(envs[key]))
