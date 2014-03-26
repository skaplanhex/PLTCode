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

#files located at FNAL
process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(
                    	'/store/user/skaplan/MinBiasTestEvents/PLTMinBiasEvents_NoPileUp_1.root',
                    	'/store/user/skaplan/MinBiasTestEvents/PLTMinBiasEvents_NoPileUp_2.root',

					),
					#duplicate event/lumisection numbers are ok (different random seeds)
					duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

)


process.TFileService = cms.Service("TFileService",
fileName = cms.string(options.outfilename)
)

process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
#feed this into .cc file
PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM")
)


process.p = cms.Path(process.demo)
