class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        
        
        n = len(original)
    
    # Calculate the minimum and maximum possible shifts from the original array
        min_shift = float('-inf')
        max_shift = float('inf')
    
        for i in range(n):
            
        # For each position, calculate how much we can shift the original value up or down
        # while staying within bounds
            local_min_shift = bounds[i][0] - original[i]  # How much we need to shift up at minimum
            local_max_shift = bounds[i][1] - original[i]  # How much we can shift up at maximum
        
        # Update our global min and max shifts
            min_shift = max(min_shift, local_min_shift)
            max_shift = min(max_shift, local_max_shift)
    
        if min_shift > max_shift:
            
            return 0
        
        return max(0, max_shift - min_shift + 1)

        