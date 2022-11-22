ask=input("Do you wish to encrypt or decrypt a message")


if ask=="encrypt":
    key=int(input("Enter the key number"))
    def encrypt(message,key):
        string=""
        message=message.lower()
        for i in message:
            if ord(i)+key>ord("z"):#121+3=124
                step1=ord("z")-ord(i)
                step2=ord("a")+(key-step1-1)
                string+=chr(step2)
            else:
                string+=chr(ord(i)+key)
        for x in string:
            check=x.isalpha()
            if check==False:
                string=string.replace(x," ")
        return(string)
elif ask=="decrypt":
    key=int(input("Enter the key number"))
    def decrypt(message,key):
        message=message.lower()
        string=""
        for i in message:
            if ord(i)-key<ord("a"):
                step1=ord("a")-(ord(i)-key)
                step2=ord("z")-(step1-1)
                string+=chr(step2)
            else:
                string+=(chr(ord(i)-key))
        for x in string:
            check=x.isalpha()
            if check==False:
                string=string.replace(x," ")
        return(string)

        

            

message=input("Enter your message")

if ask=="encrypt":
    print(encrypt(message,key))
elif ask=="decrypt":
    print(decrypt(message,key))




