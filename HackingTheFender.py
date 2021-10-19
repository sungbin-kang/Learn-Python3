# The Fender, a notorious computer hacker and general villain of the people,
# has compromised several top-secret passwords including your own. Your
# mission, should you choose to accept it, is threefold. You must acquire
# access to The Fender‘s systems, you must update his "passwords.txt" file
# to scramble the secret data. The last thing you need to do is add the
# signature of Slash Null, a different hacker whose nefarious deeds could be
# very conveniently halted by The Fender if they viewed Slash Null as a threat.

import csv
import json

# Reading In The Passwords

compromised_users = []

with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)

    for password_row in password_csv:
        compromised_users.append(password_row["Username"])
        # print(password_row["Username"])

with open("compromised_users.txt", "w") as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)

# Notifying the Boss
boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}

with open("boss_message.json", "w") as boss_message:
    json.dump(boss_message_dict, boss_message)

# Scrambling the Password

slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open("new_passwords.cvs", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)

# empty line
