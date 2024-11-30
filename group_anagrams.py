from typing import List
import string


def group_anagrams(strs: List[str]) -> List[List[str]]:
    base_key = [0] * 26
    # Create dict with all the letters and an index
    letters = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
    m: dict = {}

    for word in strs:
        tmp_key = base_key.copy()
        for l in word:
            index = letters[l]
            tmp_key[index] += 1
        key = "".join(str(tmp_key))
        if key in m:
            m[key].append(word)
        else:
            m[key] = [word]

    result: List[List[str]] = []
    for k, v in m.items():
        result.append(v)
    return result


input: List[str] = ["act", "pots", "tops", "cat", "stop", "hat"]
expected_output: List[List[str]] = [
    ["hat"], ["act", "cat"], ["stop", "pots", "tops"]
]

output: List[List[str]] = group_anagrams(input)

assert sorted(output) == sorted(expected_output)
print("yaay")