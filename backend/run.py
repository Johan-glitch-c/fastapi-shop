import uvicorn
from app.config import settings


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=5173, reload=settings.debug, log_level='info')