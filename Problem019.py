daydic = {0:"Monday",
        1:"Tuesday",
          2:"Wednesday",
          3:"Thursday",
          4:"Friday",
          5:"Saturday",
          6:"Sunday" }

my_dict2 = {y: x for x, y in daydic.items()}


monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
daycount = 0
fdoy = "Tuesday"
for i in range(1901,2001):
    if i % 4 == 0:
        monthdays[1] = 29
    else:
        monthdays[1] = 28
    for j in range(0,12):
        num = (monthdays[j] + my_dict2[fdoy]) % 7
        fdoy = daydic[num]
        if fdoy == "Sunday":
            daycount += 1
print(daycount) #171 !
