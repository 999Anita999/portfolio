import pandas as pd

morse = pd.read_csv('morse_code.csv')


def generate_code():
    direction = input("Encode or Decode? ").lower()
    use_cut = input("Use cut or full? ").lower()
    message = input("Enter a message: ").lower()
    try:
        if direction == 'encode':
            output = [morse["morse_code"][(morse["letter"] == letter) & (morse["type"] == use_cut)].values[0] + ' ' for
                      letter in message]
            output_message = ''.join(output)
        else:
            message_list = []
            morse_letter = ""
            message_length = len(message)
            letter_index = 1
            for letter in message:
                if letter == '/':
                    morse_letter = "/"
                elif letter == ' ':
                    message_list.append(morse_letter)
                    morse_letter = ""
                elif letter_index == message_length:
                    morse_letter += letter
                    message_list.append(morse_letter)
                else:
                    morse_letter += letter
                letter_index += 1
            output = [morse["letter"][(morse["morse_code"] == letter) & (morse["type"] == use_cut)].values[0] for letter
                      in message_list]
            output_message = ''.join(output)
    except IndexError as message:
        print(f"Sorry,you have used characters that I haven't added to the encoder/decoder.")
        generate_code()
    else:
        print(output_message)
        return True


generate_code()
