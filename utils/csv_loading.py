import csv
import io

def extract_csv(file):

    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}

    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    next(reader)
    rows = list(reader)

    return rows

