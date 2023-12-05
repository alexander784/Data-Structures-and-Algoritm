def remove_duplicates(sequence):
    ##Keep track of unique elements
    seen = set()
    ##store unique elements
    result = []

    for item in sequence:
        if item not in seen:
           seen.add(item)
           result.append(item)

        return result 