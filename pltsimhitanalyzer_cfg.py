from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "simhitplots.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Name of output file"
                 )
## 'maxEvents' and 'outputFile' are already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)
options.parseArguments()



import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

#source files
process.load("Analyzers.PLTSimHitAnalyzer.minbiaspileup_cfi")
# process.load("Analyzers.PLTSimHitAnalyzer.muongun_cfi")


process.TFileService = cms.Service("TFileService",
fileName = cms.string(options.outfilename)
)

digifilename = options.outfilename[:-5]+"_digioutput.txt"
process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
#feed this into .cc file
PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM"),
digiFileName = cms.string(digifilename)
)


process.p = cms.Path(process.demo)
