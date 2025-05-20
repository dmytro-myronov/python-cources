
import re
def is_ip(ip):

    if re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip):
        ip_elts = ip.split('.')
        for elt in ip_elts:
            try:
                if 0 < int(elt) > 255:
                    print("no")
                    return False
            except ValueError as e:
                return False


        return True
    return False



is_valid_ip = is_ip('150.168.10.1')
is_valid_ip2 = is_ip('_150.168.10.1')
print(is_valid_ip)
print(is_valid_ip2)