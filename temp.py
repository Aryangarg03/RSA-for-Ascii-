import time
def gcd(m,n): 
    if n==0: 
        return m 
    else: 
        return gcd(n,m%n) 

def encrypt(ascii_initial, e, n):
    ascii_final = []
    for i in ascii_initial:
        C1= pow(i,e)
        C=C1%n
#         print("value of C is:",C)  
        ascii_final.append(C)
    return ascii_final

def decrypt(ascii_initial, d, n):
    from joblib import Parallel, delayed
    # ascii_final2 = []
    ascii_final = Parallel(n_jobs=-1)(delayed(pow)(j,d,n) for j in ascii_initial)
    # for j in ascii_final:
    # # #decryption
    # #     P1=pow(j,d)
    #      P=j%n
        #  ascii_final2.append(P)
    #     print("value of P is:",P)
#     print(ascii_final2)
    return ascii_final   
def rsa_algorithm (direction, ascii_initial):
    p,q,r,s = 13, 17, 61, 37
    

    n= p*q*r*s
#     print("RSA Modulus(n) is:",n)

    # pub_key = int(input("Enter a starting value for public key generation "))
    f_of_n = (p - 1) * (q - 1) * (r-1) * (s-1)
    # print("Eulers Toitent(r) is:",f_of_n)
    #gcd
    for e in range(2,f_of_n): 
        if gcd(e,f_of_n)== 1: 
            break

    for i in range (1,f_of_n):
        d= 1+f_of_n *i/e
        if d % e==0:
            d = int(d/e) 
            break

#     print("value of d is:",d)  

    #public key generation

    # decalaring empty list
    # ascii_final = []
    #Cypher text=Encryption
    #checking whether to encode or decode

    if direction =="encode":
        ascii_final =  encrypt(ascii_initial,e,n)

    tic = time.time()
    if direction == "decode":
        ascii_final = decrypt(ascii_initial, d, n)
    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))
    return ascii_final
cont = 'yes'
while cont.lower() == 'yes':
#checking whether user wants encoding or decoding
    u_direction=input("Type 'encode' for encrypting and 'decode' for decrypting: ")
    if u_direction == 'encode':        
        user_entered_string = input(f"Enter the String to be {u_direction}d: ")
        user_entered_string = user_entered_string
        #converting into the ascii code dec
        ascii = []
        for letter in user_entered_string:
            ascii.append(ord(letter))
        # encoprint(ascii)
        #calling our rsa_algorithm function
        resultant_ascii = rsa_algorithm(u_direction,ascii)

        print(f"*********your encode ascii list is *******\n{resultant_ascii}")

    if u_direction == 'decode':
        input_string = input('Enter elements of a list separated by and , space: ')
        print("\n")
        ascii = input_string.split(', ')
        # print list
#         print('list: ', ascii)

        # convert each item to int type
        for i in range(len(ascii)):
            # convert each item to int type
            ascii[i] = int(float(ascii[i]))

        resultant_ascii = []
        resultant_ascii = (rsa_algorithm(u_direction,ascii))
#         print(resultant_ascii)

        s = ''.join(chr(i) for i in resultant_ascii)
        print(s)
    cont = input("Do you want to continue type 'yes' to continue or 'no' to stop: ")