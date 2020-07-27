var res = response.content.asJSON;

var new_res = {
    "totalRecords": res["recordsTotal"],
    "stocks": []
};

for (var i=0; i<res["data"].length; i++) {
    new_res["stocks"].push({
        "name": res["data"][i]["name"]["originalValue"],
        "wkn": res["data"][i]["wkn"],
        "isin": res["data"][i]["isin"],
    })
}

response.content = JSON.stringify(new_res, null, 2);