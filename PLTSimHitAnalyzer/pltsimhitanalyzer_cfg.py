import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                            'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/SingleElectronPt100_PLTEta_cfi_py_GEN_SIM.root'
                            )
)

process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
                              PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM")
                              )


process.p = cms.Path(process.demo)
