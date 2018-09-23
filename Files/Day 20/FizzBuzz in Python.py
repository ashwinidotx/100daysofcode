def fizzbuzz(n):

    for i in range(1, n+1):
        x = ""
        if(i % 3 == 0):
            x += "fizz"
        if(i % 5 == 0):
            x += "buzz"
        if(x == ""):
            x = i
        print(x)


inp = int(input("Enter Range"))
fizzbuzz(inp)
