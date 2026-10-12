"""
Author: Jacob Miletti

This dictionary maps each Base32 digit to the octal representation of its value.

"""

base32ToOctalTable = { "0": "0", "1": "1", "2": "2", "3": "3",
                       "4": "4", "5": "5", "6": "6", "7": "7",
                       "8": "10", "9": "11", "A": "12", "B": "13",
                       "C": "14", "D": "15", "E": "16", "F": "17",
                       "G": "20", "H": "21", "I": "22", "J": "23",
                       "K": "24", "L": "25", "M": "26", "N": "27",
                       "O": "30", "P": "31", "Q": "32", "R": "33",
                       "S": "34", "T": "35", "U": "36", "V": "37" }

userInput = input("Enter a Base32 number: ")
if userInput in base32ToOctalTable:
    def convertBase32ToOctal(base32):
        """Takes a base32 number and returns its octal representation."""
        octal = ""
        for digit in base32:
            octal += base32ToOctalTable[digit]
        return octal
    print("The Octal number is: " + convertBase32ToOctal(userInput))
else: 
    print("Invalid Base32 number. Please enter a valid Base32 digit (0-9, A-V).")
