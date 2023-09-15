



def add_time(start, duration, day=''):
    #print('---------------')
    new_time=''
    horaInicial=int((start.split(" ")[0]).split(":")[0])
    minutoInicial=int((start.split(" ")[0]).split(":")[1])
    momentoInicial=(start.split(" ")[1])
    horasExtra=int(duration.split(":")[0])
    minutosExtra=int(duration.split(":")[1])

    #if day != None:
    #  print('Start: ' + start + ', duration: ' + duration +', ' + 'day: ' + day)
    #else:
    #  print('Start: ' + start + ', duration: ' + duration)
      
    datos = addHoras(horaInicial, minutoInicial, horasExtra, minutosExtra, momentoInicial)
    #print(datos)

    new_time = datos[0] + ':' + datos[1] + ' ' + datos[2] + diaSemana(day,datos) + datosExtra(datos)

    #print(new_time)
    return new_time

def diaSemana(day,datos):
  diaFinal=''
  if day != '':
    diaFinal = day.lower()
    dias = datos[3] % 7

    for d in range(dias):
      if diaFinal == "monday":
        diaFinal = "tuesday"
        continue
      if diaFinal == "tuesday":        
        diaFinal = "wednesday"
        continue
      if diaFinal == "wednesday":        
        diaFinal = "thursday"
        continue
      if diaFinal == "thursday":
        diaFinal = "friday"
        continue
      if diaFinal == "friday":
        diaFinal = "saturday"
        continue
      if diaFinal == "saturday":
        diaFinal = "sunday"
        continue
      if diaFinal == "sunday":
        diaFinal = "monday"
        continue      

    return ', ' + diaFinal.capitalize()
  else:
   return ''


def datosExtra(datos):
  if datos[3] > 1:
    return ' (' + str(datos[3]) + ' days later)'
  if datos[3] == 1:
    return ' (next day)'
  if datos[3] == 0:
    return ''

def addHoras(horaInicial, minutoInicial, horasExtra, minutosExtra, momentoInicial):
    momento = momentoInicial
    horaFinal = horaInicial
    minutoFinal = minutoInicial
    numeroDias = 0
    datos = []

    #Horas
    for i in range(horasExtra):
      if (horaFinal == 11 and momento=='PM'):
        horaFinal = 12
        momento = 'AM'
        numeroDias = numeroDias + 1
        continue
      if (horaFinal == 11 and momento=='AM'):
        horaFinal = horaFinal + 1
        momento='PM'
        continue
      if (horaFinal == 12):
        horaFinal=1
        continue
      if (horaFinal!=11):
        horaFinal = horaFinal + 1
        continue

    #Minutos
    for i in range(minutosExtra):
      if minutoFinal == 59:
          if horaFinal == 11 and momento =='AM':
            momento='PM'
            minutoFinal = 0
            horaFinal = horaFinal + 1
            continue
          if horaFinal == 11 and momento =='PM':
            momento='AM'
            minutoFinal = 0
            horaFinal = 12
            numeroDias = numeroDias + 1
            continue
          else:
            minutoFinal = 0
            horaFinal = horaFinal + 1
            continue
      else:
        minutoFinal = minutoFinal + 1
        continue

    datos.append(str(horaFinal))
    if len(str(minutoFinal)) == 1:
      datos.append('0' + str(minutoFinal))
    else:
      datos.append(str(minutoFinal))
    datos.append(str(momento))
    datos.append(numeroDias)
    return datos

