import xml.dom.minidom 
# 使用minidom解析器打开 XML 文档
document_tree=xml.dom.minidom.parse("storehouse.xml")
collection=document_tree.documentElement#把所有元素存入集合中
price= collection.getElementsByTagName("price")
price_object=price[0]
price_object.firstChild.data=8.2
print('修改商品价格成功!')

goods=collection.getElementsByTagName("goods")
collection.removeChild(goods[1])
#collection.removeChild(collection.childNodes[1])
print('节点删除成功!')
f=open("storehouse.xml","w",encoding="utf-8")
f.write(document_tree.toxml())
f.close()    
