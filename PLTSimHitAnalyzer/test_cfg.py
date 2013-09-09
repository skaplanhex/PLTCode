import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                              'file:/YOURWORKINGAREA/CMSSW_5_3_9/src/MinBias_TuneZ2star_8TeV_pythia6_cff_GEN_SIM.root',
                              ),
                            )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("testfile.root")
                                   )

process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
                              #feed this into .cc file
                              PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM")
                              )


process.p = cms.Path(process.demo)
