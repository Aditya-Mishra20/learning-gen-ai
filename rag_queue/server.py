from fastapi import FastAPI

app = FastAPI()

'''

fastapi server does a post request to /chat and gets a message from the client
then the request goes to queue and wait
the worker(process_query) proecess the requests one by one and stores the result in redis.

'''

@app.get('/')
def root():
    return {"status": 'Server is running!!'}

# @app.post('/chat')
# def chat():
#     pass

