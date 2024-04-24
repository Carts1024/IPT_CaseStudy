#Initialize tuple
squared = ()

# Inputs in list
list = [1,2,3]

# List for squared numbers
sq_list = []

# Loop for squaring numbers  
for i in list:
    sq = i * i
    squared = (i,sq)
    # Adding squared numbers tuple to the list 
    sq_list.append(squared)
    del squared

# Print Results
print(sq_list)
