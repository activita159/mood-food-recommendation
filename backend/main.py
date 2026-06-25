from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import favorites, recommendations, restaurants


app = FastAPI(title="Mood Food Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurants.router, prefix="/api/restaurants", tags=["restaurants"])
app.include_router(
    recommendations.router,
    prefix="/api/recommendations",
    tags=["recommendations"],
)
app.include_router(favorites.router, prefix="/api/favorites", tags=["favorites"])


@app.get("/")
def read_root():
    return {"message": "Mood Food API is running"}
