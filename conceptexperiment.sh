#!/bin/bash
echo 'start running login automation'
python -m pytest testcases\conceptexperiment\conceptexperiment_jane.py --alluredir conceptexperimentreport
echo 'start generating the report'
allure serve conceptexperimentreport