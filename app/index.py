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
students_data = [{"name":"sjMG","marks":81},{"name":"sP","marks":35},{"name":"XiqUh","marks":96},{"name":"ythk1DE","marks":59},{"name":"O5m","marks":18},{"name":"kUMqC9","marks":34},{"name":"1t9z9NC1LG","marks":32},{"name":"VeUPyWk5c","marks":87},{"name":"JL5svBo","marks":64},{"name":"U2y","marks":41},{"name":"Y0Qw5ZtE","marks":45},{"name":"PgeGldU5","marks":97},{"name":"N96y","marks":69},{"name":"VXZL7Y","marks":94},{"name":"nfd7","marks":53},{"name":"Mh0","marks":48},{"name":"zxIFGa","marks":51},{"name":"exh","marks":14},{"name":"TS8I5p60b","marks":20},{"name":"jy9","marks":88},{"name":"Bv4xDI","marks":49},{"name":"jAg9uRC8D","marks":52},{"name":"Ubu7KwFXt","marks":44},{"name":"3Wf","marks":74},{"name":"ivo6","marks":18},{"name":"NlV","marks":32},{"name":"oDxjld7","marks":50},{"name":"C36Q","marks":75},{"name":"l","marks":47},{"name":"0q","marks":79},{"name":"9WWnW2","marks":99},{"name":"N7AVJvpm","marks":83},{"name":"opMO4","marks":99},{"name":"1Yz9TDoZ","marks":24},{"name":"8lPNMTE","marks":95},{"name":"L9WkeO","marks":65},{"name":"nB","marks":8},{"name":"CII8nL3d","marks":35},{"name":"j3LuK","marks":57},{"name":"669PyEDzt","marks":8},{"name":"FCjKkFmhyF","marks":27},{"name":"hcmHpU","marks":84},{"name":"SiyliAf","marks":74},{"name":"xK6GwLMU","marks":45},{"name":"lVkbXCq","marks":87},{"name":"AAXiADy6L","marks":13},{"name":"2r","marks":2},{"name":"MGIYJPFYeO","marks":97},{"name":"Utf30y9","marks":76},{"name":"G","marks":77},{"name":"HStVO1aodn","marks":89},{"name":"qsBTFOxX8","marks":89},{"name":"lunnz","marks":19},{"name":"K7TiRSHmZS","marks":17},{"name":"lVKDEy","marks":92},{"name":"44rkllj4","marks":40},{"name":"dkIF","marks":82},{"name":"8vse","marks":23},{"name":"Q","marks":34},{"name":"vJH","marks":67},{"name":"1TZg95REkl","marks":52},{"name":"kOoyHUF","marks":4},{"name":"VNmjWu","marks":49},{"name":"8ta7K6Vsw","marks":97},{"name":"7Y72ihd1E","marks":18},{"name":"TrXW1zY5","marks":66},{"name":"lCbohAL","marks":64},{"name":"tQb8Aw","marks":68},{"name":"OE0YvTDS","marks":27},{"name":"JZ77JS","marks":3},{"name":"Vg5M","marks":7},{"name":"SZ8woIx","marks":8},{"name":"dN","marks":76},{"name":"9rYTaxKhMU","marks":55},{"name":"weOHa4","marks":63},{"name":"MXYmlc","marks":17},{"name":"o1","marks":38},{"name":"3u5X5828y","marks":38},{"name":"i","marks":69},{"name":"rs","marks":20},{"name":"yhS0T70F","marks":70},{"name":"Yxx6uP5","marks":23},{"name":"Kb","marks":79},{"name":"UpiF3n","marks":91},{"name":"84e","marks":80},{"name":"en6gzB5j8","marks":12},{"name":"cV","marks":71},{"name":"mNymDl1WKc","marks":60},{"name":"vMpi","marks":41},{"name":"vJo0je","marks":41},{"name":"lhcpI7LBr","marks":43},{"name":"2qvue0j9l","marks":43},{"name":"yDLf0aYb5","marks":34},{"name":"XBx","marks":3},{"name":"O1sF1bVXEJ","marks":74},{"name":"N","marks":89},{"name":"FxYO3l","marks":48},{"name":"hU1urjTzTM","marks":64},{"name":"C","marks":15},{"name":"V","marks":26}]

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
