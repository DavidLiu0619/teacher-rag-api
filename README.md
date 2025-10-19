# Teacher RAG API for Day of AI USA Curriculum

A Retrieval Augmented Generation (RAG) API that provides intelligent responses about the Day of AI USA curriculum content using natural language processing.

## Overview

This project implements a RAG pipeline that combines a vector database with Google's Gemini model to provide accurate, contextual information about the Day of AI USA curriculum. The system processes queries in natural language and returns relevant information by searching through the curriculum content.

## Data Source

The system uses curriculum data from [Day of AI USA Grades 3-5](https://www.dayofaiusa.org/curriculum/grades-3-5). The content is processed and stored in a Chroma vector database for efficient semantic search.

## Repository Structure

| File | Description |
|------|-------------|
| `rag_pipeline.py` | Core RAG implementation for processing queries |
| `server.py` | Flask server that exposes the RAG endpoints |
| `dayofaiusa_grades3_5_2025-10-15.csv` | Curriculum dataset |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container configuration for deployment |
| `docker-compose.yml` | Local development container orchestration |
| `curl_test.sh` | Example API requests for testing |

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (optional)
- Google Gemini API Key (see [API Key Guide](https://ai.google.dev/gemini-api/docs/api-key))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/teacher-rag-api.git
cd teacher-rag-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key:
```bash
cat > .env <<EOF
GOOGLE_API_KEY=your_actual_gemini_api_key_here
EOF
```

4. Build and run with Docker:
```bash
docker compose up -d
```

## Usage

The API provides endpoints for querying information about the Day of AI USA curriculum. You can use the provided `curl_test.sh` script to test the API endpoints.

Example queries:
```bash
# Check if the server is running
curl http://localhost:5003/

# Ask about learning objectives
curl -H "Content-Type: application/json" -X POST -d '{"question":"What are the learning objectives for Lesson 1?"}' "http://localhost:5003/ask"

# Ask about resources
curl -H "Content-Type: application/json" -X POST -d '{"question":"What are the resources needed for Lesson 1?"}' "http://localhost:5003/ask"
```

You can change some of the values to see the prediction change. Both of the curl commands can be found in the file curl_test.sh. 

Check to see if you have any docker containers running using 
```bash
docker container ls
```

and stop them through 
```bash
docker componse down -v
```

## Architecture

1. **Vector Database**: Uses Chroma DB to store and retrieve curriculum content embeddings
2. **RAG Pipeline**: Implements retrieval-augmented generation to combine retrieved context with Gemini model responses
3. **API Layer**: Exposes the functionality through a REST API

## Development

To contribute to the project:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Day of AI USA](https://www.dayofaiusa.org) for providing the curriculum content
- Google for the Gemini API capabilities
- Chroma for the vector database
- LangChain for the RAG pipeline framework
