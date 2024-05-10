import json
# script to see gpt's incorrect answer

with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(1, 31):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses1-30.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(31, 61):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses31-60.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(31, 61):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses31-60.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(61, 91):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses61-90.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(91, 121):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses91-120.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value) 
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(121, 151):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses121-150.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)       
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(151, 181):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses151-180.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)
print()
with open("statements.json", "r") as file:
    wrong_answers = []
    data = json.load(file)
    for i in range(181, 201):
        statement = data[str(i)][0]
        true_value = data[str(i)][1]
        with open("gptresponses180-200.json", 'r') as file2:
            data2 = json.load(file2)
            gpt_answer = data2[str(i)][statement]
            if true_value != gpt_answer:
                print(statement, gpt_answer, true_value)    