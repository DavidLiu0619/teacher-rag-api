#!/bin/bash

curl http://localhost:5003/

# Test the Flask app running on localhost:5002
curl -H "Content-Type: application/json" -X POST -d '{"question":"What are the learning objectives for Lesson 1?"}' "http://localhost:5003/ask"

curl -H "Content-Type: application/json" -X POST -d '{"question":"What are the recources for Lesson 1?"}' "http://localhost:5003/ask"

# Test the Flask app running on Google Cloud Run
curl -X POST "https://teacher-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"What are the learning objectives for Lesson 1?"}'

curl -X POST "https://teacher-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"I am looking for clubs related to technology and innovation. Can you suggest some?"}'




