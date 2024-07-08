import cv2
import string
import os
d={}
c={}
#print{"Hi"}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

#print(c)
image_path=r"C:\Users\RAHUL VARMA\OneDrive\Desktop\Cyberproject\Turtle.webp"
x=cv2.imread(image_path)

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter key to edit(SecurityKey) : ") #key
text=input("ENter text to hide : ") #secret message

k1=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of coloumn

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[k1]]
    n=n+1
    m=m+1
    m=(m+1)%3   #this is for every value of z,remainder will be between 0,1,2, i.e G,R,B plane wiil be set automatically
    k1=(k1+1)%len(key)    #whatever be the value of z,z-(z+1)%3 will always between 0,1,2 . the same concept is used for random number in dice and card games

encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
cv2.imwrite(encrypted_image_path,x)
os.startfile(encrypted_image_path)
print("Data Hiding in Image Completed Successfully.")
#x=cv2.imread("encrypted_img.jpg")

k1=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of coloumn
ch=int(input("\nENter 1 to extract data from image : "))
if ch==1:
    key1=input("\n\nRe enter key to extract text : ")
    decrypt=""
    if key==key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[k1]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            k1=(k1+1)%len(key)
        print("Encrypted text was : ",decrypt)
    else:
        print("Key doesn't matched.")
else:
    print("Thank you. Bye. ")
    