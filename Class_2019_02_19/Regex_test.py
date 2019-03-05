import re # to import Regex

is_a_match = re.search("^jim$", "jim")

"""
Match: jim
Not match: jam, lam, 0am
"""