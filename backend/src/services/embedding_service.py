from langchain.embeddings import OpenAIEmbeddings
from typing import List
import os


class EmbeddingService:
    def __init__(self):
        # Initialize OpenAI embeddings
        # For production use, you should have the OPENAI_API_KEY in environment variables
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        self.embeddings = OpenAIEmbeddings()
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding for a single text."""
        return self.embeddings.embed_query(text)
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts."""
        return self.embeddings.embed_documents(texts)
    
    def similarity_search_by_vector(self, query_embedding: List[float], top_k: int = 4):
        """This would be used with a vector store to find similar content."""
        # This is a placeholder - in practice this would interact with a vector store
        # like Qdrant to find similar content based on the embedding
        pass