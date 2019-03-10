import random
from datetime import datetime as dt

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

def generate_page(head, body):
    page = f"""<!DOCTYPE html>
    <html>
    {head}
    {body}
    </html>"""
    return page

def generate_head(title):
    head = f"""<head>
    <meta charset='utf-8'>
    <title>{title}</title>
    <link rel="stylesheet" href="./css/goroscop.css">
    </head>
    """
    return head

def generate_body(header, content):
    body = f"""<h1 class="headline">{header}</h1>"""
    body = body + content
    return f"""<body>
            {body}
            </body>"""

def gen_index_content():
    content_text = """<ul> """
    for i in range(0,3):
        one_prophecie = ""
        for j in range(0,4):
            one_prophecie = one_prophecie + "<p>"+random.choice(times).capitalize()+" "+random.choice(advices).lower()+" "+random.choice(promises).lower()+".</p>"
            # print('<div class="gor"><li>'+one_prophecie.rstrip(' ')+'</li></div>')
        content_text = content_text + '<div class="gor"><li>' + one_prophecie.rstrip(' ') + '</li></div>'
    content_text += """</ul> 
    </hr>
    <a href="about.html">О чем все это</a>"""
    return content_text

def gen_about_content():
    content_text = """<table style="width:100%">
                    <tr>
                      <th>Времена дня:</th>
                      <th>Глаголы:</th> 
                      <th>Предсказания:</th>
                    </tr>"""
    i = 0
    stop = True
    while stop:
        one_row = ""
        one_row = one_row + "<td>" + (times[i] if i < len(times) else "") + "</td>" + "<td>" + (advices[i] if i < len(advices) else "") + "</td>" + "<td>" + (promises[i] if i < len(promises) else "") + "</td>"
        print("<tr>" + one_row + "</tr>")
        content_text = content_text + "<tr>" + one_row + "</tr>"
        i += 1
        stop = not ((i >= len(times)) and (i >= len(advices)) and (i >= len(promises)))
    content_text = content_text + """</table>
       <a href="index.html">Предсказания</a>"""
    return content_text

def save_page(title, header, content, output="index.html"):
    fp = open(output, "w")
    # today = dt.now().date()
    page = generate_page(
        head = generate_head(title ), 
        body = generate_body(header , 
                             content )
        )
    print(page)
    print(page, file=fp)
    fp.close()


#####################

today = dt.now().date()

save_page(title = "Ваши предсказания на " + str(today), 
          header = "Что день " + str(today) + " готовит", 
          content = gen_index_content(), 
          output="index1.html")
save_page(title = "О чем все это", 
          header = "Идеи для предсказаний", 
          content = gen_about_content(), 
          output="about1.html")