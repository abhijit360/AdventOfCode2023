import re

def valid_num_sliceEntry(x,y):
    # this method sets up the slice for the string.
    if x not in valid_nums.keys():
        valid_nums[x] = (y,y)
    else:
        (lowest, largest) = valid_nums[x]

        new_low = y if y < lowest else lowest
        new_high = y if y > largest else largest
        valid_nums[x] = (new_low, new_high)
        

def getAllAdjacentNums(x, y,seen):
    
    if(y < 0 or y >=len(grid[x]) or grid[x][y] == "."):
        # make sure the base case is correct
        return
    if(grid[x][y].isdigit()):
        if (x,y) not in seen:
            # x is row, y is the str index
            seen.append((x,y))
            valid_num_sliceEntry(x,y)
        else:
            return
    # print(lines_list[x][y])
    getAllAdjacentNums(x,y-1,seen)
    getAllAdjacentNums(x,y+1,seen)
    

def get_neighbours(x,y,):
    for dx in [-1, 0 , 1]:
        for dy in [-1,0,1]:
            if (dx,dy) == (0,0):
                continue
            neighbour_x , neighbour_y = x + dx, y + dy
            yield neighbour_x, neighbour_y

valid_nums = {}

grid = []
total = 0
seen = []
count = 0

with open('inputdaythree.txt') as my_input:
    for line in my_input.readlines():
        grid.append(line.strip())

    for x,row in enumerate(grid):
       for y,char in enumerate(row):
           if char.isdigit() or char == ".":
               continue
           else:
               neighbour_iter = get_neighbours(x,y)
               while True:
                    try:
                        nbr_x,nbr_y = next(neighbour_iter)
                        getAllAdjacentNums(nbr_x,nbr_y,seen)
                    except StopIteration:
                       break
              
             
        # val = re.findall(r'[^A-Za-z0-9.\n', row)
        # print(val)
    
for row in valid_nums:
    i,j = valid_nums[row]
    # print(grid[row][i:j+1])
    vals = re.findall(r"\d?\d+", grid[row][i:j+1])
    # print(vals)
    for val in vals:
        count += int(val) 


print(valid_nums)
print(count)