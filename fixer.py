#!/usr/bin/python
import sys;

if(len(sys.argv) > 1):
    f_name = sys.argv[1];
    print("> Reading file: " + f_name);
    in_file = open(f_name, "r");
    all_lines = in_file.readlines()
    first_line = all_lines[0];
    tokens = first_line.split();
    # should have only one token: OFF
    if(len(tokens) > 1):
        # Get the value with the 'OFF'
        tokens[0] = tokens[0].split("OFF")[1];
        edited_line = tokens[0] + " " + tokens[1] + " " + tokens[2] + "\n";
        all_lines[0] = edited_line;
        all_lines = ["OFF\n"] + all_lines;
        in_file.close();
        in_file = open(f_name, "w");
        in_file.writelines(all_lines);
        in_file.close();
    else:
        in_file.close();
    print("> Done!");
else:
    print("> Error: no argv found!");

exit();
