#1.1 given a number count the total number of digits in a number:
'''
num =input("Enter A number for count")
a=(len(num))
print(a)
'''


#1.2 reverse the following list using loop
'''
list1=[10,20,30,40,50]
for i in reversed(list1):
    print("The reverse list is",i)
'''



#2 string by append method:
'''
def appendmiddle(s1,s2):
    mid=int(len(s1)/2)
    print("string are :",s1,s2)
    output=s1[:mid-1:]+s2+s1[mid-1:]
    print("appended string:",output)

appendmiddle("chrisdem","IamNewString")

'''

#5 picking odd and even then add in new list
'''
listone=[3,6,9,12,15,18,21]
listtwo=[4,8,12,16,20,24,28]
listthird=list()
odd=listone[1::2]
even=listtwo[0::2]
print(odd)
print(even)
listthird.extend(odd)
listthird.extend(even)
print(listthird)
    
'''


#3

string=input("Enter the string")
w=string.split()
lower=[]
upper=[]
for i in  string:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
sortstring=''.join(lower + upper)
print("\n lower letter ")
print(sortstring)


