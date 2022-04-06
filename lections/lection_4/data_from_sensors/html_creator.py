
from user_interface import pressure_view, temperature_view, wind_speed_view


def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n<head></head>\n <body>\n'
    html += f'   <p {style}>Temperature: {temperature_view(device)} c</p>\n'
    html += f'   <p {style}>Wind_speed: {wind_speed_view(device)} m/s</p>\n'
    html += f'   <p {style}>Pressure: {pressure_view(device)} mmHg/s</p>\n'
    html += '   <\\body>\\n<\html>'

    with open("C:\\Users\\Zver\\Desktop\\GeekBrains\\python\\lections\\lection_4\\data_from_sensors\\index.html", 'w') as page:
        page.write(html)
    
    return html
