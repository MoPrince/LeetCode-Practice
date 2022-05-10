class Solution:
    def divide(self, d1: int, d2: int) -> int:
        k = -1 if (d1<0)^(d2<0) else 1

        d1, d2, count, temp, mult = abs(d1), abs(d2), 0, 1, abs(d2)

        while d1>=d2:
            
            while mult + mult < d1:

                temp += temp
                mult += mult

            d1 -= mult
            count += temp
            temp, mult= 1, d2




        return max(-2147483648, min((count)*k, 2147483647))