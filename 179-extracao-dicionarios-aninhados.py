# Extração de dicionários aninhados

from pydash import py_

item = {
    "TV":{
        "Mostruário":{
            "LG":"29p",
            "Philips":"32p"
        },
    "Estoque":{
        "Sony":"29p",
        "LG":"32p"
    }
    }
}

print(item["TV"]["Estoque"]["LG"]) # Método convencional
print(py_.get(item, "TV.Estoque.LG"))