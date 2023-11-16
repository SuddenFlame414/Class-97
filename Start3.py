z=input("Enter value")
wordcount=1
charectarcount=0
for i in z:
    charectarcount+=1
    if(i==' '):
        wordcount+=1
    print(charectarcount)
print("The number of words is:")
print(wordcount)
