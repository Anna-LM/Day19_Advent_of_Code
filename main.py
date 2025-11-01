#Open file name example.txt
f = open("example.txt")

#read the first line of the file
towel_inputs = (f.readline()).strip('\n')

#format the line into a list of each towel option
towel_inputs=towel_inputs.split(', ')
print(towel_inputs)

desired_towels=[]
#make a list of all the final towel designs
for line in f:
    desired_towels.append((line.strip('\n')))

#remove first element which was blank
desired_towels=desired_towels[1:]

print(desired_towels[1:])
 

#close file
f.close()
