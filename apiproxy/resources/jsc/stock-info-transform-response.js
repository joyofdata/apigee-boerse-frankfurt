var res = response.content.asJSON;

function get_value(obj) {
    return (
        obj.translations.en || 
        obj.translations.others || 
        obj.translations.de || 
        obj.originalValue
    ).toLowerCase();
}

var new_res = {
    "isin": res.isin,
    "market": get_value(res.market),
    "segment": get_value(res.segment),
    "industrySector": get_value(res.industrySector),
    "instrumentType": get_value(res.instrumentType),
    "securityType": get_value(res.securityType),
    "originCountry": get_value(res.originCountry),
    "sector": get_value(res.sector),
    "subSector": get_value(res.subsector), // different spelling
};

response.content = JSON.stringify(new_res, null, 2);