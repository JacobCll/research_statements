from UnlimitedGPT import ChatGPT
import csv
import json

filename = 'data.csv'

statements = {}
subject_list = ['Science', 'History', 'History, Political', "Science, Technology", "Geography, Science"]

with open(filename, 'r', encoding='cp1252', newline="" ,errors='ignore') as data:
    readobject = csv.reader(data, delimiter=',')
    torf = ['TRUE', 'FALSE']
    itemnum = 0
    for row in readobject:
        if row[2] in torf and row[1] in subject_list:
            statement = row[5]
            boolean = row[2]
            itemnum += 1
            statements[itemnum] = [statement, boolean]

session_token = "INSERT SESSION TOKEN HERE"

def promptGPT(statementsdict, start: int, end: int):
    gptresponses = {}
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    chatbot = ChatGPT(
    session_token=session_token,
    proxy=None,
    chrome_args=None,
    disable_moderation=False,
    verbose=False,
    )
    
    # change this
    for i in range(start, end):
        statement:str = statementsdict[str(i)][0] 
        boolval:str = statementsdict[str(i)][1]
        try:
            message = chatbot.send_message(f"A statement will be shown to you. The statement has a ground truth value of True or False. Identify the truth value of the statement. Answer only in TRUE or FALSE, all capitalized. You are not allowed to answer both. Do not explain and elaborate your answer. Make sure that your answer will only consist of 1 word. The statement is: {statement}",
                                        input_mode="SLOW",
                                        input_delay=1.0)
            response = str(message.response)
            gptresponses[str(i)] = {statement: response}

            # handle TP and FP
            if boolval == "TRUE":
                if response == boolval:
                    TP +=  1
                else:
                    FP += 1
            # handle TN and FN
            elif boolval == "FALSE":
                if response == boolval:
                    TN += 1
                else:
                    FN += 1

        except:
            print("An error has occured, iteration stopped at", i)
            break

    gptresponses["TP"] = TP
    gptresponses["FP"] = FP
    gptresponses["TN"] = TN
    gptresponses["FN"] = FN
    
    print(gptresponses)

    json_object = json.dumps(gptresponses, indent=4)
    with open(f"gptresponses{start}-{end-1}.json", 'w') as file:
        file.write(json_object)
        
        

with open("statements.json", 'r') as file:
    # python object
    data = json.load(file)

promptGPT(data, 1, 31)
promptGPT(data, 31, 61)
promptGPT(data, 61, 91)
promptGPT(data, 91, 121)
promptGPT(data, 121, 151)
promptGPT(data, 151, 181)
promptGPT(data, 181, 201)