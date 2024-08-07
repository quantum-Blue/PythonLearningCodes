html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Sayfam</title>
</head>
<body>

    <h1 id="header"
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Moduller
        </h2>

        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>
    </div>

    <img src = "hisoka.jpeg" alt"" >

    <a class="sister" href="https://example1.com/elsie" id = "link" >Elsie</a>
    <a class="sister" href="https://example2.com/elsie" id = "link" >Elsie</a>
    <a class="sister" href="https://example3.com/elsie" id = "link" >Elsie</a>

</body>
</html>


"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")
result = soup.prettify() # html dokumanini duzenler (cmd + F gibi)
print(result)
result = soup.title # html nin title kısmını verir
print(result)
result = soup.head # html nin head kısmını verir
print(result)
result = soup.boddy # html nin body kısmını verir
print(result) 
result = soup.title.name 
print(result)
result = soup.title.string
print(result)
result = soup.h1
print(result)
result = soup.h2
print(result)
result = soup.h2.name
print(result)
result = soup.h2.string
print(result)
result = soup.h1.string
print(result)

result =soup.find_all("h2")
print(result)
result =soup.find_all("h2")[0]
print(result)
result =soup.find_all("h2")[1]
print(result)
result =soup.div
print(result)
result =soup.find_all("div")[1]
print(result)
result =soup.find_all("div")[1].ul.find_all("li")
print(result)
result =soup.div.findChildren() # alt elemanlara children denir
print(result) # alt elemanların hepsini yazdırır
result =soup.div.find_next_sibling() # grup 1 den sonraki gruba gecer
print(result)
result =soup.div.find_previous_sibling() # onceki gruba doner
print(result)
result =soup.find_all("a")
print(result)

for link in result:
    print(link)

