# Defining Global Scope Lists
cache = []
requests = []


# Defining Functions

# -- FIFO Function
def fifo():
    """
    Implements the First In First Out (FIFO) page replacement algorithm
    for a cache with a capacity of 8.

    Description:
    This function iterates through the list of requested pages, checking
    their presence in the cache. If a page is in the cache, it prints "hit";
    otherwise, it prints "miss". When the cache reaches its capacity of 8,
    the oldest page (the first page) is evicted, and the new page is appended
    to the end of the list.

    Arguments: None
    Return values: None
    """
    # Loop over the list of requested pages
    for request in requests:
        # Check if requested page is already in cache
        if request in cache:
            print("hit")

        else:
            print("miss")

            # If cache is full, remove oldest page
            if len(cache) >= 8:
                cache.pop(0)

            # Add new page to the end of cache
            cache.append(request)

    print(cache)


# -- LFU Function
def lfu():
    """
    Implements the Least Frequently Used (LFU) page replacement algorithm
    for a cache with a capacity of 8.

    Description:
    This function iterates through a list of requested pages, checking
    their presence in the cache. If a page is not in the cache and the cache
    is not full, it is added to the cache with a "miss" recorded. When the
    cache is at full capacity, the least frequently requested page is
    evicted, and the new page is appended. In the event of multiple
    least-frequently-used pages, the lowest page number is selected
    for eviction.

    Arguments: None
    Return values: None
    """
    # Defining a dictionary to store data about
    # page numbers and their frequency
    request_occurrences = {}

    # Loop over list of requested pages
    for request in requests:
        # If requested page is not in cache and cache is not full
        if request not in cache and len(cache) < 8:
            print("miss")
            # Update request occurrences dictionary
            request_occurrences[request] = 1
            # Add page to cache
            cache.append(request)

        # If requested page is not in cache and cache is full
        elif request not in cache and len(cache) == 8:
            print("miss")
            # In case page is not in cache but it is in the dictionary
            if request in request_occurrences:
                # Update page occurrences dictionary
                request_occurrences[request] += 1

            else:
                request_occurrences[request] = 1

            # Sort dictionary by page number
            sorted_by_page = dict(
                sorted(request_occurrences.items(), key=lambda item: item[0]))

            # Sort the sorted dictionary by page occurrences
            sorted_by_occurrence = dict(
                sorted(sorted_by_page.items(), key=lambda item: item[1]))

            # Loop through keys (page numbers) in the twice sorted dictionary,
            # if it is in cache remove it and append new request
            for key in sorted_by_occurrence.keys():
                if key in cache:
                    cache.remove(key)
                    cache.append(request)
                    break

        # If requested page is in cache
        else:
            print("hit")
            # Update the page occurrences dictionary
            request_occurrences[request] += 1

    print(cache)


# Main Program

# Infinite loop to continuously prompt the user for input
while True:

    # Gather user's requested pages
    while True:
        requested_number = input(
            "Enter a positive number or enter 0 to exit: ")

        # Check if input is a digit
        if requested_number.isdigit():
            requested_number = int(requested_number)

            # If a positive number is entered, add it to the list of requests
            if requested_number > 0:
                requests.append(requested_number)

            # If 0 is entered, break out of the loop
            if requested_number == 0:
                break

    # Get and process user's choice
    user_command = input(
        "Press 1 for FIFO, 2 for LFU, or Q to quit the program: \n")

    if user_command == "1":
        fifo()
        # Clear cache and list of requests after execution
        cache.clear()
        requests.clear()

    elif user_command == "2":
        lfu()
        # Clear cache and list of requests after execution
        cache.clear()
        requests.clear()

    elif user_command.upper() == "Q":
        quit()

    else:
        print("Invalid input. Try again\n")
