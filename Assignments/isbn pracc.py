def isbn():
    
    lst_str = []

    in_file = open("./isbn.txt","r")

    for line in in_file:
        l = line.rstrip("/n")
        lst_str.append(l)


    for i in range (len(lst_str)):
        temp = []
        for ch in (lst_str[i]):
            if ch.isdigit() or ch == 'x' or ch == 'X' or ch == '-':
                if ch.isdigit() or ch == 'x' or ch == 'X':
                    temp.append(ch)
            else:
                return False
            
        
        if temp[-1] == 'x' or temp[-1] == 'X':
            temp[-1] == '10'
            
        for i in range (len(temp)):
            temp[i] == int(temp[i])

        sum1 = 0


#s1
        for i in range (len(temp)-1):
            sum1 += temp[i]
            temp[i+1] == sum1


#s2
        sum2 = 0
        for q in range(len(temp)-1):
            sum2 += temp[q]
            temp[q] == sum2

        if temp[-1]%11 == 0:
            out_file = open("./isbnOut.txt","w")
            out_file.write(lst_str[i], "valid/n")
            outfile.close()



isbn()
            
            
        
            
        
                
                
                
        
    









    
    
