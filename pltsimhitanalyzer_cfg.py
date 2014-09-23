from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "simhitplots.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Name of output file"
)
options.register('threshold',
                 4000,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "electron threshold for writing hit to digi output"
)
options.register('doBeamspotStudy',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "whether or not to do beamspot study"
)
options.register('doPileup',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "whether or not to produce pileup text files as well"
)
options.register('wantBinaryOutput',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "whether or not to produce binary output"
)
options.register('phiAtZero',
                 True,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "phi at zero"
)
options.register('runFourTelescopes',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "run four telescopes"
)
options.register('r',
                 0,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "value of r_beamspot"
)
options.register('cylinderdZ',
                3.0,
                VarParsing.multiplicity.singleton,
                VarParsing.varType.float,
                "delta Z of cylinder used to test if 3-fold coinc is from IP"
)
options.register('cylinderR',
                29.0,
                VarParsing.multiplicity.singleton,
                VarParsing.varType.float,
                "radius of cylinder used to test if 3-fold coinc is from IP"
)
options.register('inputCfi',
                'DUMMY',
                VarParsing.multiplicity.singleton,
                VarParsing.varType.string,
                "which cfi if any to pass as input"
)
options.register('reportEvery', 10,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=10)"
)
## 'maxEvents' and 'outputFile' are already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)
options.parseArguments()



import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

#source files
# process.load("Analyzers.PLTSimHitAnalyzer.minbiaspileup_cfi")
# process.load("Analyzers.PLTSimHitAnalyzer.muongun_largerange_cfi")
# process.load("Analyzers.PLTSimHitAnalyzer.MinBias14TeV_NoSmear_cfi")
# phi = 0
# if not options.phiAtZero:
#   phi = 225
# process.load("Analyzers.PLTSimHitAnalyzer.MinBiasBeamSpotPhi%iR%i_cfi"%(phi,options.r))

#if cfi file passed in at runtime, use it as input
if options.inputCfi != "DUMMY":
    process.load("Analyzers.PLTSimHitAnalyzer."+options.inputCfi)
#if no file is passed in at runtime, use this as the input
else:
    process.source = cms.Source("PoolSource",
            fileNames = cms.untracked.vstring(
                #"file:/uscms_data/d3/skaplan/PLT/sim/CMSSW_7_1_0_pre4/src/outfile14TeV.root"
                #'/store/user/skaplan/MinBiasBeamSpotPhi0R0/outfile14TeV_18_1_OfZ.root'
                # '/store/user/skaplan/noreplica/MinBias14TeV/outfile14TeVSKIM_313_1_qk7.root'
                "/store/user/skaplan/noreplica/MinBias_WithSimTracks/outfile14TeVSKIM_33_1_oLh.root"
            )
    )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.TFileService = cms.Service("TFileService",
        fileName = cms.string(options.outfilename)
)

#file name of digi output. The file endings will be added in the analyzer (as the base name is used more than once)
digifilename = options.outfilename[:-5]+"_digioutput"

#maybe have these paramateters as ones that can be passed in via VarParsing?
process.simhitplots = cms.EDAnalyzer('PLTSimHitAnalyzer',
    #feed this into .cc file
    PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM"),
    #doBeamspotStudy = cms.bool(options.doBeamspotStudy),
    #phiAtZero = cms.bool(options.phiAtZero),
    #r = cms.int32(options.r),
        #runFourTelescopes = cms.bool(options.runFourTelescopes),
    digiFileName = cms.string(digifilename),
    doPileup = cms.bool(options.doPileup),
    threshold = cms.int32(options.threshold),
    wantBinaryOutput = cms.bool(options.wantBinaryOutput), #flag to create additional binary output as well as the text
    cylinderR = cms.double(options.cylinderR),
    cylinderdZ = cms.double(options.cylinderdZ)
)


process.p = cms.Path(process.simhitplots)
