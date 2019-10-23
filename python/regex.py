import re

# docs.python.org/3/howto/regex.html
# Chorey Schafer video about RE on youtube

text_to_search = """
    #Special Metacharacters (need to be escaped if you want to match them)

        . ^ * $ + ? { } [ ] \ | ( )

    #Character Classes

    \d decimal digits   [0-9]
    \D non-digit        [^0-9]
    \s whitespaces      [\t\n\r\f\v]
    \S non-whitespaces  [^ \t\n\r\f\v]
    \w alphanumeric     [a-zA-Z0-9_]
    \W non-alphanumeric [^a-zA-Z0-9_]

    abcdefghijklmnopqrstuvwyxz
    ABCDEFGHIJKLMNOPQRSTUVWYXZ

    Ha HaHa

    321-555-4321
    123.555.1234

    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson

    www.example.com/events/giveaway/images/tab.gif/admin
    www.example.com/scripts/login.js
    www.example.com/Portal/login.aspx?oauth2=true&v=1.2
    www.example.com/index.html

    Directories : [\w]+\/
    Filenames   : [^ =www.\w][\w]+\.[\w]+


"""

# Regular Expressions are compiled into pattern objects
# This is where you put your RE
pattern = re.compile(r'[^ =www.\w][\w]+\.[\w]+')

"""
    Pattern Object Methods

    match()         searches at the beginning of the string
    search()        scan through string looking for any match
    findall()       find all substrings and return matches as a list
    finditer()      find all substrings and return matches as an iterator

"""

matches = pattern.findall(text_to_search)
print(matches)
 