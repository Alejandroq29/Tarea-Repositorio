from PIL import Image, ImageDraw, ImageFont

# Crear una imagen en blanco
width, height = 800, 400
image = Image.new('RGB', (width, height), 'lightblue')

# Crear un objeto de dibujo
draw = ImageDraw.Draw(image)

# Cargar una fuente (puedes usar una fuente TTF que tengas)
font = ImageFont.load_default()

# Mensaje de la invitación
message = "Te quiero mucho! 🐻🌸🦋"
text_width, text_height = draw.textsize(message, font=font)

# Calcular la posición del texto
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

# Dibujar el texto en la imagen
draw.text((text_x, text_y), message, fill='black', font=font)

# Guardar la imagen
image.save('invitacion.png')