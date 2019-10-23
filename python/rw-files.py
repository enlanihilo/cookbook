#o = open("workfile", "w")  # returns a file object


""" Methods of file objects                             Modes

    read()                                           r+        read and write (only when file is being read)
    readline()                                       w         write
    write('string')                                  a         append
    seek(5) - go to the 5th byte in the file         r         read and write


#creating testfile.txt

file = open("testfile.txt", "w")

file.write("Hello world\n")
file.write("This is our new text file\n")
file.write("and this is another line\n")
file.write("why? because we can\n")

file.close()

"""

content_to_add = """
Hello world
This is our new text file
and this is another line
why? because we ca
"""

# good practice to use 'with' with file objects
try:
    with open("testfile2.txt", "r+") as f:
        file_content = f.read()
except:
    print("I'm creating the file, hold on.")
    file = open("testfile2.txt", "w")   #creating file
    file.write(content_to_add)          #writing to file
    file.close()                        #closing-saving file
    
with open("testfile2.txt", "r+") as f:
    print(f.read())