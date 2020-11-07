#!/usr/bin/env python3
# Author ID: mjvelota

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    lines = f.read()
    f.close()
    return lines

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    lines = list(f)
    line_len = len(lines)
    for i in range(line_len):
    	lines[i] = lines[i].strip('\n')
    f.close()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
