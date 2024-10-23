import requests

def obtener_clima():
    ciudad = "General Levalle" #entrada.get()
    api_key = "bc899cb7e122434a9910705240210"
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es"
        respuesta = requests.get(url)
        clima = respuesta.json()
        #print(clima)
        if "errror" in clima:
          label_clima["text"] = f"error: {clima['error']["message"]}"
        else:
          label_clima["text"] = f" El clima es {clima['current']['condition']['text']} y la temperatura es {clima['current']['temp_c']}°C"
    except:
        label_clima["text"] = "error: no se pudo obtener la información"

obtener_clima()