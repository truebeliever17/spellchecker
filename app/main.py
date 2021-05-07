from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    """Displays greeting message in homepage

    Returns:
        dict: a dictionary with greeting message
    """

    return {"message": "✌"}
