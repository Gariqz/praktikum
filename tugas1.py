def fibonacci ():
    userInput = int(input("Masukkan nilai n (berapa banyak deret fibonacci yang ingin ditampilkan): "))
    if userInput <= 0:
        print("Masukkan nilai n yang lebih besar dari 0!!")
    else:
        a = 0 # first value sets to 0 (start from 0)
        b = 1 # the second value
        for i in range(userInput): # looping n times based user input
            print(a, end=" ")
            a, b = b, a + b

fibonacci()