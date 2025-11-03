from functools import cache## -- Read input texts into useful formats --

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

print(desired_towels)
print(towel_inputs)

#check if an input is in the towel, then check if the input is in that new input and so on --> recursion

@cache

def is_towel_input_n_in_next_part_of_desired_towel(desired_towel):

    #repeat until:
    # no more towel inputs to try
    # or
    # no more stripes in towel 
    
    # if theres no stripes left in towel, the towel has been completed
    if not desired_towel:
        return True
    
    #try each towel input for the first/next part of the of the current desired towel
    for towel_input in towel_inputs:
        #if the first part of the input equals the current towel input, then try the rest of the towel input
        first_part_of_towel_n = desired_towel[0:len(towel_input)]
        if first_part_of_towel_n == towel_input:  
            #keep the recursion going
            rest_of_towel_n= desired_towel[len(towel_input):]
            if is_towel_input_n_in_next_part_of_desired_towel(rest_of_towel_n):
                return True
            
    #if every towel input is tried and the remaining stripes/next stripes of the towel doesnt equal an input, it cant be made
    return False

#count how many complete towels, for each towel tried, and returned true, increase counter
complete_towel_counter = 0
for desired_towel in desired_towels:
    if is_towel_input_n_in_next_part_of_desired_towel(desired_towel):
        complete_towel_counter = complete_towel_counter+ 1

print(complete_towel_counter)
     

