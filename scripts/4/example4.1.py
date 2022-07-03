computer_engineering_topics = set()
communication_engineering_topics = set()


exit_input = 'n'
print("Enter topics for Computer Engineering: ")
while exit_input != 'y':
    topic = input("Enter topic: ")
    computer_engineering_topics.add(topic)
    exit_input = input("Enter 'y' to exit: ")
    
    
exit_input = 'n'
print("Enter topics for Communication Engineering: ")
while exit_input != 'y':
    topic = input("Enter topic: ")
    communication_engineering_topics.add(topic)
    exit_input = input("Enter 'y' to exit: ")
    
print("Computer Engineering: ", computer_engineering_topics)
print("Communication Engineering: ", communication_engineering_topics)
print("Common topics: ", computer_engineering_topics.intersection(communication_engineering_topics))
print("Extra topics in communication engineering: ", communication_engineering_topics.difference(computer_engineering_topics))
print("Extra topics in computer engineering: ", computer_engineering_topics.difference(communication_engineering_topics)
      
      teste.startswith()
      