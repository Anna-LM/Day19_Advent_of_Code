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

# Method:
# order towel compomnents by size. try and fit in the longer components in first. 
# order desired towel lengths. see how many characters is left in each desired towel design. fill from shortest. 


#order towel inputs by lengths
towel_inputs = sorted(towel_inputs, key=len, reverse=True)
print(towel_inputs)

#order desired towels by length
desired_towels = sorted(desired_towels, key=len)
print(desired_towels)

#see if the stripe pattern fits into a desired towel size
for final_towel in desired_towels:
    #iterate through all the towel stripe patters, see if first in shorest towel pattern
    for stripe_input in towel_inputs:

        # if the stripe is a substring of the desired towel
        if stripe_input in final_towel:
            print(stripe_input)
            print(final_towel)
            
            #remove the stripe from the list of stripes
            print(towel_inputs)
            towel_inputs.remove(stripe_input)
    #exit that iteration to next stripe substring
    
    
