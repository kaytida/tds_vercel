from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [{"name":"REJa16f","marks":27},{"name":"ml6nB","marks":66},{"name":"4VIo","marks":11},{"name":"cqFesY","marks":92},{"name":"Z","marks":35},{"name":"2bfn","marks":25},{"name":"1nwanQhVqj","marks":68},{"name":"ORLtQV","marks":60},{"name":"w8eBl","marks":82},{"name":"hDqa","marks":27},{"name":"I6jueXgh8","marks":54},{"name":"9XeQn","marks":42},{"name":"WWPupcTJX5","marks":88},{"name":"8RssBGVH","marks":19},{"name":"b9mL5","marks":8},{"name":"qPP6OzD","marks":95},{"name":"7qiGcvxm","marks":75},{"name":"BDLG32P1w","marks":14},{"name":"Gqr3ZJC","marks":34},{"name":"Zv5p7z9cw","marks":21},{"name":"FczOkj9Ni","marks":72},{"name":"iMcXB","marks":77},{"name":"RRJrMiC","marks":29},{"name":"vviw","marks":1},{"name":"JQgNvtG","marks":11},{"name":"iF","marks":34},{"name":"KiR8Q","marks":67},{"name":"rA4gOVl","marks":98},{"name":"3","marks":21},{"name":"AWNHj1gup","marks":84},{"name":"DFwT","marks":63},{"name":"KGGnnB","marks":37},{"name":"4mUt","marks":55},{"name":"Hjcx","marks":97},{"name":"farpTGU7","marks":35},{"name":"zcGoHm","marks":16},{"name":"JzVvf2ut","marks":75},{"name":"5Mnkn1KQ4","marks":64},{"name":"47o","marks":3},{"name":"G","marks":69},{"name":"8iddJsK","marks":41},{"name":"74tfiTXUF","marks":27},{"name":"KrRFF2lglP","marks":36},{"name":"MTGLO","marks":41},{"name":"dwb6G","marks":21},{"name":"0jMVoa","marks":75},{"name":"Bz8g","marks":20},{"name":"PTsU313IR4","marks":15},{"name":"xW","marks":28},{"name":"8N3Osrzg","marks":50},{"name":"rDiFKYQME","marks":68},{"name":"geQ4noeC93","marks":7},{"name":"sxcb","marks":21},{"name":"qqYeTp","marks":23},{"name":"Ht","marks":9},{"name":"UtSsgBBfp","marks":17},{"name":"TpdhvWRu","marks":9},{"name":"P","marks":55},{"name":"bfd2KzV29a","marks":54},{"name":"SY6lHtcER","marks":64},{"name":"Z4sWhIt3Gh","marks":8},{"name":"BCkOqXMzLW","marks":70},{"name":"5RY","marks":66},{"name":"cEgCAKm9H","marks":78},{"name":"yaWD6","marks":72},{"name":"a8Utf4b","marks":82},{"name":"D","marks":37},{"name":"d","marks":54},{"name":"K05ElLra","marks":69},{"name":"QDDo6YZ","marks":19},{"name":"k2Iez","marks":59},{"name":"C5SC","marks":65},{"name":"qOnfrMbXGn","marks":40},{"name":"i","marks":94},{"name":"UpO8tm","marks":66},{"name":"PqGdg","marks":4},{"name":"k","marks":59},{"name":"e0j0p","marks":84},{"name":"lW","marks":30},{"name":"DHlK","marks":86},{"name":"JB1z","marks":15},{"name":"QJFH194m","marks":13},{"name":"Amy","marks":16},{"name":"JH9SxIt9Eu","marks":91},{"name":"dw","marks":53},{"name":"Z0GQcDLs","marks":53},{"name":"XZBetF6D","marks":29},{"name":"hLupLThAA","marks":75},{"name":"ZzVIq","marks":63},{"name":"13UTN7v9b","marks":49},{"name":"vpAVuJNH","marks":27},{"name":"kBP5jMkb7","marks":27},{"name":"mAJ","marks":90},{"name":"WeG2fbG","marks":99},{"name":"Q0jZHhC","marks":75},{"name":"K6xSA","marks":24},{"name":"H2qS","marks":73},{"name":"dP47tm","marks":44},{"name":"Dw","marks":88},{"name":"a","marks":28}]

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [next((s["marks"] for s in students_data if s["name"] ==n), None) for n in name]
        return {"marks": marks}
    return {"marks": []}
