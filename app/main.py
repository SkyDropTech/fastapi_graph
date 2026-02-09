from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import engine, SessionLocal
from .models import Revenue, Base

app = FastAPI(title="Revenue Dashboard")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/api/revenue")
def revenue_data():
    db = SessionLocal()
    data = db.query(Revenue).all()
    db.close()

    return {
        "labels": [d.month for d in data],
        "values": [d.value for d in data]
    }
