import random
import re

class MarkovChain:
    def __init__(self, n):
        self.n = n
        self.ngrams = {}

    def train(self, text):

        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

        for sentence in sentences:
            if len(sentence) < self.n + 1:
                continue
            for i in range(len(sentence) - self.n):
                gram = sentence[i:i + self.n]
                next_char = sentence[i + self.n]
                if gram in self.ngrams:
                    self.ngrams[gram].append(next_char)
                else:
                    self.ngrams[gram] = [next_char]

    def generate_text(self, length):

        seed = random.choice(list(self.ngrams.keys()))
        current = seed
        text = seed

        while len(text) < length:
            if current in self.ngrams:
                next_char = random.choice(self.ngrams[current])
                text += next_char
                current = current[1:] + next_char
            else:
                break

        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        generated_text = ''
        total_length = 0
        for sentence in sentences:
            if total_length + len(sentence) <= length:
                generated_text += sentence + ' '
                total_length += len(sentence) + 1
            else:
                break

        return generated_text.strip()

if __name__ == "__main__":

    file_path = '/content/texts.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    n = 5
    markov_chain = MarkovChain(n)
    markov_chain.train(input_text)

    generated_text = markov_chain.generate_text(length=1000)
    print(generated_text)
