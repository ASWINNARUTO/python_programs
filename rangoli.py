#program to print rangoli
import string 
def print_rangoli(size):
    l=list(string.ascii_lowercase)
    n=len("-".join(l[size-1:0:-1]+l[0:size:]))
    for i in range(size-1,-1,-1):
        print("-".join(l[size-1:i:-1]+l[i:size:]).center(n,"-"))
    for i in range(1,size):
        print("-".join(l[size-1:i:-1]+l[i:size:]).center(n,"-"))

size=int(input())
print_rangoli(size)
        
