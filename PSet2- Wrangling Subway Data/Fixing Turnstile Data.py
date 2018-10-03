import csv
import pandas as pd
def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        # create new file to write t
         i = name.index(".")
         new_name = name[:i]
         new = "updated_" + new_name + ".txt"
        
         with open(name, "r") as f_old, open(new, "w+") as f_new:    
                reader = csv.reader(f_old)
                writer = csv.writer(f_new)
                for row in reader:
                   #row is a list. Turn into an array
                    row = [i.split('\t')[0] for i in row] 
                    header = row[:3]
                    #1st row with new header
                    writer.writerow(row[:8])
                    #rest of row is row now
                    row = row[8:]
                    for r in range(0, len(row),5):
                        writer.writerow(header+row[r:r+5])
                        
                   
                     
