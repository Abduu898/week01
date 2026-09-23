###### Task 1
phrase = "Hello World !";
print(phrase);
###### Task 1.2
print("-------");
print(phrase[0]);
###### Task 1.3
print("-------");
print(phrase[-1]);
###### Task 1.4
print("-------");
print(phrase[4:10:1]);
###### Task 1.5
print("-------");
print(phrase.lower());
###### Task 1.6
print("-------");
phrase =" tutu on the tuki-kata";
result=" "
i=0
while i < len(phrase):
    if phrase[i:i+2]=="tu":
        result+="ta"
        i+=2
    else:
        result+=phrase[i]
        i+=1
       
print(result)

###### Task  1.7
print("-------");
string = "Hello world!"
position = string.find("a")
print(position)

## since thrtr is n a in the string the output will be -1

###### Task 1.8
print("-------");
p = "abcdefghij"
print(p[::-2][:5][::-1][3:])
###### Task 1.9
print("-------");
p ="abcdefghij";
step1=p[::-2]   # take every 2nd char from the end
step2=step1[:5]    # take the first 5 characters
step3=step2[::-1]  # reverse the string
step4=step3[3:]  # take from index 3 to the end
print(step4);


###### Task 1.10
print("-------");

phrase = "Hello World !";
i=0;
while i <10:
    print(phrase);
    i+=1;

###### Task 1.11
print("-------");
## print("hello"+42)
# error cause we are trying to link an interger with a string without conversion



####### Task 3.1
print("-------");
name=input("Enter your name: ")
print("Hello " + name.capitalize()+"!")

######## Task 3.2
print("-------");
T = int(input("Enter a number 1: "))
print(type(T) )

##### Task 3.3
print("-------");
number1= int(input("Enter a number: "))
number2= int(input("Enter a number: "))
print("The sum of the provided numbers is ", number1 + number2)

##### Task 3.4
print("-------");
sentence= input("Enter a String: ")
words= sentence.split()
new_sentence= " "
for i in words:
    new_sentence+= i[0]

print(new_sentence)






    