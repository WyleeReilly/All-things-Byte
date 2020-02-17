"""Three rods, x number of disks
All disks start on the leftmost rod in ascending order
1. Only one disk can be moved at a time
2. You can only grab the top tisk from one of the stacks to place it on another stack
3. No larger disk can be placed on top of a smaller disk

Write a function that solves the Tower of Hanoi

Your function should perform the moves necessary to rearrange the towerm and
it should return the total number of steps required to solve the puzzle.

HINT -- THIS EXERCISE WILL INVOLVE RECURSION"""




def tower_move(disks, start, finish, middle):
    global moves
    moves = 0
    if disks ==1:
        print("Move disk 1 from rod",start,"to rod", finish)
        moves +=1
        return
    tower_move(disks-1, start, middle, finish)
    print("Move disk", disks, "from rod", start, "to rod", finish)
    moves+=1
    tower_move(disks-1,middle, finish, start)

tower_move(5, 'A', 'C', 'B')

