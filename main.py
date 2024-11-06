import torch
from summarizer import Summarizer

to_summarize = "The object stores an atomic boolean that dictates whether or not it is ready for handoff, which occurs through another object, the float, to transfer between threads. The data is protected by only allowing the enqueue function go through when the flag is true and the opposite for the dequeue function"

model = Summarizer()

result = model(to_summarize, num_sentences=1)

print(result)