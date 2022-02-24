# This is a good link to find your disk id
# use this command --> diskutil corestorage list
#https://derflounder.wordpress.com/2011/11/23/using-the-command-line-to-unlock-or-decrypt-your-filevault-2-encrypted-boot-drive/

import itertools
import os

counter = 0
save_to_file = input("Would you like to save the password variations to a file? Y/N ")
Disk_ID = input("Please give your disk UUID ")
seed = input("Type your best guess at your password. ")

seed_dict ={}
no_dups={""}
index_count =0
for char in seed:    
    possable_chars = str(input("Please provide possable characters for"+" "+ char+" "))
    seed_dict[index_count]= possable_chars
    index_count = index_count +1

List_of_Subs = list(seed_dict.values())
newlist =list(itertools.product(*List_of_Subs))
word_list = [''.join(data) for data in newlist]


if save_to_file == "Y" or save_to_file == "y":
# wright to text file?
    file = open("pass_vars.txt", "w")
    for word in word_list:
        #print(word)
        file.write(word + '\n')
    file.close()
for word in word_list:
    print(word)
    print(counter ,"--of--", str(len(word_list)))
    os.system("sudo -s diskutil corestorage  unlockVolume "+Disk_ID+" -passphrase "+word)
    counter=counter+1