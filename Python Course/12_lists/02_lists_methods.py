marks = [5, 2, 23, 42,83]
extra_marks = [63,73, 83, 93]

print(marks)
marks.append(34)  # Adds 34 to the end of the list
print(marks)
marks.pop() # Removes the last elenment from the list
print(marks)
marks.extend(extra_marks)  # Adds all elements from extra_marks to marks
marks.reverse() # Reverses the order of elements in the list
print(marks)
marks.sort()  # Sorts the list in ascending order
print(marks)
marks.insert(2, 99)  # Inserts 99 at index 2
print(marks)
