class Solution:
    def convert(self, s: str, n: int) -> str:
        
        lst, move, reverse, k = ['']*n, 0, False, n-1


        if n == 1:
            
            return s
        
        
        for index, char in enumerate(s):

            if k == index:

                k = index + n + (n-2)

                reverse = True


            elif move ==0 and index !=0 :

                reverse = False


            if not reverse:

                lst[move] += char

                move += 1


            else:

                lst [move] += char

                move -= 1


        return(''.join(lst))
                
        
        
            