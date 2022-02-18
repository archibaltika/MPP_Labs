from goto import with_goto


@with_goto
def main():
    n = 25
    i = 0
    temp = 0
    max_val = 0
    d = dict()
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "you're", "you've", "you'll",
                  "you'd", "wouldn't",
                  "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "she's", "her",
                  "hers", "herself",
                  "it", "it's", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
                  "who", "whom", "this",
                  "that", "that'll", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have",
                  "has", "had", "doesn't",
                  "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                  "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above",
                  "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
                  "then", "once", "here",
                  "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                  "some", "such", "no",
                  "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
                  "don", "don't", "should",
                  "should've", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "aren't",
                  "couldn't", "didn't",
                  "doesn't", "hadn't", "hasn't", "haven't", "isn't",
                  "mightn't",
                  "mustn't", "needn't", "shan't", "shouldn", "shouldn't", "wasn't",
                  "weren't", "won't"]
    symbols = [',', '.', '/', '!', '?', ':', ';', '-', '"', "'"]

    # Read the file
    with open('text.txt', 'r') as f:
        text = f.read() + "$#"

    # Delete symbols from text
    label .drop_symbols_start
    if text[i] in symbols:
        text = text[:i] + text[i + 1:]
    if text[i] == "$":
        goto.drop_symbols_end
    else:
        i += 1
        goto.drop_symbols_start
    label.drop_symbols_end

    # Convert all characters to lower case
    i = 0
    label .to_lower
    if 64 < ord(text[i]) < 91:
        text = text[:i] + chr(ord(text[i]) + 32) + text[i+1:]

    i += 1
    if text[i] == "$":
        goto.to_lower_end
    goto .to_lower
    label .to_lower_end
    i = 0

    # Creating the dictionary with words and their number
    label.first
    if text[i] == " " or text[i] == "$" or text[i] == "\n":
        if text[temp:i] not in stop_words:
            if d.get(text[temp:i]):
                d[text[temp:i]] += 1
            else:
                d[text[temp:i]] = 1
        temp = i + 1
    i += 1
    if text[i] == "#":
        goto.end
    goto.first
    label.end

    # Searching for max value
    i = len(d)
    values = list(d.values())
    label .max_start
    if max_val < values[i - 1]:
        max_val = list(d.values())[i - 1]
    i -= 1
    if i == 0:
        goto .max_end
    goto .max_start
    label .max_end

    # Printing most used words
    keys = list(d.keys())
    i = 0
    j = max_val
    length = len(d)
    label .print_start
    if n == 0:
        goto .print_end
    if i < length:
        if d[keys[i]] == j:
            print(f"{keys[i]} - {d[keys[i]]}")
            n -= 1
        i += 1
        goto .print_start
    else:
        if j == 0:
            goto.print_end
        j -= 1
        i = 0
        goto.print_start
    label .print_end


if __name__ == "__main__":
    main()
