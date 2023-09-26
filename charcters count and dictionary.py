# this program shows how to put keys and values into an empty dictionary
# we've created a dictionary where the keys are each of the letters present in the string
# and the values are how many times each letter is present.

chars_dict = {}
for ele in "how many characters in this sentence?":
    if ele not in chars_dict:
        chars_dict[ele] = 1
    else:
        chars_dict[ele] += 1

print(chars_dict)
