import math
import re
import statistics

def menu(options, prompt):  # General menu function. The second part for the menu is at the bottom of the codes.
    choice_selected = False
    selection = []
    for opt in options:
        s = opt.split(".")[0].strip()
        selection.append(s.lower())

    while not choice_selected: 
        print("\n" + prompt + "\n") # To good looking code
        for opt  in options:
            print(opt)
        print("")
        selected = input("==>")
        selected = selected.lower()
        if selected in selection:
            return selected
        else:
            print("You must choose one of the valid choices of ", selection)

def get_valid_name(prompt): # To detect is a name of the file valid or invalid. If invalid keeps asking for the valid name.
    valid = False
    while valid is False:
        try:
            file_name = input(prompt)
            test = open(file_name,"r")
            test.close()
            valid = True
        except FileNotFoundError:
            print("Could not find the file you specified bad")
            file_name = get_valid_name(prompt)
        except IOError:
            print("IOError for %s " % file_name)
            file_name = get_valid_name(prompt)
    return file_name

def findscore(lines, word):
    """Collect ratings for whole-word occurrences, ignoring case."""
    word = word.strip().casefold()
    if not word:
        return []
    results = []
    pattern = re.compile(r"(?<!\w)" + re.escape(word) + r"(?!\w)")
    for line in lines:
        if not line.strip():
            continue
        rating, _, review = line.strip().partition(' ')
        results.extend([int(rating)] * len(pattern.findall(review.casefold())))
    return results


def average(numbers):
    return statistics.mean(numbers) if numbers else math.nan


def standard_deviation(scores):
    return statistics.pstdev(scores) if scores else math.nan


def process_list(list_of_words, review_file): # To append those calculated values to list
    temp = []
    for word in list_of_words:
        word = word.strip()
        scores = findscore(review_file, word)
        avg = average(scores)
        std = standard_deviation(scores)
        temp.append((word, len(scores), avg, std))
    return temp


def report(results, sort_key, asc=True): # I used key=lambda method to sort because it was the only way I found to sort tuples.
    print("{:<20}{:>15}{:>15}{:>15}".format("Word","Occurence","Avg Score", "Std")) # Formatting
    print("="*65) # To good looking code
    if asc is True:
        s = sorted(results,key=lambda r: r[sort_key])
    else:
        s = sorted(results,key=lambda r: r[sort_key], reverse=True)
    for row in s:
        print("{:<20}{:>15d}{:>15.4f}{:>15.4f}".format(row[0],row[1],row[2],row[3])) # To format the values 

def main():
    with open("movieReviews.txt", encoding="utf-8") as stream:
        reviewsfile = stream.readlines()

    quit = False

    while quit is False: 
        x = menu(["1. Get sentiment for all words in a file","Q. Quit"], "    Python Sentiment Analysis.") # Goes back to first function

        if x == "q": # If user wants to quit
            quit = True

        if x == "1": # Optional choices
            f = get_valid_name("Enter the name of the file with words to score ")
            with open(f, encoding="utf-8") as stream:
                wordlist = stream.readlines()
            results = process_list(wordlist, reviewsfile)
            inner_quit = False
            while inner_quit is False:
                y = menu(["   1. Sort by Avg Ascending", "   2. Sort by Avg Descending", "   3. Sort by Standard Deviation Ascending","   4. Sort by Standard Deviation Descending","   Q. Exit"],"    Sort Options")
                if y == "1":
                    report(results,2) # Normally sort ( Ascending)
                if y == "2":
                    report(results,2, asc=False) # To reverse (Descending)
                if y == "3":
                    report(results,3) # Normally sort ( Ascending)
                if y == "4":
                    report(results,3, asc=False) # To reverse (Descending)
                if y =="q":
                    inner_quit = True # To quit


if __name__ == "__main__":
    main()
