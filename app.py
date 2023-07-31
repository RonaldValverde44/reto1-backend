from flask import Flask,request,render_template
from profile import Profile
from firebase import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()

@app.route('/')
def index():
    perfil = Profile()
    perfil_fb = fb.get_collection('perfil')
    perfil_det = perfil_fb[0]
    experiencia_fb = fb.get_collection('experiencias')
    perfil_exp = experiencia_fb[0]
    formacion_fb = fb.get_collection('formacion')
    perfil_formacion = formacion_fb[0]
    habilidades_fb = fb.get_collection('habilidades')
    perfil_skills = habilidades_fb[0]
    tecnologias_fb = fb.get_collection('tecnologias')
    perfil_tec = tecnologias_fb[0]
    context = {
        'nombre':perfil.name,
        'imagen':perfil.image,
        'rol':perfil.role,
        'ubicacion':perfil.location,
        'url_github':perfil.url_github,
    }
    return render_template('index.html',**context)

@app.route('/acercade')
def acercade():
    perfil_fb = fb.get_collection('perfil')
    perfil_det = perfil_fb[0]
    context = {
        'resumen':perfil_det['resumen'],
        'experiencia':perfil_det['experiencia']
    }
    return render_template('acercade.html',**context)

@app.route('/contacto')
def contacto():
    return render_template('contact.html')

@app.route('/proyectos')
def proyectos():
    lista_proyectos = fb.get_collection('proyectos')
    context = {
        'proyectos':lista_proyectos
    }
    return render_template('projects.html')

@app.route('/resumen')
def resumen():
    perfil_fb = fb.get_collection('perfil')
    perfil_det = perfil_fb[0]
    experiencia_fb = fb.get_collection('experiencias')
    perfil_exp = experiencia_fb[0]
    formacion_fb = fb.get_collection('formacion')
    perfil_formacion = formacion_fb[0]
    habilidades_fb = fb.get_collection('habilidades')
    perfil_skills = habilidades_fb[0]
    tecnologias_fb = fb.get_collection('tecnologias')
    perfil_tec = tecnologias_fb[0]
    context = {
        'cv':perfil_det['cv']
    }
    context2 = {
        'duracion':perfil_exp['duracion'],
        'funcion':perfil_exp['funcion'],
        'empresa':perfil_exp['empresa'],
        'ubicacion':perfil_exp['ubicacion'],
        'detalle':perfil_exp['detalle']
    }
    context3 = {
        'anio':perfil_formacion['anio'],
        'institucion':perfil_formacion['institucion'],
        'location':perfil_formacion['location'],
        'titulo':perfil_formacion['titulo'],
        'grado':perfil_formacion['grado'],
        'detail':perfil_formacion['detail']
    }
    context4 = {
        'skill':perfil_skills['skill']
    }
    context5 = {
        'tecnologia':perfil_tec['tecnologia']
    }
    return render_template('resume.html',**context,**context2,**context3,**context4,**context5)

app.run(debug=True)