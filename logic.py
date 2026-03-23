from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Define the model name
model_name = "sshleifer/distilbart-cnn-12-6"

# Manually load the Tokenizer and the Model
# This avoids the "Unknown task summarization" error
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def get_summary(text, max_len, min_len):
    # 1. Convert text to numbers (Tokens)
    # truncation=True ensures we don't crash if the article is too long
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    # 2. Tells the model to generate a summary
    summary_ids = model.generate(
        inputs["input_ids"], 
        max_length=max_len, 
        min_length=min_len, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )

    # 3. Converts the numbers back into human words
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary