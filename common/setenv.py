# Criar variáveis que serão utilizadas durante os execícios

import re

def __generate_settings(): 
    # Obter e-mail do usuário logado
    # A partir do e-mail gerar nome do schema que será usado nos laboratórios

    settings['lab.user.email'] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
    settings['lab.user.name'] = re.sub(r'\W', '_', settings["lab.user.email"].split('@')[0])

    settings['lab.catalog'] = spark.catalog.currentCatalog()
    settings['lab.schema'] = f"lab_{settings['lab.user.name']}"

    settings['lab.path.files'] = f"/Volumes/{settings['lab.catalog']}/{settings['lab.schema']}/files"

    # Listar e incluir variáveis no spark.conf

    print ("""Variáveis ambiente, podem ser utilizadas no código com as seguintes formas : 
    Via settings['<key>']           ex: var = settings['lab.catalog']
    Via spark.conf.get('<key>')     ex: var = spark.conf.get('lab.catalog')
    Via SQL ${<key>}                ex: SELECT * FROM ${lab.catalog}.${lab.schema}.mytable
    """)
    print (80*'=')

    for key, value in settings.items():
        spark.conf.set(key, value)
        print(f"{key.ljust(20)} : {value}")

def get_settings(key): 
    return spark.conf.get(key,None)

# main
# dicionário de variáveis
# if settings is None:
settings = {}
__generate_settings()
