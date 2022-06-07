hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

suma_minutos = mins + dura
mod = suma_minutos//60

print((hour+mod)%24, suma_minutos%60, sep=":")
