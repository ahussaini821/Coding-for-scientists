# Class for holding, reading and writing FASTA sequences
class Sequence:
    def __init__(self, accession_number, sequence):
        
        # List of sequences and accesion number for current file
        self.sequences = sequence
        self.accessions = accession_number
    
    def read(self, file_name):
        fasta = open(file_name, "r")
        lines = fasta.readlines()
        # Necessary as sequences are split on multiple lines
        current_sequence = []

        # Go through current file, appending sequences and accession 
        # numbers into list
        for x in lines:
            if ">" in x:
                
                self.accessions.append(x)
                
                # Necessary as sequences are split on multiple lines
                if len(current_sequence) > 0:
                    self.sequences.append(''.join(current_sequence))
                    current_sequence = []

                

            else:
                current_sequence.append(x)
        
        # Make sure to append last line of sequence
        self.sequences.append(''.join(current_sequence))
        current_sequence = []

        


    def write(self, output_name):
        new_file = open(output_name, "a")
        for i in range(len(self.sequences)):
            new_file.write(self.accessions[i])
            new_file.write(self.sequences[i])
            
done = False
accession_number = []
sequence = []
current_sequence = Sequence(accession_number, sequence)

print("This script is for combining FASTA sequences into one file with"
      " more \nfeatures to come \n")


  

print("To use this program, simply enter filenames of fasta files you" 
      " wish to \ncombine 1 by 1, and simply enter stop when you are done" 
      " inputting files")

            
while not done:
    user_input = raw_input("Enter filename or stop: ")
    
    if user_input == "stop":
        output_name = raw_input("What do you want to call the output" 
                                "file? ")
        current_sequence.write(output_name)
        done = True
    
    else:
        # To make sure file exists
        try:
            current_sequence.read(user_input)
        except:
            print "File does not exist in this directory"