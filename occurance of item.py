# define a function to calulate the ocuurance
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
list1 = [1, 2, 3, 4, 2, 2, 5, 2]
#element_to_count = 2
count = count_occurrences(list1,2)
print(f"Occurrence of 2 is {count}")


#Output
"""
Occurrence of 2 is 4
"""
