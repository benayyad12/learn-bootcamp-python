alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' or 'decode':\n")
# text = input("Original text:\n")
# shift = int(input("type the shift number:\n"))

def encrypt(text,shift):
    result=""
    for letter in text:
        index_cipher=alphabet.index(letter)+shift
        result+=alphabet[index_cipher%26]
    print(result)

def decrypt(text,shift):
    result=""
    for letter in text:
        index_original=alphabet.index(letter)-shift
        result+=alphabet[index_original%26]
    print(result)


def caesar_cipher(text,shift,encode_or_decode):
        result=""
        for letter in text:
            if encode_or_decode=='encode':
                index_cipher=alphabet.index(letter)+shift
            elif encode_or_decode=='decode':
                index_cipher=alphabet.index(letter)-shift

            result+=alphabet[index_cipher%26]
        print(result)

caesar_cipher("ifmmp",1,'decode')

# to skip space/special chars...
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        elif letter not in alphabet:
            output_text+=letter
        elif letter==' ':
            output_text+=' '
    print(f"Here is the {encode_or_decode}d result: {output_text}")
