

def decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    lowercase_message = message.lower()
    decoded_message = ""

    for c in lowercase_message:
        if c in alphabet:
            decoded_message += alphabet[(alphabet.index(c) + offset) % 26]
        else:
            decoded_message += c
    return decoded_message


def coder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    lowercase_message = message.lower()
    encrypted_message = ""

    for c in lowercase_message:
        if c in alphabet:
            encrypted_message += alphabet[(alphabet.index(c) - offset) % 26]
        else:
            encrypted_message += c
    return encrypted_message


first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

first_decoded_message = decoder(first_message, 10)
second_decoded_message = decoder(second_message, 14)

print(first_decoded_message)
print(second_decoded_message)


def vigener_cipher_decoder(message, keyword):
    lower_message = message.lower()
    lower_keyword = keyword.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    decoded_message = ""
    keyword_index = 0
    for c in lower_message:
        if c in alphabet:
            actual_index = (alphabet.index(c) - alphabet.index(keyword[keyword_index])) % 26
            decoded_message += alphabet[actual_index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            decoded_message += c
    return decoded_message


message1 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword1 = "friends"

print(vigener_cipher_decoder(message1, keyword1))


def vigener_cipher_coder(message, keyword):
    lower_message = message.lower()
    lower_keyword = keyword.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted_message = ""
    i = 0
    for c in lower_message:
        if c in alphabet:
            encrypted_message += alphabet[(alphabet.index(keyword[i % len(keyword)]) + alphabet.index(c)) % 26]
            i += 1
        else:
            encrypted_message += c
    return encrypted_message


test_message = "barry is the spy"
test_keyword = "dog"

print(vigener_cipher_coder(test_message, test_keyword))


# empty line