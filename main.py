#Open file name example.txt
f = open("example.txt")

#read the first line of the file
towel_inputs = (f.readline())

#format the line into a list of each towel option
towel_inputs=towel_inputs.split(', ')
print(towel_inputs)

#close file
f.close()
