########################### init parts ################################
import random

print("\nWelcome to Tic Tac Toe game!\n")
table = [
    ['   ', ' a ', ' b ', ' c ',],
    [' 0 ', '   ', '   ', '   ',],
    [' 1 ', '   ', '   ', '   ',],
    [' 2 ', '   ', '   ', '   ',]
]

i = 0
for row in table:
    print("|".join(row))
    i += 1
    if i<4:
        print("---------------")
print("\n")

endgame = False
format = True
turn = "X"
rows = ["0","1","2"]
cols = ["a","b","c"]
attempts = 0


########################### logic parts ###########################
# check the condition for winner
def check_winner(table):
    winning_combinations = [
            [(1, 1), (1, 2), (1, 3)],   # Rows 0
            [(2, 1), (2, 2), (2, 3)],   # Rows 1
            [(3, 1), (3, 2), (3, 3)],   # Rows 2
            [(1, 1), (2, 1), (3, 1)],   # Columns a
            [(1, 2), (2, 2), (3, 2)],   # Columns b
            [(1, 3), (2, 3), (3, 3)],   # Columns c
            [(1, 1), (2, 2), (3, 3)],   # Diagonals \
            [(1, 3), (2, 2), (3, 1)]    # Diagonals /
    ]
    for combination in winning_combinations:
        markers = [table[row][col] for row, col in combination]
        if markers[0] != '   ' and markers[0] == markers[1] == markers[2]:
            return markers[0]  # Return the winning marker
    return None  # No winner found

# game loop
while endgame == False:

# check input if it's the correct format or not 
    if turn == "X":
        print("X Turn")
        col = input("column a,b,c ---> ")
        row = input("row 0,1,2 ---> ")
    else:
        col = random.choice(cols)
        row = random.choice(rows)

# check the columns format 
    if col == "a":
        col = 1
    elif col == "b":
        col = 2
    elif col == "c":
        col = 3
    else:
        col = 100
        format = False

# check the rows format
    if row not in rows:
        row = 100
        format = False
    else:
        row = int(row) + 1
    print("\n")

# if the format is corrects 
    if format == True:
        
        if table[row][col] == "   ":

            table[row][col] = f' {turn} '
            i = 0
            for row in table:
                print("|".join(row))
                i += 1
                if i<4:
                    print("---------------")

            if turn == "X":
                turn = "O"
                
            else:
                turn = "X"
                attempts += 1
                print("\n")

        else:
            if turn == "X":
                print("You can pick only the empty cells please re-type :)\n")

    else:
        print("Invalid row or column. Please re-type.\n")
        format = True

    if attempts == 4:
        endgame = True
        print("### Draw! ###\n")

# winner is 
    winner = check_winner(table)
    if winner:
        print(f"\n### Player {winner} wins! ###\n")
        endgame = True
    