#makes input cfi files for all muon gun scenarios!

import os, sys

for pt in ("005",):
    for eta in ("Full","Center"):
        for phi in ("Full","Center"):
            for sigmaZ in ("20","Small"):
                folder = "AntiMuonGunPt%s/%sEta_%sPhi_%sSigmaZ/"%(pt,eta,phi,sigmaZ)
                eospath = "/eos/uscms/store/user/skaplan/noreplica/"
                shortpath = "/store/user/skaplan/noreplica/"
                fullpath = eospath+folder
                outfiles = os.listdir(fullpath)
                outfilesnew=[]
                for f in outfiles:
                    outfilesnew.append("        '"+shortpath + folder + f + "',")
                out = open("AntiMuonGunPt%s_%sEta_%sPhi_%sSigmaZ"%(pt,eta,phi,sigmaZ)+"_cfi.py",'w')
                out.write("import FWCore.ParameterSet.Config as cms\n")
                out.write("\n")
                out.write('source = cms.Source("PoolSource",\n')
                out.write("    fileNames = cms.untracked.vstring(\n")
                for f in outfilesnew:
                    out.write(f+"\n")
                out.write("    )\n")
                out.write("\n")
                out.write(")\n")
                out.close()
