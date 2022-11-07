import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('enter your text: \n').lower())

shift_number = int(input('enter your shift number from 1 to 25: \n'))

end_program = False

while not end_program:
    # search through the enter text

        for i in range(len(sentence)):
            # get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        # convert the list back to a string
        print("------------encrypted text---------------------------")
        print(''.join(map(str, sentence)))
        # end_program = True
        print("------------------decrypted text---------------------")
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
            # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program=True