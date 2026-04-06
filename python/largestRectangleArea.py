class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [-1] # Acts as a dummy left boundary
        heights.append(0) # Sentinel value to flush the stack at the end
        max_area = 0
        
        for i in range(len(heights)):
            # While the current height is lower than the height at the top of stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()] # Height of the rectangle
                w = i - stack[-1] - 1    # Width is distance between boundaries
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        # Remove the sentinel value to keep the input array unchanged (optional)
        heights.pop() 
        return max_area
