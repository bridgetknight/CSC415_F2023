def selection_sort(grades):
    print("Completing selection sort...")
    n = len(grades)
    
    for i in range(n):
        min_index = i
        for j in range(min_index+1, n):
            if(grades[j] < grades[min_index]):
                min_index = j
                (grades[i], grades[min_index]) = (grades[min_index], grades[i])

    return grades

if __name__ == "__main__":
    grades = [13, 53, 69, 8, 17, 74, 53, 51, 58, 60, 14, 70, 33, 89, 66, 17, 32, 13, 24, 9]
    n_students = len(grades)
    grades_sorted = selection_sort(grades)
    average = sum(grades)/n_students
    print(f"Highest score: {grades_sorted[-1]}\nLowest score: {grades_sorted[0]}\nAverage: {average}\n")