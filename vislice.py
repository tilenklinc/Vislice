import bottle

import model

vislice = model.Vislice()

@bottle.get("/")
def index():
    return bottle.template("Dokumenti\\2019_20\\UVP\\Git\\Visliceindex.tpl")



bottle.run(reloader=True, debug=True)