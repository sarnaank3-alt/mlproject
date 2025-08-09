from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=130, min_length=30, do_sample=False):
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        return summary[0]['summary_text']

    def summarize_conversation_history(self, conversation_history, max_length=200):
        combined_text = " ".join(conversation_history)
        return self.summarize(combined_text, max_length=max_length)