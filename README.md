---
sdk: docker
---
# Customer Support Bot 

This is a FastAPI + Gemini-powered customer support assistant, deployed with Docker on Hugging Face Spaces.

## Tech Stack
- FastAPI (backend API)
- LangChain + Gemini 1.5 Flash
- Docker for deployment

## Run locally
```bash
uvicorn api:app --reload
```
## Deployment
    This Space runs in Docker mode with:
    ```bash
    CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
    ```
    
