import unittest
from app.backend.rag_pipeline.retrieval import DocumentRetriever
from app.backend.rag_pipeline.rerank import DocumentReranker
from app.backend.rag_pipeline.summarizer import DocumentSummarizer

class TestRAGPipeline(unittest.TestCase):

    def setUp(self):
        self.retriever = DocumentRetriever()
        self.reranker = DocumentReranker()
        self.summarizer = DocumentSummarizer()

    def test_document_retrieval(self):
        query = "What are the rights management processes?"
        results = self.retriever.retrieve(query)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

    def test_document_reranking(self):
        documents = [
            {"id": "doc1", "score": 0.8},
            {"id": "doc2", "score": 0.6},
            {"id": "doc3", "score": 0.9}
        ]
        reranked = self.reranker.rerank(documents)
        self.assertEqual(reranked[0]['id'], 'doc3')

    def test_document_summarization(self):
        long_text = "This is a long document that needs to be summarized. " * 10
        summary = self.summarizer.summarize(long_text)
        self.assertLessEqual(len(summary.split()), 60)

if __name__ == '__main__':
    unittest.main()