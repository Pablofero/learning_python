import matplotlib.pyplot as plt
import string

ascii = string.ascii_lowercase
a = input()
a = str.lower(a)
a = sorted(a)#[a,a,b,c,c,...,z,z]

b = [0]*len(list(ascii))#[0,0,...,0] used for keeping count of how many letters are found

# go trough every index of the input array a and compare it with the ascii list, if a match increment that letter in b 
for element in range(len(a)):
	for compare in range(len(b)):
		if(a[element]==list(ascii)[compare]):
			b[compare]+=1

c = [0]*len(b) 
for i in range(len(b)):
	c[i] = [b[i],ord(list(ascii)[i])] #[[a,b],[a,b]...] a = amount(int),b = ascii number(int)
x = sorted(c, key=lambda x:x[0],reverse=True) # c sorted by amount (reversed, biggest at beginning)
ascii_list = [""]*len(b)
for i in range(len(b)):
	ascii_list[i] = chr(x[i][1]) #letters sorted by extracting from x
b = sorted(b,reverse=True) #sort b (reversed, biggest at beginning)
percent = [0]*len(b) 
for i in range(len(b)):
	percent[i] = b[i]/len(a)#calcuate percentage
print(percent,ascii_list)
plt.bar(range(len(b)),percent,tick_label=ascii_list)
plt.ylabel('amount')
plt.show()