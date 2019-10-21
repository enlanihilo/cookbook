#o = open("workfile", "w")  # returns a file object


""" Methods of file objects                             Modes

    read()                                           r+        read and write (only when file is being read)
    readline()                                       w         write
    write('string')                                  a         append
    seek(5) - go to the 5th byte in the file         r         read and write

"""

file = open("testfile.txt", "w")

file.write("Hello world\n")
file.write("This is our new text file\n")
file.write("and this is another line\n")
file.write("why? because we can\n")

file.close()

# good practice to use 'with' with file objects
with open("testfile.txt", "r+") as f:
    file_content = f.read()

print(file_content)
