from fastapi import FastAPI ,UploadFile
import uvicorn
from utils.csv_loading import extract_csv
import models.management
from utils.Creating_objects import creating_soldier_objects


app = FastAPI()


@app.post("/assignWithCsv")
def soldier_deployment(file:UploadFile):
    csv_loading = extract_csv(file)
    sorted_list_soldiers = sorted(csv_loading, key=lambda x: int(x[5]))
    list_of_objects = creating_soldier_objects(sorted_list_soldiers)
    m = models.management.Management(list_of_objects)
    m.fill_the_houses()
    return m.soldier_deployment_details()


@app.get("/waitingLis")
def return_of_waiting_list():
    return





if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
