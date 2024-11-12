def average():
    lens = 0
    userInput = 0
    while True:
        userInput += userInput
        userInput = int(input("Masukkan nilai: "))
        lens += 1
        playAgain = input("End? (Yes/No): ").lower()
        
        if playAgain == "yes":
            sum = userInput/lens
            print("Rata-ratanya adalah: ", sum)
            break
        
        elif playAgain == "no":
            continue
        
        else:
            print("Masukkan 'yes' atau 'no'")
            break
                  
average()