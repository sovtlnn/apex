# Apex Lab — Full Stack

FastAPI server that serves the Apex Lab website.

## Project Structure

```
apexlab/
├── main.py            # FastAPI app
├── requirements.txt   # Python dependencies
├── railway.toml       # Railway deployment config
├── nixpacks.toml      # Build config
├── Procfile           # Fallback start command
├── templates/
│   └── index.html     # The website
└── static/            # Static assets (add CSS/JS/images here later)
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://localhost:8000

## Deploy to Railway

1. Push this folder to a GitHub repository
2. Go to https://railway.app and sign in
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repository
5. Railway auto-detects the config and deploys
6. Your site is live at the Railway-provided URL

## API Endpoints

| Method | Path      | Description          |
|--------|-----------|----------------------|
| GET    | /         | Serves the website   |
| GET    | /health   | Health check         |
