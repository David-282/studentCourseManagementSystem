from fastapi import FastAPI

from routes import student_router, facilitator_router

app = FastAPI()


app.include_router(student_router.router)
app.include_router(facilitator_router.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
