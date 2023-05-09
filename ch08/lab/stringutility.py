

class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        '''
        Returns a string of the string utility object 
        Args: self (StringUtility Object) 
        Returns: (str) String of the object
        '''
        return self.string
    
    def vowels(self):
        '''
        Retruns a count of the vowels in the string object. If it is greater than or equal it 5, the function returns "many". 
        Args: self (StringUtility Object)
        Return: (str) A string of the vowel count, or many if it 5 or more. 
        '''
        vowels = 'aeiou'
        count = 0
        for i in self.string:
            if i in vowels: 
                count += 1
                if count >= 5:
                    count = "many"
                    break
        if count == "many": 
            return count
        else: 
            return str(count)
    
    def bothEnds(self):
        '''
        Returns the first and last two letters in the word. If the word is 2 or less letters it returns an empty string. 
        args: self (StringUtility Object)
        return: (str) String object with the first and last two letters or an empty string
        '''
        if len(self.string)<= 2: 
            return ''
        else: 
            return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
        

    def fixStart(self):
        '''
        The fuction takes the first letter of the word and replaces any repitition of it with "*"
        args: self (StringUtility Object)
        return: (str) String of the word with letters the same as in the first position replaced with "*". If the word has one or less letters the same string is returned. 
        '''
        length = len(self.string)
        if length <= 1:
            return self.string
        else:
            new_string = self.string[0] + self.string[1:].replace(self.string[0], "*")
            return new_string
        

    def asciiSum(self):
        '''
        Returns the sum of the ASCII values in the string 
        args: self (StringUtility Object)
        return: (int) The sum of the ASCII values in the string 
        '''
        value = 0
        for i in self.string: 
            value += ord(i)
        return value 
    
    def cipher(self): 
        '''
        Creates an encrypted message, that moves the letters in word to the postion of the length of the word. 
        args: self (StringUtility Object)
        return: (str) A string of the encypted word. 
        '''
        new_word = ""
        length = len(self.string) 
        for i in self.string:
            if i.isalpha():
                start = ord('A') if i.isupper() else ord('a') 
                num_let = ord(i)
                new_num_let = (num_let - start + length) % 26
                new_let = chr(new_num_let + start)
                new_word += new_let
            else: 
                new_word += i
        return new_word

        


                   

        
