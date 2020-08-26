import web

render = web.template.render("mvc/views/alumnos/", base="template")

class Update():

    def GET(self):
        try:
            
         result = model_alumnos.view(Matricula)[0]
            #print(result)
            return render.update(result) 
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self, Matricula):
        try:
            form = web.input()
            matricula = form.Matricula
            nombre = form.Nombre
            apellido_paterno = form.lastname
            apellido_materno = form.lastname2
            edad = form.Edad
            fecha_nacimiento = form.Fecha
            sexo = form.Sexo
            estado_civil = form.Estado
            result = model_alumnos.update(Nombre, lastname, lastname, Matricula, Edad, Fecha, Sexo, Estado)
            web.seeother('/list')
        except Exception as e:
            return "Error " + str(e.args)
