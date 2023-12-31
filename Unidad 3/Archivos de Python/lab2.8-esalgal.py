# Nombre: Eder Gael Saldaña Galván
# Fecha: 4/Diciembre/2023
# Laboratorio: 2.8

from ncclient import manager
import xml.dom.minidom

m = manager.connect (
    host = "10.10.20.48",
    port = 830,
    username = "developer",
    password = "C1sco12345",
    hostkey_verify = False
)


netconf_reply = m.get_config(source="running")
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_reply = m.get_config(source="running", filter=netconf_filter)
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
