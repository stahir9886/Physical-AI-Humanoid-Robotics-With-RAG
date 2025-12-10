<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Added sections: All principles and sections for Physical AI & Humanoid Robotics textbook project
Removed sections: None
Modified templates: N/A
Deferred items: None
-->
# Physical AI & Humanoid Robotics — Essentials Constitution

## Core Principles

### Simplicity
All features and implementations must follow the KISS principle (Keep It Simple, Stupid). Complex solutions are only acceptable when they provide measurable benefits that outweigh the added complexity. Code readability and maintenance take precedence over clever implementations.

### Accuracy  
All content and code examples must be factually correct and properly tested. Information accuracy is paramount as this serves as an educational resource. Any experimental or preliminary content must be clearly marked as such.

### Minimalism
Only essential features and dependencies should be included. Each addition must justify its inclusion with clear educational value. Extraneous code, libraries, or features that do not contribute to the learning objectives should be removed.

### Fast Builds
The Docusaurus textbook must maintain quick build times to enable rapid iteration and development. Build optimizations are required when additions would significantly slow the build process. Continuous integration pipelines must maintain acceptable build times.

### Free-tier Architecture
All architecture decisions must consider cost implications and prioritize free-tier friendly solutions. Resource usage should be optimized to remain within free tier limits of cloud services. Solutions should be scalable but not wasteful of resources.

### RAG Answers ONLY from Book Text
The RAG chatbot must exclusively draw responses from the book's content. No external sources or hallucinated information should be provided. This ensures accuracy and consistency with the educational material.

## Additional Constraints and Requirements

The project must adhere to the following constraints:
- No heavy GPU usage during normal operation; computation should be lightweight and accessible
- Minimal embeddings that can be hosted on free-tier infrastructure  
- Clean, professional UI using Docusaurus framework
- Smooth deployment to GitHub Pages
- Content limited to 6 chapters covering: Introduction to Physical AI, Basics of Humanoid Robotics, ROS 2 Fundamentals, Digital Twin Simulation, Vision-Language-Action Systems, and Capstone: Simple AI-Robot Pipeline

## Development Workflow and Quality Standards

The development process must follow these standards:
- All content and code must be well-documented and reviewed
- Pull requests must include verification of build success and accurate chatbot functionality
- New features must pass integration tests with the RAG system
- Code reviews must verify compliance with all core principles
- Deployment pipeline must successfully build and deploy to GitHub Pages

## Governance
This constitution guides all development decisions for the Physical AI & Humanoid Robotics textbook. All changes to the project must align with the stated principles. Deviations require explicit justification and formal approval. All pull requests and reviews must verify compliance with these principles. This constitution supersedes any conflicting practices.

**Version**: 1.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10