def compare(template1, template2):

    score = sum(a == b for a,b in zip(template1, template2))

    return score