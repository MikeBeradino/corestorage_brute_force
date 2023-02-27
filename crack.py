# This is a good link to find your disk id
# use this command --> diskutil corestorage list
#https://derflounder.wordpress.com/2011/11/23/using-the-command-line-to-unlock-or-decrypt-your-filevault-2-encrypted-boot-drive/

import itertools
import os

counter = 0
seed_dict = {}
no_dups = {""}
index_count = 0
hlon = "\033[7m"
iton = "\033[3m"
choff = "\033[0m"
ulmethods = ['corestorage', 'apfs']
method = ulmethods[0]

save_to_file = input(f'Would you like to save the password variations to pass_vars.txt? Y/{hlon}N{choff}: ') or 'n'
Disk_ID = input("Please give your disk UUID: ")
seed = input("Type your best guess at your password: ")

print(f'Use {hlon}~{choff} to remove spaces: {iton}e.g.{choff}, {hlon}Hello~world{choff} → {hlon}Helloworld{choff}')
for char in seed:    
    possible_chars = str(input(f'Please provide possible characters for {char}: ') or char)
    seed_dict[index_count] = possible_chars
    index_count += 1

List_of_Subs = list(seed_dict.values())
newlist = list(itertools.product(*List_of_Subs))
word_list = [''.join(data) for data in newlist]
wl_length = str(len(word_list))

# write to text file?
if save_to_file.lower() == "y":
    file = open("pass_vars.txt", "w")
    for word in word_list:
        word = word.replace('~', '')
        file.write(f'{word}\n')
    file.close()

for word in word_list:
    word = word.replace('~', '')
    print(f'{counter} --of-- {wl_length}: {word}')
    os.system(f'sudo -s diskutil {method} unlockVolume {Disk_ID} -passphrase {word}')
    counter += 1
