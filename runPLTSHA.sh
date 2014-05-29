#! /bin/tcsh
cd
source ~/cmssw_init
cd /uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/Analyzers/PLTSimHitAnalyzer
scramv1 runtime -sh
#Do whatever you want the script to do!
cmsRun pltsimhitanalyzer_cfg.py maxEvents=1500 outfilename=test.root
