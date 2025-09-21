import re

def greedy_matching(text):
    """
    Demonstrates greedy matching in regular expressions.
    Greedy quantifiers match as much as they can.
    """
    pattern = r"<(.*)>"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def non_greedy_matching(text):
    """
    Demonstrates non-greedy matching in regular expressions using *?.
    Non-greedy quantifiers match as little as they can.
    """
    pattern = r"<(.*?)>"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    test_string = "This is a <test> string with <multiple> tags."
    print(f"Original string: {test_string}")
    print(f"Greedy match: {greedy_matching(test_string)}")
    print(f"Non-greedy match: {non_greedy_matching(test_string)}")
