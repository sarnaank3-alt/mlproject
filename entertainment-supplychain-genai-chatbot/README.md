# Entertainment Supply Chain Generative AI Chatbot

This project implements an enterprise-ready Generative AI chatbot tailored for the entertainment supply chain, including studios, distributors, vendors, post-production, and rights management. The chatbot utilizes Retrieval-Augmented Generation (RAG) for knowledge retrieval, integrates OpenAI's language models, and is deployable on AWS with a Streamlit UI.

## Overview

The chatbot is designed to assist users in navigating complex queries related to the entertainment supply chain. It leverages document embeddings and a vector index for efficient retrieval of information, ensuring accurate and contextually relevant responses.

## Architecture

The architecture consists of several components, including:

- **Streamlit UI**: A user-friendly interface for interacting with the chatbot.
- **Backend Microservices**: Responsible for processing requests, managing the RAG pipeline, and interfacing with the database and vector store.
- **AWS Infrastructure**: Utilizes services such as S3 for storage, RDS for database management, ECS for container orchestration, and Lambda for serverless functions.

Refer to the architecture diagrams located in the `architecture` directory for detailed visual representations of the system components and their interactions.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd entertainment-supplychain-genai-chatbot
   ```

2. **Infrastructure Deployment**:
   - Navigate to the `infra/terraform` directory.
   - Run the following commands to deploy the infrastructure:
     ```
     terraform init
     terraform apply
     ```

3. **Build and Deploy the Application**:
   - Navigate to the `infra` directory and run the deployment script:
     ```
     ./deploy.sh
     ```

4. **Access the Streamlit UI**:
   - Once deployed, access the Streamlit UI at the provided endpoint.

## Usage Guidelines

- **Interacting with the Chatbot**: Users can input queries related to the entertainment supply chain. The chatbot will provide sourced answers and may ask follow-up questions for clarification.
- **Feedback Mechanism**: Users can provide feedback on responses, which will be logged for future improvements.
- **Monitoring and Metrics**: The application includes monitoring capabilities via CloudWatch, allowing for tracking of performance metrics and user interactions.

## Testing

The project includes unit and integration tests to ensure the reliability of the components. Tests can be found in the `tests` directory. To run the tests, use the following command:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.