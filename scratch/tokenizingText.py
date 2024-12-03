"""
Learn how to tokenize and covert token into token IDs
"""


import re 
text = "Hello, world. This, is a test."
result = re.split(r'([,.]|\s)', text)

"""
When developing a simple tokenizer, whether we should encode whitespaces as separate characters or just remove them depends on our application and its requirements

"""
result = [item for item in result if item.strip()] # strip(): removes whitespaces
# print(result)



text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
# print(result)


#-----------------------------------

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!()] | -- |\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]


"""

Converting tokens into token IDs

To map the generated token into token IDs, we have to build a vocabulary first. This vocabulary defines how we map each unique word and special character to a unique integer

"""

all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|unk|>", "<|endoftext|>"])
vocab_size = len(all_tokens)

vocab = {token:integer for integer, token in enumerate(all_tokens)}

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s|d+)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [ item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([, . ? ! " ()\'])', r'\1', text)
        return text
    

tokenizer = SimpleTokenizerV1(vocab)
text1 = "Hello, do you like tea? 64"
text2 = """'In the sunlit terraces of the palace'."""
text = " <|endoftext|> ".join((text1, text2))

# Data sampling with sliding window

enc_text = tokenizer.encode(raw_text)
print(len(enc_text))

enc_sample = enc_text[:50]

context_size = 4
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]
print(f"x: {x}")
print(f"y:{y}")



