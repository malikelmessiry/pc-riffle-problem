def riffle(words):
    riffled = [] 
    max_len = 0
    max_idx = None 

    # find max_len and max_idx
    for i, word in enumerate(words):
        if len(word) >= max_len:
            max_len = len(word)
            max_idx = i

    # iterate over each letter position
    for letter_idx in range(max_len):
        # iterate over each word
        for word_idx, word in enumerate(words):
            riffled.append(word[letter_idx % len(word)])
            if letter_idx == max_len-1 and word_idx == max_idx:
                break

    return "".join(riffled)


words = ["abc", "mno", "xyz"]
expected = "amxbnycoz"
assert riffle(words) == expected

words = ["ab", "mississippi"]
expected = "ambiasbsaibsasbiapbpai"
assert riffle(words) == expected

words = ["mississippi", "ab"]
expected = "maibsasbiasbsaibpapbi"
assert riffle(words) == expected

words = ["choo", "a", "choo", "b"]
expected = "cacbhahboaoboao"
assert riffle(words) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
