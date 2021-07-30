# author: Lyric Marner
# date: July 29, 2021

# difficulty: easy

# Wikipedia: https://en.wikipedia.org/wiki/Atbash
#   Read this for a better understanding of the cipher.

# Introduction
#
# Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#
# The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such
#   that the resulting alphabet is backwards. The first letter is replaced with the last letter,
#   the second with the second-last, and so on.
#
# An Atbash cipher for the Latin alphabet would be as follows:
#
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: zyxwvutsrqponmlkjihgfedcba
#
# It is a very weak cipher because it only has one possible key, and it is a simple monoalphabetic substitution
#   cipher. However, this may not have been an issue in the cipher's time.
#
# Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, and
#   punctuation is excluded. This is to make it harder to guess things based on word boundaries.
#
# Examples
#
#     Encoding test gives gvhg
#     Decoding gvhg gives test
#     Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog
#
#
# Program Requirements:
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - Convert the plain text into cipher text using the atbash cipher.
#   3 - Print the result to the user.
#
# HINTS:
#   1 - It may be helpful to tell the program what the plain alphabet is, as well as the cipher.
#   2 - Remember that lists can be built up, meaning it may be useful to start with an empty list.
#
# WRITE DOWN THE STEPS BEFORE ATTEMPTING THE PROGRAM
# Step 1: Write down the normal alphabet and the cipher alphabet. 
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz.,!?:\/;"\' 1234567890'
lower_cipher_alphabet = lower_alphabet[::-1]

upper_alphabet = lower_alphabet.upper()
upper_cipher_alphabet = lower_cipher_alphabet.upper()

plain_text = input('Enter a word or phrase: ')

cipher_text = ''

for i in plain_text:
    if i in lower_alphabet:
        position = lower_alphabet.find(i)
        ciph_value = lower_cipher_alphabet[position]
        cipher_text += ciph_value

    else:
        position = upper_alphabet.find(i)
        ciph_value = upper_cipher_alphabet[position]
        cipher_text += ciph_value
    
print('Original Text: ', plain_text)
print('Cipher Text: ', cipher_text)
