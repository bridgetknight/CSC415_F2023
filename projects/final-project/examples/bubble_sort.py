def bubble_sort(grades):
    print("Completing bubble sort...")
    n = len(grades)-1
    
    for idx, el in enumerate(grades[:n]):
        if(grades[idx] > grades[idx+1]):
            grades[idx], grades[idx+1] = grades[idx+1], grades[idx]

    return grades

if __name__ == "__main__":
    grades = [13, 53, 69, 8, 17, 74, 53, 51, 58, 60, 14, 70, 33, 89, 66, 17, 32, 13, 24, 9]
    n_students = len(grades)
    grades_sorted = bubble_sort(grades)
    average = sum(grades)/n_students
    print(f"Highest score: {grades_sorted[-1]}\nLowest score: {grades_sorted[0]}\nAverage: {average}\n")