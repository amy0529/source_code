import xml.dom.minidom
# 使用minidom解析器打开 XML 文档
document_tree=xml.dom.minidom.parse("storehouse.xml")
collection=document_tree.documentElement#把所有元素存入集合中
print(collection.toxml())
goods= collection.getElementsByTagName("goods")

goods_record=[]
for good_object in goods:          #获取商品的详细信息
   if good_object.hasAttribute("category"):
      goods_record.append(good_object.getAttribute("category"))
   name= good_object.getElementsByTagName('name')[0]
   goods_record.append(name.childNodes[0].data)
   amount= good_object.getElementsByTagName('amount')[0]
   goods_record.append(amount.childNodes[0].data)
   price = good_object.getElementsByTagName('price')[0]
   goods_record.append(price.childNodes[0].data)
print(goods_record)
   
