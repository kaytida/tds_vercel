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
students_data = [{"name":"REJa16f","marks":71},{"name":"dml","marks":53},{"name":"nBpY4VIoHk","marks":73},{"name":"qFesY","marks":37},{"name":"AZVX2bfnP9","marks":41},{"name":"nwanQhVqj","marks":2},{"name":"hORLtQV","marks":48},{"name":"Yw8eBly","marks":73},{"name":"hDqa","marks":8},{"name":"zI6","marks":94},{"name":"ueXgh8","marks":5},{"name":"Z9XeQn","marks":29},{"name":"3WWPu","marks":83},{"name":"cTJX52w","marks":54},{"name":"RssBGVHMbb","marks":17},{"name":"mL5EnqPP6O","marks":74},{"name":"D7w7qiGcv","marks":66},{"name":"muxBDLG32","marks":18},{"name":"1wI","marks":30},{"name":"Gqr3ZJC","marks":53},{"name":"2Zv5","marks":0},{"name":"7z9cwN3","marks":1},{"name":"c","marks":75},{"name":"Okj9Nisci","marks":43},{"name":"cXB","marks":40},{"name":"mRRJrMiC","marks":82},{"name":"Yvv","marks":34},{"name":"wApJQg","marks":13},{"name":"vtG","marks":69},{"name":"Ki","marks":63},{"name":"V","marks":83},{"name":"KiR8Q","marks":85},{"name":"nrA4gOV","marks":88},{"name":"8F3N2AW","marks":33},{"name":"Hj1","marks":32},{"name":"up0TDF","marks":22},{"name":"TniKGGnn","marks":95},{"name":"W","marks":76},{"name":"4mUt","marks":98},{"name":"UHjcx8","marks":44},{"name":"farpTGU7","marks":49},{"name":"izcG","marks":74},{"name":"HmKwJzV","marks":76},{"name":"f2utu15M","marks":66},{"name":"kn1KQ4o","marks":0},{"name":"47o","marks":34},{"name":"B","marks":75},{"name":"rr","marks":15},{"name":"iddJsKZz74","marks":21},{"name":"fiTXUFR6","marks":12},{"name":"rR","marks":27},{"name":"F","marks":85},{"name":"lglPWZMTG","marks":59},{"name":"OZ","marks":3},{"name":"dwb6G","marks":25},{"name":"k0j","marks":92},{"name":"Vo","marks":57},{"name":"uWBz8","marks":19},{"name":"M8PTsU","marks":58},{"name":"13IR4JKxW","marks":43},{"name":"v8N","marks":95},{"name":"Osrzgf0rD","marks":27},{"name":"FKYQME","marks":21},{"name":"6geQ4no","marks":61},{"name":"C93EV","marks":0},{"name":"xcbNiqqY","marks":14},{"name":"TpOGH","marks":90},{"name":"FzUtSsgB","marks":66},{"name":"f","marks":36},{"name":"LtTpdhv","marks":48},{"name":"RuFC","marks":9},{"name":"i4b","marks":88},{"name":"d2KzV2","marks":50},{"name":"ah0SY6lHtc","marks":44},{"name":"R","marks":10},{"name":"7Z4sWhI","marks":99},{"name":"3GhF8BCk","marks":61},{"name":"qXM","marks":25},{"name":"LWrQ5RYp3","marks":84},{"name":"EgCAK","marks":58},{"name":"9HweyaW","marks":41},{"name":"6","marks":11},{"name":"oa8Utf4b","marks":54},{"name":"ADWCdiuK0","marks":4},{"name":"ElLrarpQDD","marks":75},{"name":"6YZLck2","marks":49},{"name":"ez","marks":16},{"name":"XC5SCo","marks":94},{"name":"qOnfrMbXGn","marks":80},{"name":"Ci6iU","marks":30},{"name":"O8tmpaP","marks":0},{"name":"GdgDBkk","marks":24},{"name":"e0j0p","marks":34},{"name":"HlWTVDHlK","marks":11},{"name":"VJB1zJsQJ","marks":87},{"name":"H","marks":67},{"name":"94mIOAmyK","marks":30},{"name":"JH9SxIt9Eu","marks":73},{"name":"JdwhvZ0GQc","marks":57},{"name":"L","marks":47}]

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
