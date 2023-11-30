

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        
        line_status = "The line is currently: "
        for i, person in enumerate(katz_deli, start=1):
            line_status += f"{i}. {person} "
        print(line_status.strip())

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")


katz_deli = []

take_a_number(katz_deli, "Ada")  # => Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace")  # => Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent")  # => Welcome, Kent. You are number 3 in line.

line(katz_deli)  # => "The line is currently: 1. Ada 2. Grace 3. Kent"

now_serving(katz_deli)  # => "Currently serving Ada."

line(katz_deli)  # => "The line is currently: 1. Grace 2. Kent"

take_a_number(katz_deli, "Matz")  # => Welcome, Matz. You are number 3 in line.

line(katz_deli)  # => "The line is currently: 1. Grace 2. Kent 3. Matz"

now_serving(katz_deli)  # => "Currently serving Grace."

line(katz_deli)  # => "The line is currently: 1. Kent 2. Matz"
