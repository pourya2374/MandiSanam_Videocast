import os
import re


# get filenames from directory
dir = './emails'
for temp in os.walk(dir):
    filenames = temp[2]

# read files and extract emails
emails = list()
regex = r"<(\S+@\S+\.\S+)>"
for filename in filenames:
    file = open(dir + '/' + filename, 'r').read()
    matches = re.finditer(regex, file)
    for match in matches:
        emails.append(match.groups()[0])

print(emails)
output_file = open('email.txt', 'w')
for email in emails:
    output_file.write(email + '\n')
