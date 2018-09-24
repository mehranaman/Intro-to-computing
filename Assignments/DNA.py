#File: DNA.py
#Description: Computing the largest pair of similarity in a pair of DNA seqeunce. 
#Name: Naman Mehra
#UTEID: nm26465
#Course name: CS303E
#Unique number: 51850
#Date created: March 28th, 2017
#Date last modified: Feb 24th, 2017

def main():
    in_file = open("/Users/NamanMehra/Documents/CS303E/HW/Assignments/dna.txt" ,"r")
    num_pairs = (in_file.readline())
    num_pairs = int(num_pairs.strip())

    print("Longest Common Sequences")
    for i in range(num_pairs):
        q = []
        flag = False
        p = 0
        st1 = in_file.readline()
        st2 = in_file.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        if len(st1) > len(st2):
            dna1 = st1
            dna2 = st2

        else:
            dna1 = st2
            dna2 = st1

        print("Pair " + str(i+1) + ": ", end = '')
        wnd = len(dna2)
        while(wnd > 1):
            start_idx = 0
            
            while ((start_idx + wnd) <=len(dna2)):
                sub_strand = dna2[start_idx:start_idx + wnd]
                if sub_strand in dna1:
                    if len(sub_strand) >= p:
                        p = len(sub_strand)
                        if sub_strand not in q:
                            q.append(sub_strand)
                            
                            print(sub_strand)
                            print('        ', end = '')
                        flag = True
                
        
                start_idx += 1
            wnd = wnd - 1
        
        if flag == False:
            print("No Common Sequence Found")
        print()

    in_file.close()



main()





            
