# movie_recommendation_system



## Installation Guide

1. Fetching project uri
```bash
git clone <url>
```

2. Creating Conda Environment
```bash
conda create -p venv python==3.12 -y
```

3. Activate conda environment
```bash
conda activate venv/
```

4. Installing Requirements
```bash
pip install -r requirements.txt
```

5. Run Fastapi server
```bash
uvicorn api.app:app
```