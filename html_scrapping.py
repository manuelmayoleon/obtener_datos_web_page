import re
from requests_html import HTMLSession
from sympy import appellf1

# import requests
# from bs4 import BeautifulSoup


# url_primary = 'https://www.us.es/centros/departamentos/'
# reqs = requests.get(url_primary)
# soup = BeautifulSoup(reqs.text, 'html.parser')

# urls = []
# for link in soup.find_all('a'):
# 	print(link.get('href'))



url =["https://www.us.es/centros/departamentos/administracion-de-empresas-y-marketing",
"https://www.us.es/centros/departamentos/agronomia",
"https://www.us.es/centros/departamentos/algebra",
"https://www.us.es/centros/departamentos/analisis-economico-y-economia-politica",
"https://www.us.es/centros/departamentos/analisis-matematico",
"https://www.us.es/centros/departamentos/anatomia-y-embriologia-humana",
"https://www.us.es/centros/departamentos/antropologia-social",
"https://www.us.es/centros/departamentos/arquitectura-y-tecnologia-de-computadores",
"https://www.us.es/centros/departamentos/biologia-celular",
"https://www.us.es/centros/departamentos/biologia-vegetal-y-ecologia",
"https://www.us.es/centros/departamentos/bioquimica-medica-y-biologia-molecular-e-inmunologia",
"https://www.us.es/centros/departamentos/bioquimica-vegetal-y-biologia-molecular",
"https://www.us.es/centros/departamentos/bioquimica-y-biologia-molecular",
"https://www.us.es/centros/departamentos/ciencias-de-la-computacion-e-inteligencia-artificial",
"https://www.us.es/centros/departamentos/ciencias-juridicas-basicas-derecho-romano-historia-del-derecho-y-derecho",
"https://www.us.es/centros/departamentos/cirugia",
"https://www.us.es/centros/departamentos/citologia-e-histologia-normal-y-patologica",
"https://www.us.es/centros/departamentos/comunicacion-audiovisual-y-publicidad",
"https://www.us.es/centros/departamentos/construcciones-arquitectonicas-i",
"https://www.us.es/centros/departamentos/construcciones-arquitectonicas-ii",
"https://www.us.es/centros/departamentos/contabilidad-y-economia-financiera",
"https://www.us.es/centros/departamentos/cristalografia-mineralogia-y-quimica-agricola",
"https://www.us.es/centros/departamentos/derecho-administrativo",
"https://www.us.es/centros/departamentos/derecho-civil-y-derecho-internacional-privado",
"https://www.us.es/centros/departamentos/derecho-constitucional",
"https://www.us.es/centros/departamentos/derecho-del-trabajo-y-de-la-seguridad-social",
"https://www.us.es/centros/departamentos/derecho-financiero-y-tributario",
"https://www.us.es/centros/departamentos/derecho-internacional-publico-y-relaciones-internacionales",
"https://www.us.es/centros/departamentos/derecho-mercantil",
"https://www.us.es/centros/departamentos/derecho-penal-y-ciencias-criminales",
"https://www.us.es/centros/departamentos/derecho-procesal",
"https://www.us.es/centros/departamentos/dibujo",
"https://www.us.es/centros/departamentos/didactica-de-la-lengua-y-la-literatura-y-filologias-integradas",
"https://www.us.es/centros/departamentos/didactica-de-las-ciencias-experimentales-y-sociales",
"https://www.us.es/centros/departamentos/didactica-de-las-matematicas",
"https://www.us.es/centros/departamentos/didactica-y-organizacion-educativa",
"https://www.us.es/centros/departamentos/economia-aplicada-i",
"https://www.us.es/centros/departamentos/economia-aplicada-ii",
"https://www.us.es/centros/departamentos/economia-aplicada-iii",
"https://www.us.es/centros/departamentos/economia-e-historia-economica",
"https://www.us.es/centros/departamentos/economia-financiera-y-direccion-de-operaciones",
"https://www.us.es/centros/departamentos/ecuaciones-diferenciales-y-analisis-numerico",
"https://www.us.es/centros/departamentos/educacion-artistica",
"https://www.us.es/centros/departamentos/educacion-fisica-y-deporte",
"https://www.us.es/centros/departamentos/electronica-y-electromagnetismo",
"https://www.us.es/centros/departamentos/enfermeria",
"https://www.us.es/centros/departamentos/escultura-e-historia-de-las-artes-plasticas",
"https://www.us.es/centros/departamentos/estadistica-e-investigacion-operativa",
"https://www.us.es/centros/departamentos/estetica-e-historia-de-la-filosofia",
"https://www.us.es/centros/departamentos/estomatologia",
"https://www.us.es/centros/departamentos/estructuras-de-edificacion-e-ingenieria-del-terreno",
"https://www.us.es/centros/departamentos/expresion-grafica-e-ingenieria-en-la-edificacion",
"https://www.us.es/centros/departamentos/expresion-grafica-y-arquitectonica",
"https://www.us.es/centros/departamentos/farmacia-y-tecnologia-farmaceutica",
"https://www.us.es/centros/departamentos/farmacologia",
"https://www.us.es/centros/departamentos/farmacologia-pediatria-y-radiologia",
"https://www.us.es/centros/departamentos/filologia-alemana",
"https://www.us.es/centros/departamentos/filologia-francesa",
"https://www.us.es/centros/departamentos/filologia-griega-y-latina",
"https://www.us.es/centros/departamentos/filologia-inglesa-lengua-inglesa",
"https://www.us.es/centros/departamentos/filologia-inglesa-literatura-inglesa-y-norteamericana",
"https://www.us.es/centros/departamentos/filologias-integradas",
"https://www.us.es/centros/departamentos/filosofia-del-derecho",
"https://www.us.es/centros/departamentos/filosofia-y-logica-y-filosofia-de-la-ciencia",
"https://www.us.es/centros/departamentos/fisica-aplicada-i",
"https://www.us.es/centros/departamentos/fisica-aplicada-ii",
"https://www.us.es/centros/departamentos/fisica-aplicada-iii",
"https://www.us.es/centros/departamentos/fisica-atomica-molecular-y-nuclear"
,"https://www.us.es/centros/departamentos/fisica-de-la-materia-condensada"
,"https://www.us.es/centros/departamentos/fisiologia"
,"https://www.us.es/centros/departamentos/fisiologia-medica-y-biofisica"
,"https://www.us.es/centros/departamentos/fisioterapia"
,"https://www.us.es/centros/departamentos/genetica"
,"https://www.us.es/centros/departamentos/geografia-fisica-y-analisis-geografico-regional"
,"https://www.us.es/centros/departamentos/geografia-humana"
,"https://www.us.es/centros/departamentos/geometria-y-topologia"
,"https://www.us.es/centros/departamentos/historia-antigua"
,"https://www.us.es/centros/departamentos/historia-contemporanea"
,"https://www.us.es/centros/departamentos/historia-de-america"
,"https://www.us.es/centros/departamentos/historia-del-arte"
,"https://www.us.es/centros/departamentos/historia-medieval-y-ciencias-y-tecnicas-historiograficas"
,"https://www.us.es/centros/departamentos/historia-moderna"
,"https://www.us.es/centros/departamentos/historia-teoria-y-composicion-arquitectonicas"
,"https://www.us.es/centros/departamentos/ingenieria-aeroespacial-y-mecanica-de-fluidos"
,"https://www.us.es/centros/departamentos/ingenieria-de-la-construccion-y-proyectos-de-ingenieria"
,"https://www.us.es/centros/departamentos/ingenieria-de-sistemas-y-automatica"
,"https://www.us.es/centros/departamentos/ingenieria-del-diseno"
,"https://www.us.es/centros/departamentos/ingenieria-electrica"
,"https://www.us.es/centros/departamentos/ingenieria-electronica"
,"https://www.us.es/centros/departamentos/ingenieria-energetica"
,"https://www.us.es/centros/departamentos/ingenieria-grafica"
,"https://www.us.es/centros/departamentos/ingenieria-mecanica-y-fabricacion"
,"https://www.us.es/centros/departamentos/ingenieria-quimica"
,"https://www.us.es/centros/departamentos/ingenieria-quimica-y-ambiental"
,"https://www.us.es/centros/departamentos/ingenieria-telematica"
,"https://www.us.es/centros/departamentos/ingenieria-y-ciencia-de-los-materiales-y-del-transporte"
,"https://www.us.es/centros/departamentos/lengua-espanola-linguistica-y-teoria-de-la-literatura"
,"https://www.us.es/centros/departamentos/lenguajes-y-sistemas-informaticos"
,"https://www.us.es/centros/departamentos/literatura-espanola-e-hispanoamericana"
,"https://www.us.es/centros/departamentos/matematica-aplicada-i"
,"https://www.us.es/centros/departamentos/matematica-aplicada-ii"
,"https://www.us.es/centros/departamentos/mecanica-de-medios-continuos-y-teoria-de-estructuras"
,"https://www.us.es/centros/departamentos/medicina"
,"https://www.us.es/centros/departamentos/medicina-preventiva-y-salud-publica"
,"https://www.us.es/centros/departamentos/metafisica-y-corrientes-actuales-de-la-filosofia-etica-y-filosofia-politica"
,"https://www.us.es/centros/departamentos/metodos-de-investigacion-y-diagnostico-en-educacion"
,"https://www.us.es/centros/departamentos/microbiologia"
,"https://www.us.es/centros/departamentos/microbiologia-y-parasitologia"
,"https://www.us.es/centros/departamentos/motricidad-humana-y-rendimiento-deportivo"
,"https://www.us.es/centros/departamentos/nutricion-y-bromatologia-toxicologia-y-medicina-legal"
,"https://www.us.es/centros/departamentos/organizacion-industrial-y-gestion-de-empresas-i"
,"https://www.us.es/centros/departamentos/organizacion-industrial-y-gestion-de-empresas-ii"
,"https://www.us.es/centros/departamentos/periodismo-i"
,"https://www.us.es/centros/departamentos/periodismo-ii"
,"https://www.us.es/centros/departamentos/personalidad-evaluacion-y-tratamiento-psicologicos"
,"https://www.us.es/centros/departamentos/pintura"
,"https://www.us.es/centros/departamentos/podologia"
,"https://www.us.es/centros/departamentos/prehistoria-y-arqueologia"
,"https://www.us.es/centros/departamentos/proyectos-arquitectonicos"
,"https://www.us.es/centros/departamentos/psicologia-evolutiva-y-de-la-educacion"
,"https://www.us.es/centros/departamentos/psicologia-experimental"
,"https://www.us.es/centros/departamentos/psicologia-social"
,"https://www.us.es/centros/departamentos/psiquiatria"
,"https://www.us.es/centros/departamentos/quimica-analitica"
,"https://www.us.es/centros/departamentos/quimica-fisica"
,"https://www.us.es/centros/departamentos/quimica-inorganica"
,"https://www.us.es/centros/departamentos/quimica-organica"
,"https://www.us.es/centros/departamentos/quimica-organica-y-farmaceutica"
,"https://www.us.es/centros/departamentos/sociologia"
,"https://www.us.es/centros/departamentos/tecnologia-electronica"
,"https://www.us.es/centros/departamentos/teoria-de-la-senal-y-comunicaciones"
,"https://www.us.es/centros/departamentos/teoria-e-historia-de-la-educacion-y-pedagogia-social"
,"https://www.us.es/centros/departamentos/urbanistica-y-ordenacion-del-territorio"
,"https://www.us.es/centros/departamentos/zoologia"]


EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


# PHONE_REGEX  = r"""(
#      (\d{3}|\(\d{3}\))? # area code
#      (\s|-|\.)? # separator
#      (\d{2}) # first 3 digits
#      (\s|-|\.) # separator
#      (\d{3}) # last 4 digits
#      (\s|-|\.) # separator
#       (\d{2}) # first 3 digits
#      (\s|-|\.) # separator
#      (\d{2}) # last 4 digits
#      (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
#      ) """
# PHONE_REGEX = re.compile(r'''(
#      (\d{3}|\(\d{3}\))? # area code
#      (\s|-|\.)? # separator
#      (\d{2}) # first 3 digits
#      (\s|-|\.) # separator
#      (\d{3}) # last 4 digits
#      (\s|-|\.) # separator
#       (\d{2}) # first 3 digits
#      (\s|-|\.) # separator
#      (\d{2}) # last 4 digits
#      (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
#      )''', re.VERBOSE)
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)
# initiate an HTTP session
session = HTMLSession()
# create email list
email = []
phones = []
for x in url:
# get the HTTP Response
    r = session.get(x)
    phones = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',r.html.raw_html.decode())
    phones  =  list(dict.fromkeys(phones))
#     print(phones)
    for number in phones:
            if '95.' in number :
                number= number.replace('.','')
                print(number)
#     print(re.findall(PHONE_REGEX, r.html.raw_html.decode())) 
#     for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
#         match=re_match.group()
#         email.append(match)
#         print(match)
        

# print(email)