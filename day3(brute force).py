# intuition
# - find all the symbols and their index in the string
# - use regex to match  positions of digits and their spans 
# - find all posible valid indexes

import re

symbol_regex = r"[^A-Za-z0-9.\n]"
digit_regex = r"\d?(\d)+"

found = False
count = 0

collision_pos = {} # stores line: and the range of indices

def check_collision(lowest_index, largest_index, i, j):
    if i in range(lowest_index, largest_index+1) or j in range(lowest_index, largest_index+1) or (lowest_index in range(i,j+1) and largest_index in range(i,j+1) ):
        return True
    return False
    
with open('test.txt') as my_input:
    lines_list = my_input.readlines()
    for index,line in enumerate(lines_list):
        
        for strMatch in re.finditer(symbol_regex, line):
            # print(strMatch)
            # print(index-1, index , index + 1)
            (symbolPos , v) = strMatch.span()
            # print(line[symbolPos])
            
            # Line above
            indexes = [index-1, index, index + 1]
            for i in indexes:
                if i not in collision_pos:
                    collision_pos[i] = list()
                    collision_pos[i].append((symbolPos-1,symbolPos +1))
                else:
                    # collision_pos[i].append((symbolPos-1,symbolPos +1))
        
                    if (symbolPos-1,symbolPos +1) not in collision_pos[i]:
                        collision_pos[i].append((symbolPos-1,symbolPos +1))
        

    
    print(collision_pos)
    # print(collision_pos.values)
    for line_index, _line in enumerate(lines_list):
        # for each line
        for digMatch in re.finditer(digit_regex, _line):
            # for all digits matched in line
            
            (i,j) = digMatch.span() # the span of the index of the digits found
            
            valid_index = [line_index-1, line_index, line_index + 1] # what lines to check (3 iterations)
            print(digMatch)
            print(valid_index)
            # print(valid_index)
            for vi in valid_index: 
                # check the valid lines for matches (3 iterations max)
                if(vi >= 0 and vi < len(lines_list)):
                    # check if the index is valid for the 2 edge cases ( first line and last line as -1 and len(lines_list) are invalid)
                    for (lowest_index, largest_index) in collision_pos[vi]:
                        # check each colision spot, if it is a valid collision 
                        found = check_collision(lowest_index,largest_index, i,j)
                       
                        
                    
                if(found):
                    # don't check the rest of the valid indexes
                    # print(digMatch.group())
                    count += int(digMatch.group())
                    break

    print(count)
                    
          