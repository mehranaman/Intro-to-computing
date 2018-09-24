def check_str(string):
    for ch in string:
        if not ch.isdigit() and not ch == 'x' and not ch == 'X' and not ch=='-':
            return False
        if (ch == 'x' or ch == 'X') and ch!= string[-1]:
            return False
    return True


            


def Xto10inte(string):
    lst_sum = []
    string2 = ''
    for i in range(len(string)):
        if string[i] != '-':
            string2 += string[i]

    for i in range(len(string2)-1):
        lst_sum.append(eval(string2[i]))
    if string2[-1] == 'x' or string2[-1] == 'X':
        lst_sum.append(10)
    else:
        lst_sum.append(eval(string[-1]))



    
    return lst_sum   
        




def read_string():
    in_file = open("isbn.txt","r")
    lst_sum = []
    lst_str = []
    sum1 = 0
    sum2 = 0 
    out_file = open("isbnOut.txt","w")
    
    for line in in_file:
        l = line.rstrip("\n")
        lst_str.append(l)

    lst_str_main = []
    lst_str_defunct= []
    lst_sum_int = []
    lst_final = []
    
    for i in range (len(lst_str)):
        
        if check_str(lst_str[i]):
            lst_str_main.append(lst_str[i])

        else:
            lst_str_defunct.append(lst_str[i])

    for i in range (len(lst_str_main)):
        string_final = ''
        lst_sum = (Xto10inte(lst_str[i]))


#s1
        for i in range (len(lst_sum)):
            
            sum1 += lst_sum[i]
            lst_sum_int.append(sum1)
    
#s2
        for i in range (len(lst_sum_int)):
            sum2 += lst_sum_int[i]

        if sum2%11 == 0:
            for i in range(len(lst_sum_int)):
                string_final += str((lst_sum_int[i]))
            out_file.write(string_final)
            out_file.write("valid\n")
        else:
            for i in range(len(lst_sum_int)):
                string_final += str((lst_sum_int[i]))
            out_file.write(string_final)
            out_file.write(" invalid\n")
           
                                               
    out_file.close()
    in_file.close()

read_string()
        
    

    








    
                       
        
    
        
