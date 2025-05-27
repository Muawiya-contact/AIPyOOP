class OOPConcepts:
    @staticmethod
    def explain_concept(concept_name):
        concepts = {
            "class": "A class is a blueprint for creating objects.",
            "object": "An object is an instance of a class.",
            "inheritance": "Inheritance allows a class to inherit attributes and methods from another class.",
            "polymorphism": "Polymorphism allows methods to do different things based on the object it is acting upon.",
            "encapsulation": "Encapsulation restricts direct access to object data and methods."
        }
        return concepts.get(concept_name.lower(), "Concept not found.")
