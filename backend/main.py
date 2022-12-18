from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_data import get_data

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = get_data()

print(data)

@app.get("/")
def read_root():
    data = get_data()
    print(type(data))
    print(data)
    return {"message": data}
    