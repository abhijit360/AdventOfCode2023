import re
games_regex = r"Game\s\d?\d+:"

inventory = {
    "red": 12,
    "green": 13,
    "blue":14
}

best_valid_inventory = {
    "red": 0,
    "green": 0,
    "blue": 0
}


count = 0
powerSet = 0
# 'inputdaytwo.txt'
def calculate_valid_game(draw, game_id):
    for d in draw.split(", "):
        num = re.findall(r'\d?\d+', d.split()[0])[0]
        colour = re.findall(r'\w+',d.split()[1])[0]
        print(colour)
        if int(num) > inventory.get(colour):
            return False
        
        
    return True

def update_inventory_validity(draw):
    for d in draw.split(", "):
        num = re.findall(r'\d?\d+', d.split()[0])[0]
        colour = re.findall(r'\w+',d.split()[1])[0].strip()
        if int(num) > int(best_valid_inventory.get(colour)):
            best_valid_inventory[colour] = int(num)
        else:
            continue
        



with open("inputdaytwo.txt", "r") as my_input:
    for index, line in enumerate(my_input.readlines()):
       
        game_id = index + 1
        # re.match(games_regex, line).group().split()[1][:-1]
        games = re.split(games_regex,line)[1]
        draws = games.split(";")

        for draw in draws:
            update_inventory_validity(draw)
            powerSet_val = 1
            for val in best_valid_inventory.values():
                powerSet_val *= val

        powerSet += powerSet_val  
            
     
        best_valid_inventory =   {"red": 0,"green": 0, "blue": 0}
        # part 1 solution
        # valid_game = True
        # for draw in draws:
        #     valid_game = calculate_valid_game(draw, game_id) 
        #     if not valid_game:
        #         break
        
        # if valid_game:
        #     # print(game_id)
        #     # print(f"game id: {game_id} |", draws)
        #     count += int(game_id)

print(count)
print(powerSet) 
                 
# text = "Game 1: testgame : 1"

# test_game=  re.split(r"(Game \d:)", text)
# print(test_game)
