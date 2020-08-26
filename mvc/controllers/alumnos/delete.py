import web

render = web.template.render("mvc/views/alumnos/", base="template")

class Delete():

    def GET(self):
        try:
            return render.delete() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
        
        
    def POST(self, Matricula):
        try:
            form = web.input()
            Matricula = form['Matricula']
            result = model_alumnos.delete(Matricula)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"
