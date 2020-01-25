from hypothesis import given, example, settings
from hypothesis.strategies import text, lists, integers


def encode(input_string):
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q


def average_agreement(list1, list2, max_depth):
    # Empty lists evaluate to false.
    if (not list1) or (not list2):
        return 0.0

    ### NEW CODE ###
    # Truncate the depth
    max_list_len = max(len(list1), len(list2))
    max_depth = min(max_depth, max_list_len)

    agreements = []

    for depth in range(1, max_depth + 1):
        set1 = set(list1[:depth])
        set2 = set(list2[:depth])

        intersection = set1 & set2

        agreements.append(2 * len(intersection) / (len(set1) + len(set2)))

    return sum(agreements) / len(agreements)


@given(
    list1=lists(integers(min_value=1)),
    list2=lists(integers(min_value=1)),
    depth=integers(min_value=1)
)
@settings(deadline=300)  # <- NEW CODE
def test_average_agreement_properties(list1, list2, depth):
    answer = average_agreement(list1, list2, depth)
    inverse_answer = average_agreement(list2, list1, depth)

    assert answer >= 0.0
    assert answer <= 1.0
    assert answer == inverse_answer

@given(s=text())
@example(s="001")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


if __name__ == "__main__":
    test_decode_inverts_encode()