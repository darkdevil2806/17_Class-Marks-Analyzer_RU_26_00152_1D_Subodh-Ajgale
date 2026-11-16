import numpy as np

PASS_MARK = 40

def get_marks():
    raw_text = input("Marks: ")
    tokens = raw_text.split()

    if len(tokens) == 0:
        print("No marks entered.")
        return None

    marks_list = []
    for token in tokens:      
        try:
            mark = float(token)
        except ValueError:
            print(f"Invalid marks '{token}'. Enter numbers only.")
            return None
        if not (0 <= mark <= 100):
            print("Marks must be between 0 and 100.")
            return None
        marks_list.append(mark) 
    return np.array(marks_list)

def analyze_marks(marks):
    total = len(marks)
    mean = np.mean(marks)
    median = np.median(marks)
    highest = np.max(marks) 
    lowest = np.min(marks)
    std = np.std(marks)
    passed = int(np.sum(marks >= PASS_MARK))
    failed = total - passed
    pass_percentage = (passed / total) * 100 
    above_average = int(np.sum(marks > mean))
    return mean, median, highest, lowest, std, passed, failed, pass_percentage, above_average, total



def print_results(mean, median, highest, lowest, std, passed, failed, pass_percentage, above_average, total):
    print(f"Mean: {mean:.2f} | Median: {median:.2f}")
    print(f"Max: {highest:g} | Min: {lowest:g} | Std Dev: {std:.2f}")
    print(f"Passed: {passed} of {total} | Failed: {failed} | Pass percentage: {pass_percentage:.2f}%")
    print(f"Above average: {above_average} students")

def main():
    marks = get_marks()
    if marks is None:
        return

    mean, median, highest, lowest, std, passed, failed, pass_percentage, above_average, total = analyze_marks(marks)
    print_results(mean, median, highest, lowest, std, passed, failed, pass_percentage, above_average, total)


if __name__ == "__main__":
    main()
