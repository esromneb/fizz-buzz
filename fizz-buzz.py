for i in range(1,100):
    output = ""

    if( i % 3 == 0 ):
        output += "Fizz"

    if( i % 5 == 0 ):
        output += "Buzz"

    print ( output == "" ) and i or output