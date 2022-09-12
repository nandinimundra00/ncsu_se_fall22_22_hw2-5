import re


def coerce(s: str) -> int | float | bool | str:
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
