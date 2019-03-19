

class NumberToWord():

    def __init__(self):
        self.ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.tens = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.hundreds = "hundred"
        self.thousands = "thousand"
        self.millions = "million"
    
    def convert(self, number):
        num = str(number)
        newNum = ""
        numWord = ""
        if(len(num) == 7):
            numWord = numWord + self.ones[int(num[0])] + " " + self.millions + " "
            newNum = num[1:]

        if(len(newNum) == 6):
            num = newNum

        if(len(num) == 6):
            if(int(num[0]) != 0):
                numWord = numWord + self.ones[int(num[0])] + " " + self.hundreds + " "
            newNum = num[1:]

        if(len(newNum) == 5):
            num = newNum
        
        if(len(num) == 5):
            if(int(num[0]) != 0):
                if(int(num[0:2]) >19):
                    if(int(num[1]) == 0):
                        numWord = numWord + self.tens[int(num[0])] + " " + self.thousands + " "
                        newNum = num[2:]
                    else:
                        numWord = numWord + self.tens[int(num[0])] + " " + self.ones[int(num[1])] + " " + self.thousands + " "
                        newNum = num[2:]
            else:
                newNum = num[1:]

        if(len(newNum) == 4):
            num = newNum

        if(len(num) == 4):
            if(int(num[0]) != 0):
                numWord = numWord + self.ones[int(num[0])] + " " + self.thousands + " "
            newNum = num[1:]
        
        if(len(newNum) == 3):
            num = newNum

        if(len(num) == 3):
            if(int(num[0]) != 0):
                numWord = numWord + self.ones[int(num[0])] + " " + self.hundreds + " "
            newNum = num[1:]

        if(len(newNum) == 2):
            num = newNum

        if(len(num) == 2):
            if(int(num[0]) == 1):
                numWord = numWord + self.ten[int(num[1])] + " "
            elif(int(num[1]) == 0):
                    numWord = numWord + self.tens[int(num[0])] + " "
                    newNum = num[2:]
            else:
                numWord = numWord + self.tens[int(num[0])] + " " + self.ones[int(num[1])] + " "
                newNum = num[2:]
        else:
            if(len(numWord) == 0):
                numWord = numWord + self.ones[int(num[0])] + " "
        
        return numWord

#a = NumberToWord()
#a.convert(9000101)
#a.convert(501)
#a.convert(39101)
#a.convert(4011)
#a.convert(41)
#a.convert(1)
