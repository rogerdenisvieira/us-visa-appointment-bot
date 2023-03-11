from pathlib import Path
from scrapy.http import FormRequest
from scrapy import Request

import os
import scrapy


class AppointmentSpider(scrapy.Spider):
    name = "appointment_spider"

    def start_requests(self):
        URL = 'https://ais.usvisa-info.com/pt-br/niv/users/sign_in'
        return [
            Request(URL, callback=self.login)
        ]


    def login(self, response):
        print(response)
        URL = 'https://ais.usvisa-info.com/pt-br/niv/users/sign_in'
        USER = os.environ.get("SCRAPY_USER")
        PWD = os.environ.get("SCRAPY_PWD")

        return FormRequest.from_response(response, formdata={"user[email]":USER,"user[password]":PWD, 
        "policy_confirmed":"1", "commit": "Acessar"}, callback=self.parse)
        


    def parse(self, response):
        print(response)
        pass

    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     Path(filename).write_bytes(response.body)
    #     self.log(f'Saved file {filename}')