#!/bin/sh

numUEs="${config["numue"]}"
gnb_ipaddr="${config["gnb_ipaddr"]}"
proxy_ipaddr="${config["proxy_ipaddr"]}"
ue_ipaddr="${config["ue_ipaddr"]}"

/home/oai-lte-5g-multi-ue-proxy/build/proxy $numUEs --nr $gnb_ipaddr $proxy_ipaddr $ue_ipaddr
