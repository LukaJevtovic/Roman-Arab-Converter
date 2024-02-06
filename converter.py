roman = input("Enter the Roman numeral: ") #string input of roman numeral
ROMAN = list(roman) #Convert string to a list of characters (e.g. ['C', 'I', 'V'])

ARAB = [] 

number = 0 #this is the variable that will become the converted number

#loop which converts a list of Roman strings into a list of Arab numbers
for i in range(len(ROMAN)):
    
    if ROMAN[i] == 'I':
        ARAB.append(1)
    elif ROMAN[i] == 'V':
        ARAB.append(5)
    elif ROMAN[i] == 'X':
        ARAB.append(10)
    elif ROMAN[i] == 'L':
        ARAB.append(50)
    elif ROMAN[i] == 'C':
        ARAB.append(100)
    elif ROMAN[i] == 'D':
        ARAB.append(500)
    elif ROMAN[i] == 'M':
        ARAB.append(1000)



#loop which does the conversion
i = 0
while i<len(ARAB):

    if i != (len(ARAB)-1): #necessary if to avoid list index out of range error
        
        #Handling small number in front of larger one situations
        if ARAB[i] < ARAB[i+1]:
            number += ARAB[i+1] - ARAB[i]
            i+=2
        #Otherwise just sum up the numbers
        else:
            number += ARAB[i]
            i+=1
            
    else:
        number += ARAB[i]
        i+=1
        
print(number) #Output