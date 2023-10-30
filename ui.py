import functions

score_list = []
undo_stack = []

while True:
    print("\nMenu")
    print(f"Score table: {score_list}")
    print("1. Add the result of a new participant to the array")
    print("2. Modify the scores in the array (as a result of appeals)")
    print("3. Get the participants with scores having some properties")
    print("4. Obtain different characteristics of participants")
    print("5. Filter values")
    print("6. Undo")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. Add a score as the last element of the score list")
        print("2. Insert a score at a wanted index")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            while True:
                value = int(input("Enter the score you want to add to the list (or -1 to exit): "))
                if value == -1:
                    break
                if 10 <= value <= 100:
                    undo_stack.append(list(score_list))
                    score_list = functions.add(score_list, value)
                    print("Updated scores:", score_list)
                else:
                    print("The participants scores should be between 10 and 100. Please enter a valid input.")

        if choice1 == 2:
            value = int(input("Enter a value: "))
            index = int(input("Enter the index(the index of the first element is 0): "))
            try:
                undo_stack.append((list(score_list)))
                if 10 <= value <= 100:
                    print(f"Modified scores are now: {functions.insert_in_score_list(score_list, index, value)}")
                else:
                    print("The participants scores should be between 10 and 100. Please enter a valid input.")
            except IndexError:
                print("Invalid index. Please enter a proper value.")

        if choice1 != 1 and choice1 != 2:
            print("Invalid input. Please enter a proper choice.")


    if choice == 2:
        print("1. Remove the score of a specific participant")
        print("2. Remove all the scores from a participant to another")
        print("3. Replace the score of a participant")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            index = int(input("Enter the number of the participant: "))
            if 0 < index <= len(score_list):
                undo_stack.append((list(score_list)))
                functions.remove(score_list, index-1)
                sufix = f"{index}st" if index == 1 else f"{index}nd" if index == 2 else f"{index}rd" if index == 3 else f"{index}th"
                print(f"The score list after removing the score of the {sufix} participant is: {score_list}")
            else:
                print("Invalid input. Please enter proper participant numbers.")

        if choice1 == 2:
            from_index = int(input("First participant: "))
            to_index = int(input("Last participant: "))
            if 0 < from_index < to_index <= len(score_list):
                undo_stack.append((list(score_list)))
                functions.remove_fromindex_toindex(score_list, from_index-1, to_index-1)
                sufix1 = f"{from_index}st" if from_index == 1 else f"{from_index}nd" if from_index == 2 else f"{from_index}rd" if from_index == 3 else f"{from_index}th"
                sufix2 = f"{to_index}st" if to_index == 1 else f"{to_index}nd" if to_index == 2 else f"{to_index}rd" if to_index == 3 else f"{to_index}th"
                print(f"The score list after removing the scores between {sufix1} participant and {sufix2} participant is: {score_list}")
            else:
                print("Invalid input. Please enter proper participant numbers.")

        if choice1 == 3:
            index = int(input("Enter the number of the participant you want to change the score for:"))
            if 0 < index <= len(score_list):
                undo_stack.append((list(score_list)))
                sufix = f"{index}st" if index == 1 else f"{index}nd" if index == 2 else f"{index}rd" if index == 3 else f"{index}th"
                new_value = int(input(f"Enter modified score for the {sufix} participant:"))
                score_list = functions.replace(score_list, index-1, new_value)
                print("The modified scores are now: ", score_list)
            else:
                print("Invalid input. Please enter proper participant numbers.")

        if choice1 != 1 and choice1 != 2 and choice1 != 3:
            print("Invalid input. Please enter a proper choice.")

    if choice == 3:
        print("1. Get the participants with scores less than value")
        print("2. Get the standings of the participants")
        print("3. Get the participants with scores higher than value sorted")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            value = int(input("Enter the value: "))
            if value < 100:
                print(f"The following participants have their scores less than {value}:")
                print(*functions.less(score_list, value), sep="\n")
            else:
                print("Invalid input. Please enter a proper value.")

        if choice1 == 2:
            print("Standings:")
            print(*functions.sorted_standings(score_list), sep="\n")

        if choice1 == 3:
            value = int(input("Enter a value: "))
            if value <= 100:
                print(f"Participants with scores higher than {value} sorted are:")
                print(*functions.sorted_higher(score_list, value), sep="\n")
            else:
                print("Invalid input. Please enter a proper value.")

        if choice1 != 1 and choice1 != 2 and choice1 != 3:
            print("Invalid input. Please enter a proper choice.")

    if choice == 4:
        print("1. Get the average score starting from a participant to another")
        print("2. Get the minimum score starting from a participant to another")
        print("3. Get the scores starting from a participant to another which are multiples of value")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            from_index = int(input("First participant: "))
            to_index = int(input("Last participant: "))
            sufix1 = f"{from_index}st" if from_index == 1 else f"{from_index}nd" if from_index == 2 else f"{from_index}rd" if from_index == 3 else f"{from_index}th"
            sufix2 = f"{to_index}st" if to_index == 1 else f"{to_index}nd" if to_index == 2 else f"{to_index}rd" if to_index == 3 else f"{to_index}th"
            if 0 < from_index < to_index <= len(score_list):
                print(
                    f"The average score starting from {sufix1} participant to {sufix2} participant is {functions.avg(score_list, from_index - 1, to_index - 1)}.")
            else:
                print("Invalid input. Please enter proper participant numbers.")

        if choice1 == 2:
            from_index = int(input("First participant: "))
            to_index = int(input("Last participant: "))
            wr_from_index = f"{from_index}st" if from_index == 1 else f"{from_index}nd" if from_index == 2 else f"{from_index}rd" if from_index == 3 else f"{from_index}th"
            wr_to_index = f"{to_index}st" if to_index == 1 else f"{to_index}nd" if to_index == 2 else f"{to_index}rd" if to_index == 3 else f"{to_index}th"
            if 0 < from_index < to_index <= len(score_list):
                print(f"The minimum score starting from {wr_from_index} participant to {wr_to_index} participant is {functions.min(score_list, from_index - 1, to_index - 1)}.")

        if choice1 == 3:
            value = int(input("Enter the value: "))
            from_index = int(input("First participant: "))
            to_index = int(input("Last participant: "))
            sufix1 = f"{from_index}st" if from_index == 1 else f"{from_index}nd" if from_index == 2 else f"{from_index}rd" if from_index == 3 else f"{from_index}th"
            sufix2 = f"{to_index}st" if to_index == 1 else f"{to_index}nd" if to_index == 2 else f"{to_index}rd" if to_index == 3 else f"{to_index}th"
            if 0 < value <= 100:
                if 0 < from_index < to_index <= len(score_list):
                    print(f"The scores multiples of {value} starting from {sufix1} participant to {sufix2} participant are:")
                    print(f"{functions.mul(score_list, value, from_index - 1, to_index - 1)}")
                else:
                    print("Invalid input. Please enter proper participant numbers.")
            else:
                print("Invalid input. Please enter a proper value.")

        if choice1 != 1 and choice1 != 2 and choice1 != 3:
            print("Invalid input. Please enter a proper choice.")

    if choice == 5:
        print("1. Keep only the participants with scores multiples of value")
        print("2. Keep only the participants with scores higher than value")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            value = int(input("Enter a value: "))
            if value < 100:
                undo_stack.append((list(score_list)))
                score_list = functions.filter_mul(score_list, value)
                print(f"The score list after only keeping the scores multiples of {value} is: {score_list}.")
            else:
                print("Invalid input. Please enter a proper value.")

        if choice1 == 2:
            value = int(input("Enter a value: "))
            if value < 100:
                undo_stack.append((list(score_list)))
                score_list = functions.filter_greater(score_list, value)
                print(f"The score list after only keeping the scores higher than {value} is: {score_list}.")
            else:
                print("Invalid input. Please enter a proper value.")

        if choice1 != 1 and choice1 != 2:
            print("Invalid input. Please enter a proper choice.")

    if choice == 6:
        if undo_stack:
            previous_state = undo_stack.pop()
            score_list = previous_state
            print(f"Undoing the last operation. Current scores: {score_list}")
        else:
            print("Nothing to undo.")

    if choice == 7:
        break

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7:
        print("Invalid input. Please enter a proper choice.")



