from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "simhitplots.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Name of output file"
)
options.register('doBeamspotStudy',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "whether or not to do beamspot study"
)
options.register('phiAtZero',
                 True,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "phi at zero"
)
options.register('r',
                 0,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "value of r_beamspot"
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
# process.load("Analyzers.PLTSimHitAnalyzer.minbiaspileup_cfi")
# process.load("Analyzers.PLTSimHitAnalyzer.muongun_cfi")
phi = 0
if not options.phiAtZero:
	phi = 225
process.load("Analyzers.PLTSimHitAnalyzer.MinBiasBeamSpotPhi%iR%i_cfi"%(phi,options.r))

# process.source = cms.Source("PoolSource",
# 		fileNames = cms.untracked.vstring(
# 			#"file:/uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/outfile14TeV.root"
# 			#'/store/user/skaplan/MinBiasBeamSpotPhi0R0/outfile14TeV_18_1_OfZ.root'
# 			'/store/user/skaplan/MinBiasPileUpOfficial/outfile_169_1_WvX.root'
# 		)
# )

process.TFileService = cms.Service("TFileService",
fileName = cms.string(options.outfilename)
)

#file name of digi output. The file endings will be added in the analyzer (as the base name is used more than once)
digifilename = options.outfilename[:-5]+"_digioutput"

#maybe have these paramateters as ones that can be passed in via VarParsing?
process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
	#feed this into .cc file
	PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM"),
	doBeamspotStudy = cms.bool(options.doBeamspotStudy),
	phiAtZero = cms.bool(options.phiAtZero),
	r = cms.int32(options.r),
	#digiFileName = cms.string(digifilename),
	#doPileup = cms.bool(True),
	#threshold = cms.int32(4000),
)


process.p = cms.Path(process.demo)
