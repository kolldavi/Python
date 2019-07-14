import getopt, sys

# - further arguments
argumentList = sys.argv[1:]

print("argumentList",argumentList)

unixOptions = "ho:v"  
gnuOptions = ["help", "output=", "verbose"]  
try:  
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:  
    # output error, and return with an error code
    print ("ERROR:",str(err))
    sys.exit(2)



# evaluate given options
for currentArgument, currentValue in arguments:  
    if currentArgument in ("-v", "-verbose"):
        print (currentArgument," command: enabling verbose mode")
    elif currentArgument in ("-h", "--help"):
        print (currentArgument," command: displaying help")
    elif currentArgument in ("-o", "--output"):
        print (("enabling special output mode (%s)") % (currentValue))