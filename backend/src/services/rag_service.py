from qdrant_client import QdrantClient
from qdrant_client.http import models
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
import os
from typing import List, Optional


class RAGService:
    def __init__(self):
        # Initialize Qdrant client
        self.client = QdrantClient(
            host=os.getenv("QDRANT_HOST", "localhost"),
            port=int(os.getenv("QDRANT_PORT", 6333)),
        )
        
        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings()
        
        # Specify the collection name for textbook content
        self.collection_name = "textbook_content"
        
        # Create collection if it doesn't exist
        self._ensure_collection_exists()
    
    def _ensure_collection_exists(self):
        """Ensure the Qdrant collection exists with proper configuration."""
        try:
            # Try to get collection info to see if it exists
            self.client.get_collection(self.collection_name)
        except:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
            )
    
    def add_texts(self, texts: List[str], metadatas: Optional[List[dict]] = None, ids: Optional[List[str]] = None):
        """Add texts to the Qdrant collection."""
        # Generate embeddings for the texts
        embedding_vectors = [self.embeddings.embed_query(text) for text in texts]
        
        # Prepare points for Qdrant
        points = []
        for i, (text, embedding) in enumerate(zip(texts, embedding_vectors)):
            point_id = ids[i] if ids else str(i)
            metadata = metadatas[i] if metadatas else {}
            
            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload={
                        "content": text,
                        **metadata
                    }
                )
            )
        
        # Upload points to Qdrant
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
    
    def similarity_search(self, query: str, k: int = 4, filter: Optional[models.Filter] = None) -> List[dict]:
        """Search for similar content in the Qdrant collection."""
        query_embedding = self.embeddings.embed_query(query)
        
        search_results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=k,
            query_filter=filter,
            with_payload=True
        )
        
        results = []
        for result in search_results:
            results.append({
                "content": result.payload["content"],
                "score": result.score,
                "metadata": {k: v for k, v in result.payload.items() if k != "content"}
            })
        
        return results