class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_int = digits.pop()     
        add_one = last_int + 1          
        
        if add_one < 10:
            digits.append(add_one)
            return digits
        
        digits.append(0)     
        
        i = len(digits) - 2 
        
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0   
                i -= 1
            else:
                digits[i] += 1  
                return digits   
        
        return [1] + digits

        