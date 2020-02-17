




def matrix_sort(matrix):
    with open(matrix, "r", encoding='utf8') as numbers:
        #Here I am using a list comprehension to create one list of each word...
        # .. by doing a nested for-loop within a list comprehension    
        matrix_list = [word for line in numbers for word in line.splitlines()]

"""
        file = open(filename, "r")
        lines = [line.split() for line in file]
        #Next step is to do a to-int"""

        matrix_list = [x.replace(' ',',') for row in matrix_list for x in row]
    
        #print(matrix_list)
        #Right now I have it split up, but it is not saving to anything. so, once this for loop is called, it is 
        #instantle going into the garbage

        #initial function is the sorter function.
        #second function 

        empty_dict = {}
        #print(matrix_list)
        #for x in range(len(matrix_list)):
         #   print([x, matrix_list[x]])
            #matrix_list.append(empty_dict)
        #print(matrix_list)



matrix_sort('testmatrix.txt')







"""
        for line_num in range(len(matrix_list)):
            for line in matrix_list:
                matrix_to_dict += {line_num, line}
"""