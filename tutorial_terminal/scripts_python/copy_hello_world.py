from datetime import datetime

fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('/workspaces/notes_github/tutorial_terminal/res/test.txt', 'a') as archivo: archivo.write(f'Tarea finalizada a las {fecha_hora_actual}')
