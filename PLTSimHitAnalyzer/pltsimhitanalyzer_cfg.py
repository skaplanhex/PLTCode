import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun0.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun1.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun2.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun3.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun4.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun5.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun6.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun7.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun8.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun9.root',
                          #'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun10.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun11.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun12.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun13.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun14.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun15.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun16.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun17.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun18.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun19.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun20.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun21.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun22.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun23.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun24.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun25.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun26.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun27.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun28.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun29.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun30.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun31.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun32.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun33.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun34.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun35.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun36.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun37.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun38.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun39.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun40.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun41.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun42.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun43.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun44.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun45.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun46.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun47.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun48.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBias10KRun49.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun0.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun1.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun2.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun3.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun4.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun5.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun6.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun7.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun8.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun9.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun10.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun11.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun12.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun13.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun14.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun15.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun16.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun17.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun18.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun19.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun20.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun21.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun22.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun23.root',
                          'file:/cms/skaplan/PLT/sim/CMSSW_5_3_9/src/MinBiasRun24.root'
                            ),
                #event and lumiblock structure in each input file is the same, so cmsRun thinks each file is a duplicate (it isn't, different random number for each). Tell cmsRun not to do a duplicate check
                            noEventSort = cms.untracked.bool(True),
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
)

process.TFileService = cms.Service("TFileService",
   fileName = cms.string("testfile.root")
)

process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
                              #feed this into .cc file
                              PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM")
                              )


process.p = cms.Path(process.demo)
