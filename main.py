import sys
import os

# Add root directory to sys.path for clean import resolution on cloud hosts (Render/Railway/Hostinger VPS)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.app.main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
