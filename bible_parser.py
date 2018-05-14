# Creates a dictionary to hold. the. entire. bible. 

bible = {}

# Opens (and later closes) the bible file. 

with open('kjv.atv') as bible_file:

    # Goes line by line through the bible file,
    # splitting the lines into books, chapters, verse numbers, and verse text. 

    for line in bible_file:

        # Strips white space from beginning in end

        line = line.strip()

        # Bible is written in the following format: Ge@1:1@In the beginning God created the heaven and the earth
        # Therefore, the text can be split at the @ symbol and each part is put into a list.

        parts = line.split('@')

        # Assigns the book to the first term in the parts list (where the broken down line is stored).

        book = parts[0]
        
        # Stores the reference, which contains chapter and verse, in reference.

        reference = parts[1]

        # Chapter and verse are separated by a :. This splits the string into two parts, chapter and verse. 

        parts_ref = reference.split(':')

        # Chapter is assigned to the integer version of the first section in the parts_ref list
            
        chapter = int(parts_ref[0])
        
        # Verse is second part of parts_ref list
            
        verse = int(parts_ref[1])
        
        # Finally, the verse is the 3rd part of the list parts...
            
        verse_text = parts[2]
            

        # Checks to see if the book is in the dictionary bible. If not, it adds the book to bible. 

        if book in bible:
           
            # Assigns book chapters to the list corresponding to the key value in bible with the key book. This allows us to add verses to those already contained in the book chapter.
        
            book_chapters = bible[book]

        else:

            book_chapters = list()

            bible[book] = book_chapters

        if len(book_chapters) >= chapter:

            book_chapters[chapter - 1].append(verse_text)

        else:
            
            # Adds a list entry to the list book_chapters. The list entered has only one entry, but represents a place to put all the verses in that chapter. 
            
            book_chapters.append([verse_text])
            
for book in bible:
    
    for chapter in bible[book]:
        
        for verse in chapter:
            
            print verse

book = raw_input('Enter a book of the bible: ')

book_chapters = bible[book]

num_chapters = len(book_chapters)

chapter = raw_input('Enter the desired chapter [1 - %d]: ' % (num_chapters))

chapter = int(chapter) - 1

num_verses = len(book_chapters[chapter])

verse = raw_input('Enter the desired verse [1 - %d]: ' % (num_verses))

verse = int(verse) - 1
    
print bible[book][chapter][verse]

fewest_chapters = len(bible['Ge'])

book_with_fewest_chapters = len(bible['Ge'])

