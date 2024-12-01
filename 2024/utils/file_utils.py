import re

def read_input(file_path):
    with open(file_path, "r") as f:
        return f.readlines()
 
def format_input_file(input_path, output_path):
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            formatted_line = re.sub(r'\s+', '\t', line.strip())
            outfile.write(formatted_line + '\n')
