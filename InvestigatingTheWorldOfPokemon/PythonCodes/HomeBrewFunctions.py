def UniqueWordCounter(csv_file, col_name, c_size = None):

    """Return a dictionary with counts of occurrences as value for each key."""

    # Dependencies
    import pandas as pd

    # Create the data frame
    df = pd.read_csv(csv_file, chunksize=c_size)

    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary
    counts_dict = {}

    # Iterate over all of the rows in a column and record the unique word count.
    for entry in df[col_name]:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

    print("\n", "The unique words in the", str(col_name), "column, and the number of times they appear are:")

    for key, value in counts_dict.items():
        print(str(key), ":", int(value))

    return counts_dict

##########

# To be used with the UniqueWordCounter function

def ListGenerator(dictionary):

    """Return two lists of keys and values respectively from a given dictionary."""

    Words = []
    Count = []

    for key, value in dictionary.items():
        Words.append(str(key))
        Count.append(int(value))

    return Words, Count

##########

def NaN_Checker(df):

    """Checks whether NaN values exist within the DataFrame"""

    print("\n", "+++++ NaN value checker.", "\n")

    if df.isnull().any().any():
        print("I returned TRUE, therefore NaN values do exist!")
    else:
        print("I returned False, therefore NaN values do not exist!")
    return df.isnull().any().any()

##########

def NaN_Counter(df):

    """Counts the number of NaN values per column in a Data Frame"""

    print("\n", "+++++ NaN values exist here: ")

    for entry in df.columns:
        print("\n", entry, ", NaN values: ", len(df[df[entry].isnull()]))
    return

##########