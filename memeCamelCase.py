'''
This program reads text from a file and proceeds to alternate the text written on that file
This program is also very retarded...
'''

infile = open('Infile.txt', 'r')
outfile = open('Output.txt', 'w')
case = 1
message = infile.read()
output = ''

for lines in message:
    if case == 1 and lines != ' ':
        output += lines.upper()
        case = 0
    elif case == 0 and lines != ' ':
        output += lines.lower()
        case = 1
    else:
        output += ' '

outfile.write(output)

print('Task complete, closing files...')

infile.close()
outfile.close()