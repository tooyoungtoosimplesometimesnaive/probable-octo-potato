
def uncompress(input):
    """
    2[a2[bc]d] -> abcbcdabcbcd
    Expand string between brackets
    :param input:
    :return:
    """
    if len(input) == 0:
        return ''

    i, j = 0, len(input) - 1
    num = 0
    prefix, suffix = '', ''

    # after this while loop, i will be pointing to [, or points to the end
    while i < len(input) and input[i] != '[':
        if input[i] <= '9' and input[i] >= '0':
            num = num * 10 + int(input[i])
        else:
            prefix += input[i]
        i += 1
    while j > i and input[j] != ']':
        suffix += input[j]
        j -= 1

    if i >= len(input):
        return input
    else:
        return prefix + uncompress(input[i + 1:j]) * num + suffix


if __name__ == '__main__':
    assert uncompress('abcd2[a2[bc]d]ppp') == 'abcdabcbcdabcbcdppp'
    assert uncompress('2[a2[bc]d]') == 'abcbcdabcbcd'
    assert uncompress('aaaa') == 'aaaa'
    assert uncompress('2a2b2c') == '2a2b2c'
    assert uncompress('a11[b]') == 'abbbbbbbbbbb'
