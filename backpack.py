
# Python3 implementation of the approach
 
# Function to return the sorted string

def getSortedString():
     
    
    # Strips the newline character 
    file = open("in.txt","r")
    file = file.read()
    lines = file.split(" ")        #lines = [line.replace(" ",",").rstrip() for line in file]
        #lines = [lines. for line in lines]
    # Vectors to store the lowercase
    v1=[]
    
    v2=[]
    # and uppercase characters
    for i in range(0,len(lines)):
        #print(lines[i])
        j = len(lines[i])//2
        v2.append(lines[i][j:])
        v1.append(lines[i][:j])
        #for k in range(0,len(lines[i])//2):
           
    
    #first, snd =    lines[:len(lines)//2],lines[len(lines)//2:]
    print(len(v1))
    #print (" ")
    print (len(v2))
    #res = [x for x in v1 + v2 if x  in v1 and x  in v2]
    list3 = []
    for i in v1:
        for j in v2:
            if j in i:
                i = ''.join(i.split(j))
    list3.append(i)
       #print(list3)
         
        
    return list3

small = {

    a =  1
    b
}

small = getSortedString()
print (small)