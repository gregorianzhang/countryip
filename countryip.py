#!/usr/bin/python
#-*- conding:utf-8 -*-

import math
import requests
from optparse import OptionParser

url = "http://ftp.apnic.net/stats/apnic/delegated-apnic-latest"


def main():
    parser = OptionParser()
    parser.add_option("-f","--file",dest="filename",help="write to FILE")
    parser.add_option("-c","--country",dest="country",help="country code")
    (options, args) = parser.parse_args()
    #print options.country
    req = requests.get(url)
    lines =req.content.splitlines()

    cidr=[]
    for line in lines:
        if (('ipv4' in line) & ( options.country in line)):
            s=line.split("|")
            addr="%s/%d" % (s[3],int((32-math.log(float(s[4]),2))))
            #addr="%s/%s" % (s[3],s[4])
#            print options.filename
            if options.filename :
#                with open(options.filename,"a+") as f:
#                    f.write(addr+"\n")
                cidr.append(addr)
            else:
                print addr

    with open(options.filename,"a+") as f:
        for line in cidr:
            f.write(line+"\n")


if __name__ == "__main__":
    main()

