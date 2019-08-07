import requests
import parsel

response = requests.get("http://www.weather.com.cn/weather/101280601.shtml")

response.encoding = response.apparent_encoding

html = response.text

# print(html)
#re, css, xpath
#lxml pyquery bs4 parse1
# make the html a structure that can be chosen
sel = parsel.Selector(response.text)

li = sel.xpath('//ul[@class="clearfix"]/li')

span = li[0].css('span::text').get()
em = li[0].css('em::text').get()
p = li[0].css('p::text').get()

print(span, em, p)




# for i in li:
#     print(i.re('<span>(.*?)</span>'))
#     print(i.re('<em>(.*?)</em>'))
#     print(i.re('<p>(.*?)</p>'))
