from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World"}

@app.get("/home")
def home():
    return {"message" : "Home Page"}

# Step 1 : 터미널창에 "pip install fastapi uvicorn[standard]" 입력
# Step 2 : 경우에 따라서 "python.exe -m pip install --upgrade pip" 입력 필요 (pip 업데이트)


# 실행 방법 : 터미널창에 "uvicorn main:app --reload" 입력
#             이후 로그에 있는 "http://127.0.0.1:8000" 클릭

# 종료 방법 : 터미널창에서 "Ctrl + c" 입력력