def translate(text: str) -> str:
    """Translate text from English to Pig Latin.

    :param text: str - The input text to translate.
    :return: str - The translated text in Pig Latin.
    """
    vowels = "aeiou"
    result = []

    for word in text.split():
        # Rule 1: Starts with a vowel or "xr"/"yt"
        if word[0] in vowels or word.startswith(("xr", "yt")):
            result.append(word + "ay")
        # Rule 3: Starts with consonants followed by "qu"
        elif word.startswith("qu") or ("qu" in word and word.index("qu") == 1):
            qu_index = word.index("qu") + 2
            result.append(word[qu_index:] + word[:qu_index] + "ay")
        # Rule 4: Starts with consonants followed by "y"
        elif "y" in word and word.index("y") > 0:
            y_index = word.index("y")
            if all(char not in vowels for char in word[:y_index]):
                result.append(word[y_index:] + word[:y_index] + "ay")
            else:
                for i, char in enumerate(word):
                    if char in vowels:
                        result.append(word[i:] + word[:i] + "ay")
                        break
        # Rule 2: Starts with one or more consonants
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(result)