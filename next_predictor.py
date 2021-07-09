import numpy as np

lexicon = {}

def update_lexicon(current : str, next_word : str) -> None:

    if current not in lexicon:
        lexicon.update({current: {next_word: 1} })
        return
    options = lexicon[current]
    if next_word not in options:
        options.update({next_word : 1})
    else:
        options.update({next_word : options[next_word] + 1})
    lexicon[current] = options

def ajust_probability() -> None:
    for word, transition in lexicon.items():
        transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
        lexicon[word] = transition

def parse_line(line : str) -> None:
    words = line.strip().split(' ')
    for i in range(len(words) - 1):
        update_lexicon(words[i], words[i+1])

def predict(word : str) -> str:
    if word not in lexicon:
        return None
    options = lexicon[word]
    return np.random.choice(list(options.keys()), p=list(options.values()))
    

def load_dataset():

    with open('dataset.txt', 'r') as dataset:
        for raw_line in dataset:
            line = raw_line.split(' ', 5)[-1].strip('\n')
            parse_line(line)
    ajust_probability()

def predict_loop():
    
    while(1):
        
        line = input('> ')
        word = line.strip().split(' ')[-1]
        word = predict(word)

      
        if word is not None:
            print(line +' '+ word)


if __name__ == '__main__':
    load_dataset()
    try:
        predict_loop()
    except (KeyboardInterrupt, EOFError):
        pass