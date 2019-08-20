from lxml import etree

str = """
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html" class="cls1">fourth item<span>abc</span></a></li>
             <li class="item-0"><a href="link5.html" class="cls">fifth item</a>
         </ul>
     </div>
 """

html = etree.HTML(str)
# ret = html.xpath('//li')
# ret = html.xpath('//a/text()')
ret = html.xpath('//li/a[@href="link1.html"]')
# ret = html.xpath('//li//span')
# ret = html.xpath('//li/a/@class')
# ret = html.xpath('//li[last()]/a/@href')
# ret = html.xpath('//li[last()-1]//text()')
print(ret)
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
print(set(a)&set(b))
print(set(a)|set(b))
print(set(a)^set(b))
import random

x = [i for i in range(10)]

print(x)

random.shuffle(x)

print(x)
