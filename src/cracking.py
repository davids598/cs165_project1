import crypt
import itertools

def main():
    #testInput = "xycavn"
    #testSalt = "hfT7jp2q"
    #hashedPassword = "omJxtlgWN1scUoPZjBMZl1"
    #hash = crypt.crypt(testInput, "$1$" + testSalt)
    #print(hash)
    
    salt = "5HyLUwPA"
    hashedPassword = "RsiTjvvH6ryOLxPch/Clx."

    #Generate inputs
    #print(list(itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
    #print(list(itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2)))
    inputs1 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    inputs2 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2) 
    inputs3 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3) 
    inputs4 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)
    inputs5 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=5)
    inputs6 = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=6)

    totalInputsTemp = [inputs1, inputs2, inputs3, inputs4, inputs5, inputs6]

    totalInputs = list(itertools.chain(*totalInputsTemp))


    for inputSet in totalInputs:
        print(inputSet)
        for password in inputSet:
            print(password)
            #print(password[0])
            hash = crypt.crypt(password, "$1$" + salt)
            if hash == hashedPassword:
                print("Password found, the password is:", password)
                break
    

if __name__ == '__main__':
    main()