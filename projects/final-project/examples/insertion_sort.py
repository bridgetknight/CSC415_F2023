def insertion_sort(grades):
    print("Completing insertion sort...")
    n = len(grades)
    
    for i in range(1, n):
        val = grades[i]
        j = i-1
        while j>=0 and val < grades[j]:
            grades[j+1] = grades[j]
            j = j-1
        grades[j+1] = val
        
    return grades

if __name__ == "__main__":
    grades = [13, 53, 69, 8, 17, 74, 53, 51, 58, 60, 14, 70, 33, 89, 66, 17, 32, 13, 24, 9]
    n_students = len(grades)
    grades_sorted = insertion_sort(grades)
    average = sum(grades)/n_students
    print(f"Highest score: {grades_sorted[-1]}\nLowest score: {grades_sorted[0]}\nAverage: {average}\n")