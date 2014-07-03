#! /bin/bash

export SCRAM_ARCH=slc5_amd64_gcc462
source /uscmst1/prod/sw/cms/shrc prod

cd /uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/Analyzers/PLTSimHitAnalyzer
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
#echo $PWD
phi=True
radius=$1
telmask=False
#special case
if [ $radius -eq 31 ]
then
	phi=True
	radius=0
	telmask=True
elif [ $radius -gt 20 ]
then
	phi=False
	radius=$(($radius-20))
	telmask=True
# if radius >10 but not >20, radius-=10, phi = False
elif [ $radius -gt 10 ]
then
	phi=False
	radius=$(($radius-10))
else
	echo "shouldn't be seeing this"
fi

cmsRun pltsimhitanalyzer_cfg.py doBeamspotStudy=True phiAtZero=$phi r=$radius runFourTelescopes=$telmask maxEvents=-1
