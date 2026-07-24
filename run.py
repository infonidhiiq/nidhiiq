import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.app.main import app

if __name__ == "__main__":
    import uvicorn
    print("[NidhiIQ] Starting NidhiIQ PolicyBazaar Financial Engine on http://127.0.0.1:8000...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
