#!/usr/bin/env python3
3
import subprocess
import optparse
import re

def get_current_mac(interface):
    ifconfig_out = subprocess.check_output(["ifconfig", values.interface]).decode("utf-8")
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_out).group(0)
    print("[+] MAC address at " + interface + " is: " + mac)
    return mac

def mac_changer(interface, mac):
    print("[+] Changing MAC address for " + values.interface + " to " + values.mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface whose MAC you want to change; run ifconfig for a list of interfaces")
    parser.add_option("-a", "--mac", dest="mac", help="The new MAC address for the interface")
    (values,_) = parser.parse_args()
    if not values.interface:
        parser.error("[-] PLease specify an interface, flag --help for more information.")
        return
    if not values.mac:
        parser.error("[-] PLease specify a MAC address, flag --help for more information.")
        return
    return values

values = get_args()
get_current_mac(values.interface)
mac_changer(values.interface,values.mac)
get_current_mac(values.interface)

