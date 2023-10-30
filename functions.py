def add(score_list, value):
    '''
    Description: Adds a value to the end of the score list if the value is between 10 and 100.
    Input:
    score_list: List of participant scores.
    value: The score to be added.
    Output: Returns the updated score_list.
    '''
    if 10 <= value <= 100:
        score_list.append(value)
    return score_list

def insert_in_score_list(score_list, index, value):
    '''
    Description: Inserts a value at the specified index in the score list if the value is between 10 and 100.
    Input:
    score_list: List of participant scores.
    index: The index at which the score should be inserted.
    value: The score to be inserted.
    Output: Returns the updated score_list.
    '''
    if 10 <= value <= 100:
        score_list.insert(index, value)
    return score_list

def remove(score_list, index):
    '''
    Description: Removes the score of a specific participant at the given index.
    Input:
    score_list: List of participant scores.
    index: The index of the participant whose score should be removed.
    Output: Returns the updated score_list.
    '''
    score_list.pop(index)
    return score_list

def remove_fromindex_toindex(score_list, from_index, to_index):
    '''
    Description: Removes scores from one index to another, inclusively.
    Input:
    score_list: List of participant scores.
    from_index: The starting index.
    to_index: The ending index.
    Output: Returns the updated score_list.
    '''

    score_list[from_index:to_index + 1] = []
    return score_list

def replace(score_list, index, new_value):
    '''
    Description: Replaces the score of a specific participant at the given index with a new value.
    Input:
    score_list: List of participant scores.
    index: The index of the participant whose score should be replaced.
    new_value: The new score to replace the old one.
    Output: Returns the updated score_list.
    '''
    score_list.pop(index)
    score_list.insert(index, new_value)
    return score_list

def less(score_list, value):
    '''
    Description: Returns a list of participants with scores less than the specified value.
    Input:
    score_list: List of participant scores.
    value: The value to compare against for filtering.
    Output: Returns a list of participant names who meet the criteria
    Method: I created a new list in which we append the indeces of the participants with scores
    higher than the given value and created an output list in order to have a nicer UI, by
    choosing the proper sufix for the index of the participant.
    '''
    new_list = []
    output_list = []
    for i in range(len(score_list)):
        if score_list[i] < value:
            new_list.append(i + 1)
    for i in range(len(new_list)):
        sufix = f"st participant" if new_list[i] == 1 else f"nd participant" if new_list[i] == 2 else f"rd participant" if new_list[i] == 3 else f"th participant"
        output_list.append(f"{new_list[i]}{sufix}")
    return output_list

def sorted_standings(score_list):
    '''
    Description: Generates a list of participants in descending order of their scores.
    Input:
    score_list: List of participant scores.
    Output: Returns a list of participants and their standings.
    Method: I created a list containing the participant indices and sorted it using the key=lambda for the
    scores in the score_list and used reverse=True in order to sort the participants in decending order
    of their scores, indicating the place in the standings table. Then I created another list in which
    I played with the sufixes again, in order to have a nicer UI.
    '''
    participant_indices = list(range(len(score_list)))
    participant_indices.sort(key=lambda i: score_list[i], reverse=True)
    participant_place = []
    for i in range(len(participant_indices)):
        place = i + 1
        place_str = f"{place}st place: " if place == 1 else f"{place}nd place: " if place == 2 else f"{place}rd place: " if place == 3 else f"{place}th place: "
        participant_place.append(f"{place_str}{participant_indices[i] + 1}th participant")
    return participant_place

def sorted_higher(score_list, value):
    '''
    Description: Returns a list of indices of participants with scores higher than the specified value, sorted in ascending order of their scores.
    Input:
    score_list: List of participant scores.
    value: The threshold value for comparison.
    Output: Returns a list of indices of participants.
    Method: I created a new list in which i added both the index and the score of the participant, if their score is
    higher than the given value.(using enumerate) Then, I created a list which is a sorted list of the new_list
    in ascending order of the second element of the tuple (the score). For output, I created another list which only
    has the indeces of the participants, the first element of the tuple.
    '''
    new_list = []
    output1 = []
    for i,score in enumerate(score_list):
        if score > value:
            new_list.append((i, score))
    sorted_list = sorted(new_list, key=lambda x: x[1])
    output = [i for i, _ in sorted_list]
    for i in range(len(output)):
        for_sufix = output[i]+1
        sufix = f"{for_sufix}st" if for_sufix == 1 else f"{for_sufix}nd" if for_sufix == 2 else f"{for_sufix}rd" if for_sufix == 3 else f"{for_sufix}th"
        output1.append(f"{for_sufix}{sufix} participant")
    return output1

def avg(score_list, from_index, to_index):
    '''
    Description: Calculates the average score for a range of participants.
    Input:
    score_list: List of participant scores.
    from_index: The starting index of the range.
    to_index: The ending index of the range.
    Output: Returns the average score for the specified range.
    '''
    sum_of_scores = 0
    for i in range(from_index, to_index + 1):
        sum_of_scores += score_list[i]
    average = sum_of_scores / (to_index - from_index + 1)
    return average

def min(score_list, from_index, to_index):
    '''
    Description: Finds the minimum score within a specified range of participants.
    Input:
    score_list: List of participant scores.
    from_index: The starting index of the range.
    to_index: The ending index of the range.
    Output: Returns the minimum score within the range.
    '''
    my_list = []
    for i in range(from_index, to_index + 1):
        my_list.append(score_list[i])
    my_list.sort()
    return my_list[0]

def mul(score_list, value, from_index, to_index):
    '''
    Description: Returns a list of scores that are multiples of the specified value within a given range of participants.
    Input:
    score_list: List of participant scores.
    value: The value to check for multiples.
    from_index: The starting index of the range.
    to_index: The ending index of the range.
    Output: Returns a list of scores that meet the criteria.
    '''
    mul_list = []
    for i in range(from_index, to_index + 1):
        if score_list[i] % value == 0:
            mul_list.append(score_list[i])
    return mul_list

def filter_mul(score_list, value):
    '''
    Description: Filters and returns a list of participants with scores that are multiples of the specified value.
    Input:
    score_list: List of participant scores.
    value: The value to check for multiples.
    Output: Returns a list of filtered scores.
    '''
    new_list = []
    for score in score_list:
        if score % value == 0:
            new_list.append(score)
    return new_list

def filter_greater(score_list, value):
    '''
    Description: Filters and returns a list of participants with scores greater than the specified value.
    Input:
    score_list: List of participant scores.
    value: The threshold value for comparison.
    Output: Returns a list of filtered scores.
    '''
    filtered_list = []
    for score in score_list:
        if score > value:
            filtered_list.append(score)
    return filtered_list

