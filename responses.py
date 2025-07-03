import re

def process_message(message, response_array, response):
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())
    score = sum(1 for word in list_message if word in response_array)
    return [score, response]

def get_response(message):
    response_list = [
        process_message(message, ['hola', 'buenas', 'holis'], '¡Hola! 👋 ¿En qué puedo ayudarte con InventarioApp?'),
        process_message(message, ['stock', 'producto', 'cantidad'], '📦 Podés consultar el stock enviando el nombre o código del producto.'),
        process_message(message, ['error', 'fallo', 'problema'], '🔧 Por favor describí el error. Nuestro equipo lo revisará.'),
        process_message(message, ['usuario', 'acceso', 'contraseña'], '🔐 Si olvidaste tu contraseña, escribinos por WhatsApp.'),
        process_message(message, ['soporte', 'ayuda', 'contacto'], '👩‍💻 Podés contactarnos por WhatsApp al +54 123456789.'),
        process_message(message, ['chau', 'gracias', 'adios'], '¡Gracias por usar InventarioApp! 👋')
    ]
    scores = [r[0] for r in response_list]
    best = max(scores, default=0)
    return response_list[scores.index(best)][1] if best > 0 else 'No entendí tu mensaje. Usá /start para ver opciones.'
