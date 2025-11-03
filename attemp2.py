## -- Read input texts into useful formats --

#Open file name example.txt
f = open("example.txt")

#read the first line of the file
towel_inputs = (f.readline()).strip('\n')

#format the line into a list of each towel option
towel_inputs=towel_inputs.split(', ')

desired_towels=[]
#make a list of all the final towel designs
for line in f:
    desired_towels.append((line.strip('\n')))

#remove first element which was blank
desired_towels=desired_towels[1:]
 
#close file
f.close()

#check if an input is in th towel, then chck if th input is in that new input and so on --> recursion
print(desired_towels)
print(towel_inputs)

#is towel input 1 in position 1 of towel 1:
#first_part_of_towel_1 = desired_towels[0][0:len(towel_inputs[0])]
#print(first_part_of_towel_1)


towel_input_index = 0
def is_towel_input_1_in_first_part_of_towel(towel_input_index,towel):
    if len(towel)>0 and towel_input_index<len(towel_inputs):
        
        print ('towel_cut',towel[0:len(towel_inputs[towel_input_index])])
        if towel[0:len(towel_inputs[towel_input_index])] == towel_inputs[towel_input_index]:
            towel=towel[len(towel_inputs[towel_input_index]):]
            print(towel)
            
            is_towel_input_1_in_first_part_of_towel(towel_input_index,towel)
        else:
            towel_input_index = towel_input_index+1
            is_towel_input_1_in_first_part_of_towel(towel_input_index,towel)

            
    print(towel)
    print('length',len(towel))
    print('index',towel_input_index)

            #try next towel input      

is_towel_input_1_in_first_part_of_towel(towel_input_index,desired_towels[0])

'''

#if first input in first part in towel 1, then we know we can remove that from the beginning of towel
if first_part_of_towel_1 == towel_inputs[0]:
    first_part_of_towel_1 = first_part_of_towel_1[0:len(towel_inputs[0])]
    print(first_part_of_towel_1)

#else try next input in first part of towel 1
else:
    first_part_of_towel_1 = desired_towels[0][0:len(towel_inputs[1])]
    print(first_part_of_towel_1)  

    #if first input in first part in towel 1, then we know we can remove that from the beginning of towel
    if first_part_of_towel_1 == towel_inputs[0]:
        first_part_of_towel_1 = first_part_of_towel_1[0:len(towel_inputs[0])]
        print(first_part_of_towel_1)
    
    else:
        first_part_of_towel_1 = desired_towels[0][0:len(towel_inputs[1])]
        print(first_part_of_towel_1)  


        #repeat until:
            # no more towel inputs to try
            # or
            # no more stripes in towel 




'''
