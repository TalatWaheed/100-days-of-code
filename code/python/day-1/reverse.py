a = input("Enter a string:")
l=1
a1=""
for letter in a:
  l=l+1
while l>=0:
  a1=a1+a[l]
  l=l-1
print(a1)  
