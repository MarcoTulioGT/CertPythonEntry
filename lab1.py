hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

suma_minutos = mins + dura

div = suma_minutos%60
mod = suma_minutos//60

hora = (hour+mod)%24
minutos = div


print(hora, minutos, sep=":")
