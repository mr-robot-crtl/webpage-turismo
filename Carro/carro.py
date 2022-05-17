#from ipaddress import v4_int_to_packed
#from multiprocessing.sharedctypes import Value


class Carro:
    #niciar la sesion
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro
    def agregar(self, categoriaservicio):
        if(str(categoriaservicio.id) not in self.carro.keys()):
            self.carro[categoriaservicio.id]={
                "categoriaservicio_id":categoriaservicio.id,
                "nombre":categoriaservicio.nombre,
                "image":categoriaservicio.image.url,
                "descripcion":categoriaservicio.descripcion,
                "precio":str(categoriaservicio.costo),
                "cantidad":1
            }
        else:
            for key, value in self.carro.items():
                if key==str(categoriaservicio.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+categoriaservicio.costo
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, categoriaservicio):
        categoriaservicio.id=str(categoriaservicio.id)
        if categoriaservicio.id in self.carro:
            del self.carro[categoriaservicio.id]
            self.guardar_carro()
    
    def restar(self, categoriaservicio):
        for key, value in self.carro.items():
            if key==str(categoriaservicio.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-categoriaservicio.costo
                if  value["cantidad"]<1:
                    self.eliminar(categoriaservicio)
                break
        self.guardar_carro()
    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True



