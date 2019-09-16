#Practicing string manipulation and loops
#hello 

pronouncedWord = input("Please enter a Hawaiian word to pronounce:")
repeatFlag = True
validFlag = True
validCharacters = "aeioupkhlmnw '"
vowels = "aeiou"
consonants = "pkhlmn"
vowelGroup = ("ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui")

while validFlag == True:
    for letter in pronouncedWord:
        if letter.lower() not in validCharacters:
            pronouncedWord = input("Your word contains invalid characters. Please enter a Hawaiian word to pronounce:")
        else:
            validFlag = False

while repeatFlag == True:
    phoneticSpelling = ""

    for letter in range(0, len(pronouncedWord)):
        #Does the letter belong to the consonant family
        if pronouncedWord[letter].lower() in consonants:
            phoneticSpelling += pronouncedWord[letter]
        #Does the letter special 'w'
        elif pronouncedWord[letter].lower() == "w":
            if letter == 0:
                phoneticSpelling += pronouncedWord[letter]
            elif pronouncedWord[letter-1] in ( "auo"):
                phoneticSpelling += pronouncedWord[letter]
            elif pronouncedWord[letter-1] in ("ie"):
                phoneticSpelling += "v"
        elif pronouncedWord[letter].lower() in vowels:
            if letter < len(pronouncedWord)-2:
                if pronouncedWord[letter]+pronouncedWord[letter+1]in vowelGroup and pronouncedWord[letter+1]+pronouncedWord[letter+2]in vowelGroup:
                    if pronouncedWord[letter]+pronouncedWord[letter+1] in ("ai","ae"):
                        phoneticSpelling += "eye-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ao", "au"):
                        phoneticSpelling += "ow-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ei"):
                        phoneticSpelling += "ay-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("eu"):
                        phoneticSpelling += "eh-oo"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("iu"):
                        phoneticSpelling += "ew-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("oi"):
                        phoneticSpelling += "oy-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ou"):
                        phoneticSpelling += "ow-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ui"):
                        phoneticSpelling += "ooey-"
                    if pronouncedWord[letter+2] == "a":
                        phoneticSpelling += "ah-"
                    elif pronouncedWord[letter+2] == "e":
                        phoneticSpelling += "eh-"
                    elif pronouncedWord[letter+2] == "i":
                        phoneticSpelling += "ee-"
                    elif pronouncedWord[letter+2] == "o":
                        phoneticSpelling += "oh-"
                    elif pronouncedWord[letter+2] == "u":
                        phoneticSpelling += "oo-"
                elif pronouncedWord[letter]+pronouncedWord[letter+1]in vowelGroup:
                    if pronouncedWord[letter]+pronouncedWord[letter+1] in ("ai","ae"):
                        phoneticSpelling += "eye-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ao", "au"):
                        phoneticSpelling += "ow-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ei"):
                        phoneticSpelling += "ay-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("eu"):
                        phoneticSpelling += "eh-oo"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("iu"):
                        phoneticSpelling += "ew-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("oi"):
                        phoneticSpelling += "oy-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ou"):
                        phoneticSpelling += "ow-"
                    elif pronouncedWord[letter]+pronouncedWord[letter+1] in ("ui"):
                        phoneticSpelling += "ooey-"
                else:
                    if pronouncedWord[letter] == "a":
                        phoneticSpelling += "ah-"
                    elif pronouncedWord[letter] == "e":
                        phoneticSpelling += "eh-"
                    elif pronouncedWord[letter] == "i":
                        phoneticSpelling += "ee-"
                    elif pronouncedWord[letter] == "o":
                        phoneticSpelling += "oh-"
                    elif pronouncedWord[letter] == "u":
                        phoneticSpelling += "oo-"
            elif letter == len(pronouncedWord)-1 and pronouncedWord[letter-1] not in vowels:
                if pronouncedWord[letter] == "a":
                    phoneticSpelling += "ah"
                elif pronouncedWord[letter] == "e":
                    phoneticSpelling += "eh"
                elif pronouncedWord[letter] == "i":
                    phoneticSpelling += "ee"
                elif pronouncedWord[letter] == "o":
                    phoneticSpelling += "oh"
                elif pronouncedWord[letter] == "u":
                    phoneticSpelling += "oo"
        elif pronouncedWord[letter] in (" ", "'"):
            phoneticSpelling += pronouncedWord[letter]

    print(pronouncedWord + " is pronounced " + phoneticSpelling)
    print()

    tryAgain = input("Do you want to enter another word? Y/YES/N/NO")

    if tryAgain.upper() in ("YYES"):
        #continue
        phoneticSpelling = ""
        pronouncedWord = input("Please enter a Hawaiian word to pronounce:")
        repeatFlag = True
    else:
        repeatFlag = False

