

def encrypt (text,shift):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded_list = []  
    
    for i in text:
          
        index_char = alphabet.index(i)
        print(index_char)
            
        #sliced_char = alphabet[index_char + shift :  : shift]
        #print("The shifted character is : " + sliced_char[0])
         
        if (index_char + shift) > len(alphabet):
            encoded_list.append(alphabet[(index_char + shift) - len(alphabet) ])

        else:     
           
            encoded_list.append(alphabet[index_char + shift])
            print("The encoded character list is : " )
            print(encoded_list)
            
        
        encoded_string = ''.join(encoded_list)
        print("Your encoded text is :" + encoded_string)
     


def decrypt (text,shift):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded_list = []  
    
    for i in text:
          
        index_char = alphabet.index(i)
        print(index_char)
            
        if (index_char - shift)<0:
            decoded_list.append(alphabet[len(alphabet) - (shift- index_char)])
        else:     
           
            decoded_list.append(alphabet[index_char - shift])
            print("The Decoded character list is : " )
            print(decoded_list)
            
        
        decoded_string = ''.join(decoded_list)
        print("Your Decoded text is :" + decoded_string)
     

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


  # What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    if direction == "encode":
      encrypt(text,shift)
    else:
        decrypt(text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
        

    
    



