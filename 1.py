from lxml import etree

text = '''
<div>
    <ul>
        <li class='n1'><a href="link1.html">1</a></li>
        <li class='n2'><a href='link2.html'>2</a></li>
        <li class='n3'><a href='link3.html'>3</a></li>
        <li class='n4'><a href='link4.html'>4</a>
        <li class='n5'><a href='link5.html'>5</a>
    </ul>
</div>

'''

# 利用etree.HTML将字符串解析为HTML文档
html = etree.HTML(text)
print(html)

# 按字符串序列化HTML文档
result = etree.tostring(html)
print(result.decode())