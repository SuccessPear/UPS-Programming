# hihi
def frog_cross_river(stones: list[int]):
    # Create a stack
    # Value in the stack will be in format (stone, step)
    # Stone: the stone value itself
    # Step: the number of step that the frog use to jump to the stone
    stone_stack = []
    
    # Append the first stone to the stack
    stone_stack.append([0, 1])
    
    # Loop until stack have no value
    while(len(stone_stack) > 0):
        stone, step = stone_stack.pop()
        
        # Consider 3 possible case step-1, step, step+1
        for i in [-1, 0, 1]:
            # Check if there is a stone on each case
            if step + i > 0 and stone + step + i in stones:
                # If we reach the last stone, return True
                if stone + step + i == stones[-1]:
                    return True
                
                # Add new (stone, step) to the stack
                stone_stack.append([stone+step+i, step+i])
    
    # After the while loop and we still not reach the end stone,
    # It means that the frog can't cross the river, so return False.
    return False

#stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]
print(frog_cross_river(stones))