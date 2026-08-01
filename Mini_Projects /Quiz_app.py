import json

# JSON file load karna
with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

score = 0

print("====== Day 27 - Quiz App ======")
print(f"Total Sawal: {len(questions)}\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")

    # Options dikhao A, B, C, D
    for j, option in enumerate(q["options"]):
        print(f" {chr(65+j)}. {option}")

    # User se answer lo
    ans = input("Tumhara jawab A/B/C/D: ").upper()
    ans_index = ord(ans) - 65 # A=0, B=1...

    if q["options"][ans_index] == q["answer"]:
        print("Sahi jawab! ✅\n")
        score += 1
    else:
        print(f"Galat! Sahi jawab: {q['answer']} ❌\n")

print("====== Quiz Khatam ======")
print(f"Tumhara Final Score: {score}/{len(questions)}")
