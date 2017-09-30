palin = (int)(input('Enter a number\n'))
notFound= True
palin_str = (str)(palin)
while(notFound):
    if((palin_str==palin_str[::-1]) and len(palin_str)%2==1):
        notFound=False
        palin_str = (str)(palin)
        break
    palin+=1
    palin_str = (str)(palin)

print("Next greatest palindrome is " +palin_str)
