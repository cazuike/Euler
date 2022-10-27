dic = {
       0:"",
       1:"one",
       2:"two",
       3:"three",
       4:"four",
       5:"five",
       6:"six",
       7:"seven",
       8:"eight",
       9:"nine",
       100:"onehundred",
       200:"twohundred",
       300:"threehundred",
       400:"fourhundred",
       500:"fivehundred",
       600:"sixhundred",
       700:"sevenhundred",
       800:"eighthundred",
       900:"ninehundred",
       1000:"onethousand",
       10:"ten",
       11:"eleven",
       12:"twelve",
       13:"thirteen",
       14:"fourteen",
       15:"fifteen",
       16:"sixteen",
       17:"seventeen",
       18:"eighteen",
       19:"nineteen",
       20:'twenty',
       30:"thirty",
       40:"forty",
       50:"fifty",
       60:"sixty",
       70:"seventy",
       80:"eighty",
       90:"ninety"
       }

def toEnglish(n):
    string = str(n)
    if len(string) == 0:
        return ""
    return dic[int(string[0]) * (10**(len(string)-1))] + toEnglish(string[1:])

total = 0
for i in range(1,1001):
    if i <= 20:
        total += len(dic[i])
    else:
        total += len(toEnglish(i))
    if i > 100:
        total += 3
total += 9
print(total) #21124
