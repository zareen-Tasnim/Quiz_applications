from string import ascii_lowercase

QUESTIONS = {
        "What's the purpose of the built-in zip() function": [
                "To iterate over two or more sequences at the same time",
                "To combine several strings into one",
                "To compress several files into one archive",
                "To get information from the user",
            ],
            "What's the name of Python's sorting algorithm": [
                "Timsort", "Quicksort", "Merge sort", "Bubble sort"
            ],
            "What does dict.get(key) return if key isn't found in dict": [
                "None", "key", "True", "False",
            ]
}
num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"{label} {alternative}")

    answer_label = input("\nChoices:")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("*CORRECT*")
    else:
        print(f"Correct answer is {correct_answer} not {answer}")

print(f"You gave right answer for {num_correct} questions out of {num} questions")