import re, argparse, sys
from urllib import parse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file containing urls with directories.")
parser.add_argument("-v", "--verbose", help="increase verbosness")
args = parser.parse_args()

directories = []
parameters = []

if not args.file:
    sys.exit(f"Usage: {sys.argv[0]} -f urls.txt")
else:
    try:

        #get stuff from urls
        with open(args.file) as f:

            for line in f:
                line = parse.urlparse(line) # ParseResult Object (scheme, netloc, path, params, query, fragment)
                
                if line != "/\n" and len(line.path) > 1:
                    directories.append(line.path)
                if len(line.query) > 1: 
                    parameters.append(line.query)
                if len(line.params) > 1: #checking if urls contains parameters
                    parameters.append(line.params)

                
         
        #write results to files
        output_directories_filename = "directories-huntlist.txt"
        output_parameters_filename = "parameters-huntlist.txt"

        try:
            file = open(f"{output_directories_filename}", "w")
            for dirs in directories:
                file.write(dirs)
            file.close()

        except:
            sys.exit(f"[ERROR] failed to create {output_directories_filename} file")

        try:
            file = open(f"{output_parameters_filename}", "w")
            for params in parameters:
                file.write(params)
            file.close()

        except:
            sys.exit(f"[ERROR] failed to create {output_parameters_filename} file")

    except:
        sys.exit(f"[ERROR] Can't open OR Can't find {args.file} in the current directory")
