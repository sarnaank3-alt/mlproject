# Vector Store Integration Documentation

This directory contains the implementation and documentation for the vector store integration used in the entertainment supply chain Generative AI chatbot project. The vector store is responsible for managing document embeddings and facilitating knowledge retrieval through efficient querying.

## Overview

The vector store is designed to support the retrieval-augmented generation (RAG) pipeline by storing embeddings of documents and allowing for quick access to relevant information based on user queries. This integration is crucial for providing accurate and contextually relevant responses in the chatbot.

## Components

- **driver.py**: This file implements the core functionality for interacting with the vector store, including methods for adding embeddings and querying the store.
- **schema.sql**: This file defines the database schema for the vector store, outlining the structure of the tables and relationships necessary for storing embeddings and associated metadata.

## Setup Instructions

1. **Database Setup**: Ensure that the vector store database is created using the schema defined in `schema.sql`. You can execute the SQL commands in a compatible database management system.

2. **Integration**: The `driver.py` file should be imported and utilized within the RAG pipeline to handle embedding storage and retrieval.

3. **Configuration**: Update any necessary configuration settings in the main application to connect to the vector store.

## Usage Guidelines

- Use the methods provided in `driver.py` to add new document embeddings and to perform queries based on user input.
- Ensure that the embeddings are generated using a consistent method to maintain accuracy in retrieval.

## Testing

Make sure to run the unit tests associated with the vector store integration to verify that all functionalities are working as expected. The tests can be found in the `tests/unit` directory.

## Feedback and Contributions

For any issues or suggestions regarding the vector store integration, please refer to the project's main repository for guidelines on contributing and providing feedback.