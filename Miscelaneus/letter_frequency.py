import matplotlib.pyplot as plt
import string

### takes an text input and displays it's letter frequency in percentage ###

input = input()# get string
input = str.lower(input)# set all to lowercase 
input = sorted(input)#[a,a,b,c,c,...,z,z]

ascii = string.ascii_lowercase # list of all ascii caracteres
count = [0]*len(list(ascii))#[0,0,...,0] used for keeping count of how many letters are found

# go trough every index of the input array input and compare it with the ascii list, if input match increment that letter in count:
for element in range(len(input)):
	for compare in range(len(count)):
		if(input[element]==list(ascii)[compare]):
			count[compare]+=1

# put caracters and their counts in one data structure to make handeling them easier, as it will keep caracters and counts together:
data = [0]*len(count) 
for i in range(len(count)):
	data[i] = [count[i],ord(list(ascii)[i])] #[[caracter,count],[caracter,count]...] input = amount(is a int),count = ascii number(is a int)
# sort data by count: 
data = sorted(data, key=lambda x:x[0],reverse=True) # data sorted by count (reversed thus biggest at beginning)

# create the label list:
ascii_list = [""]*len(count)# empty string list to populate
for i in range(len(count)):
	ascii_list[i] = chr(data[i][1]) #letters sorted by extracting them from data

# create the percentage list:
percent = [0]*len(data) 
for i in range(len(count)):
	percent[i] = data[i][0]/len(input)#calcuate percentage percentage = #of that caracter / total text lenght 

#display bar graph:
plt.bar(range(len(count)),percent,tick_label=ascii_list)
plt.ylabel('amount')
plt.show()