import xml.etree.ElementTree as ET
from StringIO import StringIO
from xml.dom import minidom
import random

str1 = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">

 <key attr.name="De" attr.type="string" for="node" id="d0"/>


  <graph edgedefault="directed" id="G">
  	 <node id="n0">
  	 	 <data key="d0"><![CDATA[Test1]]></data>
  	 	 <label> Event1 </label>
  	 </node>
  	 <node id="n1">
  	 	 <data key="d0"><![CDATA[Test2]]></data>
  	 	 <label> Event2 </label>
  	 </node>
  	 <node id="n2">
  	 	 <data key="d0"><![CDATA[Test2]]></data>
  	 	 <label> Event3 </label>
  	 </node>
  	 <node id="n3">
  	 	 <data key="d0"><![CDATA[Test2]]></data>
  	 </node>
  	 <edge id="e6" source="n0" target="n1"></edge>
  	 <edge id="e7" source="n1" target="n3"></edge>
  	 <edge id="e8" source="n2" target="n3"></edge>
  	 	
  	 
  </graph>
 </graphml>

"""
ks2  = "<key "
ks3 = "</graphml>"
broiler_plate = "<?xml version='1.0' encoding='UTF-8' standalone='no'?><graphml xmlns='http://graphml.graphdrawing.org/xmlns' xmlns:java='http://www.yworks.com/xml/yfiles-common/1.0/java' xmlns:sys='http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0' xmlns:x='http://www.yworks.com/xml/yfiles-common/markup/2.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:y='http://www.yworks.com/xml/graphml' xmlns:yed='http://www.yworks.com/xml/yed/3' xsi:schemaLocation='http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd'>"
broiler_plate2 = '<key for="node" id="d8" yfiles.type="nodegraphics"/>' #d8 reserved for graphics
end = '</graphml>'
#print str1.find(s3)
#print str1[:862]
#print str1.find(s2)
#print str1[565:]
#root = ET.fromstring(str1)
#instead use the following to parse and remove extraneous
it = ET.iterparse(StringIO(str1))
for _, el in it:
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
root = it.root


#print root.tag
#for child in root:
#	print child.tag, child.attrib
	
#for child in root[1][0]:
#	print child.tag, child.attrib


x = 336
y = 213
i = 11
for neighbor in root[1].iter('node'):
	val = i
	try:
		val = neighbor[1].text
	except:
		pass
	child = ET.SubElement(neighbor, 'data', attrib = {'key' : 'd8'})
	sub = ET.SubElement(child, 'y:ShapeNode')
	s1 = ET.SubElement(sub, 'y:Geometry', attrib = {'height':'30.0', 'width':'30.0', 'x':str(x), 'y':str(y)})
	s2 = ET.SubElement(sub, 'y:BorderStyle', attrib = {'color' : "#000000", 'type' :"line", 'width':"1.0"})
	s3 = ET.SubElement(sub, 'y:NodeLabel', attrib = {'alignment':"center",'autoSizePolicy':"content", 'fontFamily':"Dialog", 'fontSize':"12", 'fontStyle':"plain", 'hasBackgroundColor':"false", 'hasLineColor':"false" ,'height':"18.701171875" ,'modelName':"custom" ,'textColor':"#000000" ,'visible':"true" ,'width':"10.673828125" ,'x':"9.6630859375" , 'y':"5.6494140625"})
	s3.text = str(val)
	s4 = ET.SubElement(s3, 'y:LabelModel')
	s5 = ET.SubElement(s4, 'y:SmartNodeLabelModel', attrib = {'distance': '4.0'})
	s7 = ET.SubElement(s3, 'y:ModelParameter')
	s8 = ET.SubElement(s7, 'y:SmartNodeLabelModelParameter', attrib = {'labelRatioX':"0.0" ,'labelRatioY':"0.0",'nodeRatioX':"0.0" ,'nodeRatioY':"0.0" ,'offsetX':"0.0", 'offsetY':"0.0" ,'upX':"0.0" ,'upY':"-1.0"})
	s9 = ET.SubElement(sub, 'y:Shape', attrib = {'type':'rectangle'})
	#print ET.tostring(neighbor)
	#print '##########'
	x += 80
	y += random.randint(-160, 160)
	if y <= 20:
		y = 213
	i += 1
	
top = ET.Element('top')
child = ET.SubElement(top, 'y:child', attrib = {'key' : 'd8'})
child.text = 'This child contains text.'

raw = ET.tostring(root)
sid =  raw.find(ks2)
temp = raw[sid:]
man =  temp.find(ks3)
temp2 = temp[:man]

print broiler_plate + '\n' + broiler_plate2 + '\n' + temp2 + '\n' + end
