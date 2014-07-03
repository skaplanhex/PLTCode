#makes input cfi files for all beamspot scenarios!

import os, sys

eospath = "/eos/uscms/store/user/skaplan/noreplica/"
shortpath = "/store/user/skaplan/noreplica/"

for phi in (0,225):
	for r in range(11):
		if (phi == 225 and r == 0):
			continue
		folder="MinBiasBeamSpotPhi%iR%i_HISTATS/"%(phi,r)
		fullpath = eospath+folder
		outfiles = os.listdir(fullpath)
		outfilesnew=[]
		for f in outfiles:
			outfilesnew.append("		'"+shortpath + folder + f + "',")
		out = open("MinBiasBeamSpotPhi%iR%i"%(phi,r)+"_cfi.py",'w')
		out.write("import FWCore.ParameterSet.Config as cms\n")
		out.write("\n")
		out.write('source = cms.Source("PoolSource",\n')
		out.write("	fileNames = cms.untracked.vstring(\n")
		for f in outfilesnew:
			out.write(f+"\n")
		out.write("	)\n")
		out.write("\n")
		out.write(")\n")
		out.close()
