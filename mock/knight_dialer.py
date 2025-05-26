class Solution:
    def knightDialer(self, n: int) -> int:
        # Initialize an array to store the possible positions of the knight on the phone pad
        cur_pos = [1] * 10

        # Loop through the number of jumps required
        for jump in range(2, n + 1):
            # Create a new list to store the updated positions after each jump
            new_pos = [0] * 10

            # Calculate the new positions based on the valid knight moves
            new_pos[0] = (cur_pos[6] + cur_pos[4])
            new_pos[1] = (cur_pos[6] + cur_pos[8])
            new_pos[2] = (cur_pos[7] + cur_pos[9])
            new_pos[3] = (cur_pos[4] + cur_pos[8])
            new_pos[4] = (cur_pos[0] + cur_pos[3] + cur_pos[9]) 
            new_pos[5] = 0  # Knight cannot move to position 5
            new_pos[6] = (cur_pos[0] + cur_pos[1] + cur_pos[7]) 
            new_pos[7] = (cur_pos[2] + cur_pos[6]) 
            new_pos[8] = (cur_pos[1] + cur_pos[3]) 
            new_pos[9] = (cur_pos[2] + cur_pos[4]) 

            # Update the current positions list for the next iteration
            cur_pos = new_pos

        return sum(cur_pos) % 10**9 + 7
