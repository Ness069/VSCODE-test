# SOLICITUDES API
# Json es como las principales apis comparten la informacion 
# y x sus siglas Java Script object Notacion 
#formato de intercambio de datos % sistemas y lengajes de progra
#Apis son (interfas de programacion de aplicaciones)

import requests #importa paquete
#asigna el URL a una variable
url = 'https://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
#empaqueta la solicitud sokicita el requet y cacha la respuesta en variable
r = requests.get(url)
#imprime el texto d ela respuesta
print(r.text)
