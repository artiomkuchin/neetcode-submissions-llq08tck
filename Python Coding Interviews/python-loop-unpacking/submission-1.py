from typing import List, Tuple

# 1 - best student name, 2 - best score 
# Assume Score is not less than 0 and is unique
# Loop - best_student_name , best_score

def best_student(scores: List[Tuple[str, int]]) -> str:
        best_student_name, best_score = "", 0

        for name, score in scores:
            if score > best_score:
                best_student_name, best_score = name, score
        return best_student_name
            


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
