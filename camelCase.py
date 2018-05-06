def camelcase(s):
    # Complete this function
    if len(s) == 0: return 0

    num_words = 1;
    for c in s:
        if ord('a') - ord(c) > 0:
            num_words += 1
    return num_words