in_file = open("isbn.txt","r")
lst_str = []

for line in infile:
    line = line.rstrip("/n")
    lst_str.append(line)

infile.close()

lst_str2 = []
lst_int = []
response = []

for i in range(len(lst_str)):
    
    lst_str2.append(int(lst_str[i]))


for i in range(len(lst_str2)):
    for ch in lst_str2[i]:
        if ch != 'X' and ch != '-' and ch.isdigit ==  False :
            response.append('invalid')



        
