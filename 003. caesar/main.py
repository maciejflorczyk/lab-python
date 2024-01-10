import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Ma pytać czy zakończyć program.
#TODO-2: Ma umieć sobie poradzić z sytuacją kiedy shift > niż liter w alfabecie.
#TODO-3: Ma zostawić liczby, symbole i spacje nienaruszone.
end_program = False


def ceasar(text,shift,direction):

    end_text = []
    if direction == 'decode':
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)

            end_text += alphabet[new_position]
        else:
            end_text += char
    print("--------------------------------------")
    print("".join(end_text))
    print("--------------------------------------")

while end_program == False:
    print(art.logo)
    print("--------------------------------------")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    ceasar(text=text,shift=shift,direction=direction)

    if input("Do you want to end the program? y or n? ") == "y":
        end_program = True
    else:
        end_program = False
