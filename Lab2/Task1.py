import re
from constants import abbreviations, regular_sentence, regular_word, regular_sentence_declarative, regular_abbreviations


def analyse_sentences(sents):
    declaratives = 0
    non_declaratives = 0
    for sent in sents:
        if re.fullmatch(regular_sentence_declarative, sent):
            print("declarative:\t" + sent)
            declaratives += 1
        else:
            print("non_declarative:\t" + sent)
    non_declaratives = len(sents) - declaratives
    print("\n\n")
    print("The number of declarative sentences:\t" + str(declaratives))
    print("The number of non_declarative sentences:\t " + str(non_declaratives))
    return non_declaratives







def Task1( string, n, k):
    default_dict: dict[str, int] = {}
    if string == "":
        return 0, 0, 0, 0, default_dict



    average_words = 0.0
    average_sentence = 0.0
    total_words = 0
    total_length = 0.0
    sentences_tuples = re.findall(regular_sentence, string)
    sentences = ["" for _ in range(len(sentences_tuples))]
    for ind, sent in enumerate(sentences_tuples):
        sentences[ind] = sent[0]

    nd = analyse_sentences(sentences)



    for sent in sentences:
        words = re.findall(regular_word, sent, re.IGNORECASE)
        total_words += len(words)
        for word in words:
            total_length += len(word)

    if total_words != 0:
        average_sentence = total_length/len(sentences)
        average_words = total_length/total_words


    print("\n\nAverage word length: " + str(average_words))
    print("Average sentence length: " + str(average_sentence))

    return len(sentences), nd, average_sentence, average_words

print("task1\n\n")
task1_text = 'Abc... Abc?! Abc!!! Mr. Abc: Abc, Abc. Mr., Abc?! Hello. My Name is Dasha. Hagimemashite!! '
N = 4
K = 10
Task1(task1_text, N, K)


