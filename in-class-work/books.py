import pandas as pd

# function to sort books using selection sort
def sort_arrivals(file):
    
    # Read in the data and process it
    print("Reading file...")
    books = pd.read_csv(file, engine="python")[:10]
    #years = (books["Year-Of-Publication"]._convert(numeric=True).dropna()).unique()

    # Sort years
    print("Sorting...")
    n = len(books)
    for i in range(n):
        min_index = i
        for j in range(min_index+1, n):
            if(books.iloc[j]["Year-Of-Publication"] < books.iloc[min_index]["Year-Of-Publication"]):
                min_index = j
        (books.iloc[i], books.iloc[min_index]) = (books.iloc[min_index], books.iloc[i])
        
    print("Finding new arrivals...")
    
    # Return 50 most recent books
    new_arrivals = books.iloc[:50]
    
    return pd.DataFrame(new_arrivals)

if __name__ == "__main__":
    
    file = "data/New_Books.csv"
    sort_arrivals(file)