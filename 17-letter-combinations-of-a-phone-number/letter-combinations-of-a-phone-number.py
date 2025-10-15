class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map=['','','abc','def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        output=[]
        len_digit=len(digits)
        if len_digit == 1: return [key for key in key_map[int(digits)]]

        elif len_digit == 2:
            digit1 = key_map[int(digits[0])]
            digit2 = key_map[int(digits[1])]
            for i in range(len(digit1)):
                for j in range(len(digit2)):
                    output += [digit1[i] + digit2[j]]

        elif len_digit == 3:
            digit1 = key_map[int(digits[0])]
            digit2 = key_map[int(digits[1])]
            digit3 = key_map[int(digits[2])]
            for i in range(len(digit1)):
                for j in range(len(digit2)):
                    for k in range(len(digit3)):
                        output += [digit1[i] + digit2[j] + digit3[k]]
        
        elif len_digit == 4:
            digit1 = key_map[int(digits[0])]
            digit2 = key_map[int(digits[1])]
            digit3 = key_map[int(digits[2])]
            digit4 = key_map[int(digits[3])]
            for i in range(len(digit1)):
                for j in range(len(digit2)):
                    for k in range(len(digit3)):
                        for l in range(len(digit4)):
                            output += [digit1[i] + digit2[j] + digit3[k] + digit4[l]]
        
        return output
