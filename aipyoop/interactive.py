def start_learning():
    print("Welcome to AIPyOOP Interactive Learning Mode!")
    while True:
        concept = input("Enter an OOP concept to learn (or 'exit' to quit): ")
        if concept.lower() == 'exit':
            break
        print(OOPConcepts.explain_concept(concept))
