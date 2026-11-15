from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict] = [
    {
    "id":1,
    "author": "Ayoub M",
    "title": "Learn SQL With Me",
    "content": "I use this list of resources to learn SQL..."
     },
    {
    "id":2,
    "author": "Jensen Huang",
    "title": "I did it",
    "content": "I did things one two three"
     }
]
@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/posts/{post_id}" ,include_in_schema=False)
def get_post_page(post_id: int, request: Request):
    for post in posts:
        if post["id"] == post_id:
            return templates.TemplateResponse(request, "post.html", {"post": post})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int) -> dict:
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/signup", include_in_schema=False)
def signup(request: Request):
    return templates.TemplateResponse(request, "signup.html", {"title": "Signup"})

@app.get("/login", include_in_schema=False)
def logi(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": "Login"})