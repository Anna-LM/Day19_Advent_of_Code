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


# Method 1: *** This method is designed more for if there is finite number of stripes, not indefinate. ***
# order towel compomnents by size. try and fit in the longer components in first. 
# order desired towel lengths. see how many characters is left in each desired towel design. fill from shortest. 
'''
#order towel inputs by lengths
towel_inputs = sorted(towel_inputs, key=len, reverse=True)

#see if the stripe pattern fits into a desired towel size
for final_towel in desired_towels:

    used_stripes=[]
    #iterate through all the towel stripe patters, see if first in shorest towel pattern
    for stripe_input in towel_inputs:
        
        # if the stripe is a substring of the desired towel
        if stripe_input in final_towel:
            
            #remove the stripe from final towel design
            final_towel = final_towel.replace(stripe_input, "")
            
            #record which stripes were used
            used_stripes.append(stripe_input)

    if final_towel.strip('')== '':
        complete_towel_counter=complete_towel_counter+1
        
        #only if the towel was completed remove the stripes from the list of stripes
        #remove the stripe from the list of stripes
        towel_inputs.remove(stripe_input)

'''    

# Method 2: *** indefinate number of each stripe available ***
# i was noticing in the previous method that the remaining stripes in the incomplete towels were ones where there was not that individual stripe. so i am going to readjust my method, and start by noting which individual stripes were not available. then for each towel that involved a stripe of that colour, working backwards and seeing if theres a stripe substring including that letter and the one either side in the desired towel, and then two either side etc. 
# 1. compare all possible stripes with stripe list from input, see which indicidual colours not included
# 2. for each desired towel if it includes the indivdal stripe colour not included in the input, then check, if not we know it can be achieved
# 3. check stripe options for desired towel: unincluded stripe colour +/- 1 stripe colour, then +/-2, 
# * for efficiency, remove any of the towel stripe options that dont include the non-included colour, and remove any towels from desired towels that dont included non-included colour.


print(complete_towel_counter)
    
