import matplotlib.pyplot as plt
import json
import sys


def printMessages(file):
    f = open(file,"r", encoding='utf-8')
    data = json.loads(f.read()) 
    f.close()
    
    names = []
    messages = []
    messageTotalLength = []
    averageMessageLength = []

    # Count messages
    for message in data['messages']:
        if "from" in message:
            if message["from"] not in names and message["from"] != None:
                names.append(message["from"])
                messages.append(0)
                messageTotalLength.append(0)
                averageMessageLength.append(0)
            for i in range(0, len(names)):
                if (message["from"] == names[i]):
                    messages[i] += 1
                    messageTotalLength[i] += len(message["text"])

    # Print
    for i in range(0, len(names)):
        averageMessageLength[i] = messageTotalLength[i] / messages[i]
        print(str(names[i]) + ' sent ' + str(messages[i]) + ' messages')
        print('Totalling ' + str(messageTotalLength[i]) + ' characters')
        print('Averaging ' + str(round(averageMessageLength[i], 1)) + ' characters per message')
        print()
     
    # Plot
    plt.style.use('seaborn')
    
    plt.bar(names, messages)
    plt.title('Number of Messages')
    plt.ylabel('Messages')
    
    plt.figure()
    plt.bar(names, messageTotalLength)
    plt.title('Total Characters')
    plt.ylabel('Characters')
    
    plt.figure()
    plt.bar(names, averageMessageLength)
    plt.title('Average Characters')
    plt.ylabel('Characters')
    
    plt.show()


args = sys.argv
if len(args) <= 1:
    print("Please use the format 'python run.py [filename]\n")
else:
    file = args[1]
    printMessages(file)
