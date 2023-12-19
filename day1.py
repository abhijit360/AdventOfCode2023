import re

count = 0

letterDict ={
    'one' : '1',
    'two' : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}
# "inputdayonepartone.txt"
with open('inputdayonepartone.txt', "r") as my_input:
    intList = []
    for line in my_input.readlines():
        for key in letterDict.keys():
            for match in re.finditer(key,line):
                # iterate through the iterator.
                # better to use 
                intList.append((letterDict[key], match.span()[0]))
        
        for index, char in enumerate(line):

            if char.isdigit():
                intList.append((char,index))

        min_value = min(intList, key=lambda x: x[1]) 
        max_value = max(intList, key=lambda x: x[1])
        val = min_value[0] + max_value[0]
        # print(val)
        # print(min_value)
        # print(max_value)
        count += int(val)
        intList.clear()  
    
    
    # for (num, val) in intList: 
    #     if(isinstance(num, str)):


     # count += int(intList[0] + intList[len(intList)-1])
    # intList.clear()
    # intList.clear()

print(count)