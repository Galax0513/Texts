import numpy as np

text = open('avidreaders.ru__mertvye-dushi.txt', encoding='utf8').read()

words = text.split()


def make_pairs(words):
    for i in range(len(words) - 1):
        yield (words[i], words[i + 1])


pairs = make_pairs(words)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(words)

while first_word.islower():
    first_word = np.random.choice(words)

chain = [first_word]


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


replace_values = {"$": "",
                  "@": "",
                  "%": "",
                  "&": "",
                  "#": "",
                  "^": "",
                  "§": ""}


def generator_text(size=100):
    for i in range(size):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    str_res = ' '.join(chain)
    res = multiple_replace(str_res, replace_values)
    print(res)


if __name__ == "__main__":
    generator_text()
