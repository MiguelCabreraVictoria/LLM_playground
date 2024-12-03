
## What is an LLM? 

An LLM is neironal network designed to understand, generate and respond to human like text. These models are deep networks trained on massive amount of text data.

LLms utilize an architecture called transformer, which allows them to pay selective attention to different parts of the input when making predictions, since LLMs are capable of generating text, LLMs are also often referred to as a form of generative AI

LLMs may be used for effective knowledge retrieval from vast volumes of text in specialized areas, in short LLMs are invluable for automating almost any task that involves parsing and generating text.

Using custom-built LLMs offers several advantages, particularly regarding data privacy

LLMs use self-supervised learning, where the model generates its own labels from the input data.

After obtaining a pretrained LLM from training on large text datasets, where the LLM is trained to predict the next word in the text, we can further train the LLM on labeled data, also known as fine-tuning


## Transformer architecture

Deep neuronal network architecture 

- Submodules
 - Encoder
  - Processes the input text and encodes it into series of numerical representations or vectors that capture the contextual information of the input
 - Decoder
  - Takes the encoded vectors and generates the output text

Both encoder and decoder consist of many layers connected by so-called self-attention mechanism 

The self-attention mechanism allows the model to weight the importance of different words or tokens in a sequence relative to each other, enabling to capture long-range dependencies and contextual relationships within the input data.


## Chapter Two: Working with text data

> Word embeddings

- Converting data into vector format (map points in a continuos vector space)
- embeddings size often referred to as the dimensionality of the model's hidden state

> Byte Pair encoding

- The algorithm underlying BPE breaks down the words that aren`tin its predifined vocahulary into smaller subwords units or even individual characters, enabling it to handle out-of-vocabulary words
- BPE if the tokenizer encounters an unfamiliar word during tokenization, it can represent it as a sequence of subword tokens or characters

> Data sampling with sliding window

- Input-target pairs 

> Token embeddings

- Embeddings weights with random values
- Continuos vector is neccessary since deep neuronal network train with backpropagation 
- LLM self-attention mechanism doesn't have notion of position or order for tokens within a sequence

> Encoding word positions

- Self-attention of LLMs itself is also position-agnostic, it is helpful to inject additional position information
- Relative positional embeddings: Relative position or distance between tokens
 - the model learns the relationship in terms of "how far apart" rather than "at wchih exact position"
 - The model can generalize better sequences of varying lenghts, even if it hasn't seen such lenghts during training.
- Absolute positional embeddings: specific positions in a sequence
  - For each position in the input sequence, a unique embedding is added to the token's embedding to convey its exact location

- Both types of positional embeddings aim to augment the capacity of LLMs to understand the order or relationship between tokens, ensuring more accurate and context-aware predictions

- For a GPT model's absolute embedding approach, we just need to create another emebedding layer that has the same embedding dimemsion as the token_embedding_layer

