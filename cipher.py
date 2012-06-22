
phrase=raw_input('Enter sentence to encrypt')

shift_value=input('Enter shift value')

encoded_phrase=''
encoded_phrase2=''

for c in phrase:
    asciiv=ord(c)
    asciir=asciiv +int(shift_value)
    
    if c.isalpha():
        if c.islower():
            #encoded_phrase = encoded_phrase + 'x'
        
            
            
            if asciir>122:
               asciib=asciir-123 +97
               asciishift=chr(asciib )
               
               encoded_phrase= encoded_phrase + asciishift
            else:
                asciishift=chr(asciir)
                encoded_phrase= encoded_phrase + asciishift
        elif c.isupper():
            #encoded_phrase = encoded_phrase + 'X'
            if asciir>90:
               asciid=asciir-91 +65
               asciishift=chr(asciid )
               encoded_phrase= encoded_phrase + asciishift
            else:
                asciishift=chr(asciir )
                encoded_phrase= encoded_phrase + asciishift
            
    elif c.isdigit():
        asciishift=chr(asciiv + shift_value)
        asciishift=int(asciishift)
        asciishift=(asciishift%6)
        encoded_phrase= encoded_phrase + str(asciishift)
        
    else:
        encoded_phrase = encoded_phrase + c
       
print encoded_phrase, 








     
