import sys #Imports sys, the library containing the argv function
the_string=str(sys.argv[1]) #The string to repeat is the first argument given.
target_number_of_repeats=int(sys.argv[2]) #The number of repeats is the second argument given.
number_of_repeats=0 #Set this variable to zero, as there are no repeats at the start of program.
while (number_of_repeats<target_number_of_repeats):#Until the statement in the brackets is false.
    print (the_string) #Output the string, again. (This section must be indented!)
    number_of_repeats=number_of_repeats+1 #Add 1 to the number of repeats.
