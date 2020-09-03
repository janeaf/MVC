import web
import mvc.models.model as alumnos
render = web.template.render("mvc/views/alumnos/", base="template")
model_alumnos = alumnos.Alumnos()
class Update():

    def GET(self, Matricula):
        try:
            
         result = model_alumnos.view(Matricula)[0]
            #print(result)
            return render.update(result) 
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self, Matricula):
        try:
            form = web.input()
            Matricula = form.Matricula
            Nombre = form.Nombre
            lastname = form.lastname
            lastname2 = form.lastname2
            Edad = form.Edad
            Fecha = form.Fecha
            Sexo = form.Sexo
            Estado = form.Estado
            result = model_alumnos.update(Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado)
            web.seeother('/list')
        except Exception as e:
            return "Error " + str(e.args)
