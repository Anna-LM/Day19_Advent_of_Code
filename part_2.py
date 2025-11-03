from functools import cache## -- Read input texts into useful formats --

## -- Read input texts into useful formats --

#Open file name example.txt
f = open("samdesk_puzzle_input.txt")

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

#print(desired_towels)
#print(towel_inputs)

#check if an input is in the towel, then check if the input is in that new input and so on --> recursion

@cache

def is_towel_input_n_in_next_part_of_desired_towel(desired_towel):

    #repeat until:
    # no more towel inputs to try
    # or
    # no more stripes in towel 
    
    # if theres no stripes left in towel, the towel has been completed, thats 1 way to be completed
    if not desired_towel:
        return 1
    
    #for each loop of the recurrsion, add a counter
    recurrsion_counter = 0

    #try each towel input for the first/next part of the of the current desired towel
    for towel_input in towel_inputs:
        #if the first part of the input equals the current towel input, then try the rest of the towel input
        first_part_of_towel_n = desired_towel[0:len(towel_input)]
        if first_part_of_towel_n == towel_input:  
            #keep the recursion going, increase recurrsion_counter
            rest_of_towel_n= desired_towel[len(towel_input):]
            recurrsion_counter = recurrsion_counter+ is_towel_input_n_in_next_part_of_desired_towel(rest_of_towel_n)

    #if the towel cant be made the recussion counter will be 0 from the beginning of th recurssion loop
    return recurrsion_counter
            

#count how many complete towels, for each towel tried, and returned true, increase counter
complete_towel_counter = 0
for desired_towel in desired_towels:
    if is_towel_input_n_in_next_part_of_desired_towel(desired_towel):
        complete_towel_counter = complete_towel_counter+ 1

print('number of complete towels:',complete_towel_counter)
     
#add up how many times the recurrsion occurs that the towel completes
total_number_of_designs_counter = 0
for desired_towel in desired_towels:
    total_number_of_designs_counter = total_number_of_designs_counter+is_towel_input_n_in_next_part_of_desired_towel(desired_towel)

print('number of ways to complete:',total_number_of_designs_counter)