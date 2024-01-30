#!/bin/sh

pushd /home/openairinterface5g
source oaienv
popd

/home/openairinterface5g/cmake_targets/ran_build/build/nr-softmodem \
    -O gNB_proxy.conf --nfapi VNF --sa --emulate-l1 \
    --log_config.global_log_options level,nocolor,time,thread_id | tee gNB.log 2>&1
