from goto import with_goto


@with_goto
def main():
    i = 0
    temp = 0
    row_counter = 0
    page_counter = 1  # It is more common to use line numbering that begins with 1
    d = dict()
    res = dict()
    symbols = [',', '.', '/', '!', '?', ':', ';', '-', '"', "'"]

    with open('text1.txt', 'r') as f:  # Reading the file 'text1.txt'
        text = f.read() + "$#"

    # Convert all characters to lower case
    label .to_lower
    if 64 < ord(text[i]) < 91:
        text = text[:i] + chr(ord(text[i]) + 32) + text[i+1:]
    i += 1
    if text[i] == "$":
        goto.to_lower_end
    goto .to_lower
    label .to_lower_end

    # Delete symbols from text
    i = 0
    label .drop_symbols_start
    if text[i] in symbols:
        text = text[:i] + text[i + 1:]
        i -= 1
    if text[i] == "$":
        goto.drop_symbols_end
    else:
        i += 1
        goto.drop_symbols_start
    label.drop_symbols_end

    # Fill the dictionary with values in the format:
    # {"word" : [number of words, page_1, page_2, ..., page_n ], ...}
    i = 0
    label .format_start
    if text[i] == " " or text[i] == "$" or text[i] == "\n":
        if text[i] == "\n":
            row_counter += 1
            page_counter = row_counter // 45 + 1
        if d.get(text[temp:i]):
            d[text[temp:i]][0] += 1
            if d[text[temp:i]][-1] != page_counter:
                d[text[temp:i]].append(page_counter)
        else:
            d[text[temp:i]] = [1, page_counter]
        temp = i + 1
    i += 1
    if text[i] == "#":
        goto.format_end
    goto.format_start
    label .format_end

    # Delete the words which number > 100
    i = 0
    keys = list(d.keys())
    values = list(d.values())
    length = len(d)
    label .strict_start
    if d[keys[i]][0] < 101:
        res[keys[i]] = d[keys[i]][1:]
    i += 1
    if i == length:
        goto.strict_end
    goto.strict_start
    label.strict_end

    # Sort the 'keys' list
    keys = list(res.keys())
    values = list(res.values())
    length = len(res)
    i = 0
    label .sort_start
    if i == length - 1:
        goto.sort_end
    j = 0
    # ------------------Start of inner cycle------------------
    label .inner_start
    if j == length - 1 - i:
        goto.inner_end
    if keys[j] > keys[j + 1]:
        keys[j], keys[j + 1] = keys[j + 1], keys[j]
    j += 1
    goto.inner_start
    label .inner_end
    # ------------------End of inner cycle------------------
    i += 1
    goto.sort_start
    label .sort_end

    # Print the result dictionary
    i = 0
    label .print_start
    print(f"{keys[i]} - {str(res[keys[i]])[1:-1]}")
    if i == length - 1:
        goto.print_end
    else:
        i += 1
        goto.print_start
    label .print_end


if __name__ == "__main__":
    main()
