from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/user/{user}/pass/{contra}")
def loggin(user:str,contra:str):
        token=""
        if (user=="camilo" and contra=="123456789"):
                token="VALIDO"
        else:
                token="NO VALIDO"
        return{token}
