import scrapy


class Robot(scrapy.Spider):

    name = "salary"
    start_urls = [
        "https://transparencia.setorpessoal.com/funcionarios.php?CODCLIENTE=685101&TIPO=1&ANO=2018&MES=05N&",
    ]

    def parse(self, response):
        for line in response.css('.linha'):
            yield {
                "name": line.css("td:nth-child(1)").extract_first().replace("<td>", "").replace("</td>", ""),
                "job": line.css("td:nth-child(4)").extract_first().replace("<td>", "").replace("</td>", ""),
                "relation": line.css("td:nth-child(3)").extract_first().replace("<td>", "").replace("</td>", ""),
                "place": line.css("td:nth-child(5)").extract_first().replace("<td>", "").replace("</td>", ""),
                "working_hours": line.css("td:nth-child(6)").extract_first().replace("<td>", "").replace("</td>", ""),
                "salary": line.css(".linha td:nth-child(7)").extract_first().replace("</td>", "").replace("\"", "").replace("<td style=text-align:right;>", "").replace(",", "").replace(".", "")
            }

