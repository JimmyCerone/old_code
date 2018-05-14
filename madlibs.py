# This code allows you to play MadLibs on your computer!

# The first part of the code makes the user type in a file name containing the MadLib into the command line...

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file', required = True, help = 'Choose a file for your MadLib...')

arguments = parser.parse_args()

files = arguments.file

# Output creates an empty place to put our output later. 

output = ""

# Now we are finished with setup code... Here is the real meat!

# with allows files to be both opened and closed without having to enter open and close commands. 

# Here we open the files in the variable files and refer to the contents as templateFile

with open(files) as templateFile:
    
    # To allow for 'smarter' game play, where words the user has entered can be used more than once, we declare a dictionary. 

    placeholders = dict()
    
    # Now we break up the templateFile data into line and words! We can then check the words to see if the user can mess with them, 
    # and if so, ask the user what their madlib would like to be!
    
    for line in templateFile:
        line = line.strip();
        words = line.split(" ")
        
        #This part looks through line, word by word. If it sees < and >, it prompts the user for whatever is betweent he < and >. 
        
        for word in words:
            
            if word[0] == '<' and word[-1] == ">":
                
                # This little part removes the underscores
                
                type_of_word = word[1:-1].replace('_', ' ')
                
                # Now we check to see if the value is already stored in the dictionary. 
                
                if not type_of_word in placeholders or not type_of_word[-1].isdigit():
                    
                    placeholder_value = raw_input('\nEnter a %s: ' % (type_of_word))
                    placeholders[type_of_word] = placeholder_value
                
                else:
                    placeholder_value = placeholders[type_of_word]
                
                output = output + " " + placeholder_value
            else:
                output = output + " " + word
                
        output = output + '\n\n'       
                
print '\n' + output