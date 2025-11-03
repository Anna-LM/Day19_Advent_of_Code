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




## -- Create Towel designs --
complete_towel_counter  = 0



print(desired_towels)
print(towel_inputs)
possible_individual_stripes =  ['w','u','b','r','g']
print()
# remove desired towels and input stripes that can be made up of individul stripe inputs

individual_stripes_not_included=[]

for colour in possible_individual_stripes:
    if colour not in towel_inputs:
        individual_stripes_not_included.append(colour)
print(individual_stripes_not_included)
