#!/bin/sh

ueID=${config["ueID"]}
ueIMSI=${config["ueIMSI"]}

# TODO: Don't hardcode path to OAI directory + softmodem exectuables
pushd /home/jrmurphy/dev/openairinterface5g
source oaienv
popd

/home/jrmurphy/dev/openairinterface5g/cmake_targets/ran_build/build/nr-uesoftmodem \
    -O nrUE_proxy.conf --nokrnmod 1 --ue-idx-standalone $ueID --node-number $ueID \
    --nfapi STANDALONE_PNF --sa --emulate-l1 --uicc0.imsi $ueIMSI \
    --log_config.global_log_options level,nocolor,time,thread_id | tee nrUE.log 2>&1