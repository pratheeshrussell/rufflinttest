from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    x = make_three_adders()
    return {"message": str(x)}

def make_three_adders():
    result = []
    for i in [10, 20, 30]:
        def add(x):
            return x + i
        result.append(add)
    return result