
def encrypt(str):
    new = []
    for i in str:
        a=ord(i)+1
        a=a<<1
        # a=str(bin(i))[2:] 
        a = "{0:b}".format(a)
        new.append(a)
    return new    
def decrypt(encrypt):
    foo =""
    for i in encrypt:
        a = int(i,2)
        a=ord(chr(a))-1
        a = a >> 1
        foo = foo + chr(a)
        # foo.append(a)
    return (foo)  
def main():
   while(True): 
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        str = input("Enter string to encrypt: ")
        print(encrypt(str))
    elif ch==2:
        str = encrypt(str)
        print(decrypt(str))
    else:
        break
main()
   
  