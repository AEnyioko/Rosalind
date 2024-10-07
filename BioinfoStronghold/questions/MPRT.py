"""
Finding a Protein Motif

Given: Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, 
output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""
import urllib.request
import certifi

def motif(file):
    """
    Prints the locations of the N-glycosylation motif 
    """
    # retrieves list of ID's
    with open(file, 'r') as id:

        # creates fasta url to pull protein sequence
        for name in id.readlines():
            seq = ''
            url = 'https://rest.uniprot.org/uniprotkb/' + name.strip()[0:6] + '.fasta' 
            location = []

            # generates readable sequence
            for line in urllib.request.urlopen(url, cafile=certifi.where()):
                if b'>' not in line:
                    seq += line.decode("utf-8").strip()

            # checks for N-glycosylation motif in sequence
            for i in range(len(seq) - 3):
                if (seq[i] == 'N') and (seq[i + 1] != 'P') and (seq[i + 2] == 'S' or seq[i + 2] == 'T') and (seq[i + 3] != 'P'):
                    location.append(i + 1)

            # prints name position of motif
            print(name.strip()) 
            print((str(location)[1:-1]).replace(',', '')) 
    return None
    
motif('RosalindData/rosalind_mprt (6).txt')