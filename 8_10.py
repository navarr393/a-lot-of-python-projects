def send_messages(text=[], messages=[]):
    for message in text:
        print(message)
        messages.append(message)


sent_messages = []
texts = ['Hello', 'There', 'Nice', 'To', 'Meet', 'You']
send_messages(texts, sent_messages)

#sent messages list
print("\nnew list:") 
for sent in sent_messages:
    print(sent)
