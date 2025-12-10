#!/usr/bin/env python3
"""
Content indexing script for initial textbook chapters.
This script reads the textbook content and indexes it in Qdrant for RAG operations.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the backend/src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.services.rag_service import RAGService
from src.config import settings


async def index_textbook_content():
    """Index all textbook content into the RAG system."""
    print("Starting textbook content indexing...")
    
    # Initialize RAG service
    rag_service = RAGService()
    
    # For this initial implementation, we'll simulate indexing
    # In a real implementation, we would read from actual textbook files
    textbook_content = [
        {
            "id": "chapter-1-intro-physical-ai",
            "title": "Introduction to Physical AI",
            "content": "# Introduction to Physical AI\n\nPhysical AI is a field that combines physical systems with artificial intelligence. It focuses on creating intelligent systems that can interact with the physical world in a meaningful way. This chapter introduces the fundamental concepts and principles of Physical AI."
        },
        {
            "id": "chapter-2-basics-humanoid",
            "title": "Basics of Humanoid Robotics",
            "content": "# Basics of Humanoid Robotics\n\nHumanoid robotics is a branch of robotics focused on creating robots with human-like characteristics. This chapter covers the basic principles of humanoid design, kinematics, and control systems."
        },
        {
            "id": "chapter-3-ros-fundamentals",
            "title": "ROS 2 Fundamentals",
            "content": "# ROS 2 Fundamentals\n\nROS 2 (Robot Operating System 2) is a flexible framework for writing robot software. This chapter covers the basics of ROS 2 including nodes, topics, services, and actions."
        },
        {
            "id": "chapter-4-digital-twin",
            "title": "Digital Twin Simulation (Gazebo + Isaac)",
            "content": "# Digital Twin Simulation\n\nDigital twin technology allows creating virtual replicas of physical systems. This chapter explores simulation using Gazebo and Isaac for robotics applications."
        },
        {
            "id": "chapter-5-vla-systems",
            "title": "Vision-Language-Action Systems",
            "content": "# Vision-Language-Action Systems\n\nVision-Language-Action (VLA) systems integrate visual perception, language understanding, and physical action. This chapter covers how these systems work together in robotics applications."
        },
        {
            "id": "chapter-6-capstone",
            "title": "Capstone: Simple AI-Robot Pipeline",
            "content": "# Capstone: Simple AI-Robot Pipeline\n\nThis capstone chapter brings together all concepts learned to build a simple AI-robot pipeline, demonstrating the integration of perception, decision-making, and action."
        }
    ]
    
    # Extract text content and prepare metadata for each chapter
    texts = []
    metadatas = []
    ids = []
    
    for chapter in textbook_content:
        texts.append(chapter["content"])
        metadatas.append({
            "title": chapter["title"],
            "chapter_id": chapter["id"],
            "source": "textbook"
        })
        ids.append(chapter["id"])
    
    # Add the content to the RAG service
    print(f"Indexing {len(texts)} chapters...")
    rag_service.add_texts(texts, metadatas, ids)
    
    print("Textbook content indexing completed successfully!")


if __name__ == "__main__":
    asyncio.run(index_textbook_content())