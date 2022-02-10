import urllib
import csv

def retrieve_data(url, fname):
    """
    Retrieve a file from the specified url and save it in a local file 
    called fname.
    """
    
    # grab the data and parse it
    filedata = urllib.request.urlopen(url) 
    to_write = filedata.read()
    
    # write to file
    with open(fname, "wb") as f:
        f.write(to_write)

        
def read_data(path):
    """
    read downloaded data from a .csv file, and return a list of tuples. 
    each tuple represents a link between states.
    Args:
        path: string (Path of the file in which data is present)
    Returns:
        data: list of tuples which represents the data
    """
    with open(path, "r") as f:
        reader = csv.reader(f)
        return [(row[0], row[1]) for row in list(reader)]

def describe(data, n):
    """
    print a string describing the nth element of the loaded dataset,
    with capitalization.
    Args:
        data: list of tuples
        n: integer
    Returns:
        None (The function prints the string and does not return anything)
    """
    print('Element {0} of the Hamilton data set is {1}. This means that {2} mentions {3} in a song.'.format(n, data[n], str.title(data[n][0]), str.title(data[n][1])))
    
    
    
    
def data_to_dictionary(data):
    """
    convert data (represented as a list of 2-tuples) into a dictionary
    keyed by first entry of the tuple. The corresponding value is the
    list of all second entries corresponding to the first entry,
    with repeats.
    Args:
        data: list of tuples
    Returns:
        dictionary: which is created in this function
    """
    dic = {}
    for i in range(len(data)):
        c = data[i]
        if c[0] in dic:
            dic[c[0]].append(c[1])
        else:
            dic[c[0]] = [c[1]]
        
    return dic