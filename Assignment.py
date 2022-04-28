small = int(input(" Enter the small Value: "))
large= int(input(" Enter the large Value: "))
total = 0

for Num in range (small, large + 1):
    count = 0
    for i in range(2, (Num//2 + 1)):
        if(Num % i == 0):
            count = count + 1
            break

    if (count == 0 and Num != 1):
        print(" %d" %Num, end = '  ')
        total = total + Num

print("\n\nSum from %d to %d = %d" %(small, large, total))
