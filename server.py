from fastapi import FastAPI
import uvicorn

app = FastAPI()

wordCounter = dict()

@app.get("/word-counter/get/{word}")
async def get_word_count(word):
    global wordCounter
    
    count = '0'

    if word in wordCounter:
        count = str(wordCounter[word])

    return {'count': count}

if __name__ == "__main__":
    uvicorn.run('server: app', host="0.0.0.0", port=8000, reload=True)