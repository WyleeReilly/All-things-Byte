"""
Write a program that takes a filename and a second
parameter called n

Return a list in descending order of the most common words in the file
n is the number of the 'most common words' in the file

"""

def word_stats(filename, n):
    with open(filename, "r", encoding='utf8') as text:
        #Here I am using a list comprehension to create one list of each word    
        word_list = [word for line in text for word in line.split()]

        word_list = [word.strip().lower() for word in word_list]
        bad_chars = [',', "'", '"', '!', '.', '-', '(', ')']
        for word in range(len(word_list)):
            for x in bad_chars:
                word_list[word] = word_list[word].replace(x, '') 
    
    #initializing a dictionary
    word_counts = {}
    #looping through my list of words and appending ...
    for word in word_list:
        #I don't know how this .get works but its adding each word
        word_counts[word] = word_counts.get(word,0) + 1
    word_counts = sorted(word_counts.items(), key = lambda x: x[1], reverse = True)

    final_list = ()
    for x in range(0,n):
        final_list += word_counts[x]
    
    return(final_list)
        #print(word_counts[x][x+1])



print(word_stats('test.txt', 3))




"""word_freq = []
    #iterating through my dictionary i just made earlier to flip key and value 
    #so that i can sort by key value... is this necessay?
    for key,value in word_counts.items():
        word_freq.append((value, key))
    sorted_list = word_freq.sort(reverse=True)

    counter = n
    while counter >0:
        print(value, key)
        counter -=1
"""