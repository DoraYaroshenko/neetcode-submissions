import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        m=piles[0]
        m_index = 0
        for i,pile in enumerate(piles):
            if pile>m:
                m=pile
                m_index = i
        if h==n:
            return m
        left = 1
        right = m
        result=m
        while left<=right:
            speed = (left+right)//2
            time_needed_to_eat_all = 0
            for pile in piles:
                hours_needed_for_pile = math.ceil(pile/speed)
                time_needed_to_eat_all += hours_needed_for_pile
            if time_needed_to_eat_all<=h:
                result=speed
                right=speed-1
            elif time_needed_to_eat_all>h:
                left=speed+1
        return result
