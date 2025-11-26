from fastapi import FastAPI ,UploadFile
import uvicorn
from utils.csv_loading import extract_csv

app = FastAPI()


@app.post("/assignWithCsv")
def soldier_deployment(file:UploadFile):
    csv_loading = extract_csv(file)
    sorted_list = sorted(csv_loading, key=lambda x: int(x[5]))
    return sorted_list




if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
