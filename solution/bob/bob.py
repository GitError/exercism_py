def response(hey_bob: str) -> str:
    """Determine Bob's response based on the input.

    :param hey_bob: str - The input string directed at Bob.
    :return: str - Bob's response.
    """
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever."