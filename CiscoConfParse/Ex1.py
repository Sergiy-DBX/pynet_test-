#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
import pdb

CONFIG_FILE = '../../pynet-ons-oct17/day3/cisco_ipsec.txt'

def read_conf_file(text_file):
    with open(text_file) as file_in:
        just_text = file_in.read()
        return just_text

def main():
   
    cisco_config_file = read_conf_file(CONFIG_FILE)
    #print(cisco_config_file) 
    cisco_cfg = CiscoConfParse(CONFIG_FILE)
    print(cisco_cfg)
    
    
    pdb.set_trace() 
    
if __name__ == '__main__':
    main()
