
import json
import xmltodict


class XmlToJsonConverter:

    def convert_from_xxml_to_json(self, xml_file: str) -> bool:

        try:
             with open(xml_file, 'r') as xml_file_e:
                xml_output = xml_file_e.read()
                xml_dict = xmltodict.parse(xml_output)
                with open('convert.json', 'w') as json_file:
                    json.dump(xml_dict, json_file)
                    return True

        except Exception as e:
            print("Error {e}")
            return False


converter = XmlToJsonConverter()
converter.convert_from_xxml_to_json('products.xml')
