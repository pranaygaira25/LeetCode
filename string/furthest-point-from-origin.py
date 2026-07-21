class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        x = 0
        unknown = 0
        
        for ch in moves:
            if ch == 'L':
                x -= 1
            elif ch == 'R':
                x += 1
            else:  # '_'
                unknown += 1
        
        return abs(x) + unknown