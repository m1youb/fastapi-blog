from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict] = [
    {
    "id":1,
    "author": "Ayoub Miane",
    "title": "Learn SQL With Me",
    "content": "I use this list of resources to learn SQL..."
     },
    {
    "id":2,
    "author": "Jensen Huang",
    "title": "I F*cked Up",
    "content": "I cheated on my wife with a chinese model"
     }
]
@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts