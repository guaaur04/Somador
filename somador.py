# a = 10
# b = 20 

# soma = a + b 

# print("A soma dos numeros e soma", soma)

# temperaturaFarenheit = input("Digite uma temperatura em Farenheit: ")

# temp = float(temperaturaFarenheit)

# temperaturaCelsius =(temperaturaFarenheit - 32) * 5 / 9

# print("A temperatura em celsius e", temperaturaCelsius)

# nomeDaMae = input("Qual o nome da sua mae?")
# nomeDoPai = input ("Qual o nome do seu pai?")

# print("Bom dia Sra.", nomeDaMae, "!!! E bom dia Sr.", nomeDoPai)

segundos_str = input ("Por favor, entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas" , minutos, "minutos e", segs_restantes_final, "segundos.")