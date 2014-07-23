#! /bin/bash

export SCRAM_ARCH=slc5_amd64_gcc462
source /uscmst1/prod/sw/cms/shrc prod

cd /uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/Analyzers/PLTSimHitAnalyzer
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}

cmsRun pltsimhitanalyzer_cfg.py outfilename=muonplots.root maxEvents=100
