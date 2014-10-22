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
options.register('applyPixelMask',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 "whether or not to apply a pixel mask"
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
                #"/store/user/skaplan/noreplica/MinBias_WithSimTracks/outfile14TeVSKIM_33_1_oLh.root"
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_1000_1_IDa.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_100_1_LKc.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_101_1_UFz.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_102_1_ktE.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_103_1_qHK.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_104_1_e3t.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_105_1_etr.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_106_1_RMI.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_107_1_VMZ.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_108_1_qcM.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_109_1_bXL.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_10_1_lXA.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_110_1_ERO.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_111_1_lDW.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_112_1_zQs.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_113_1_r2L.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_114_1_WgQ.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_115_1_JIh.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_116_1_fcz.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_117_1_81I.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_118_1_Bxm.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_119_1_VSH.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_11_1_qXg.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_120_1_x4L.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_121_1_3iq.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_122_1_C1T.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_123_1_x4p.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_124_1_4DA.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_125_1_CWd.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_126_1_qzC.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_127_1_waR.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_128_1_4GC.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_129_1_sUV.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_12_1_lqZ.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_130_1_YOB.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_131_1_9t1.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_132_1_jcW.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_133_1_sLO.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_134_1_aVI.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_135_1_O3a.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_136_1_2os.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_137_1_GN1.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_138_1_kU8.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_139_1_MHF.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_13_1_D8S.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_140_1_m6m.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_141_1_y8V.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_142_1_u3Q.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_143_1_O5n.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_144_1_Y2E.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_145_1_V65.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_146_1_BVf.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_147_1_xA5.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_148_1_ccr.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_149_1_6L4.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_14_1_vol.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_150_1_63a.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_151_1_PnC.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_152_1_TNG.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_153_1_Ad7.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_154_1_QEI.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_155_1_QV7.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_156_1_xEj.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_157_1_txJ.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_158_1_FTm.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_159_1_xlp.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_15_1_LvL.root',
                '/store/user/skaplan/noreplica/MinBias14TeV_NoSmear/outfile14TeVSKIM_160_1_yKE.root',
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
    cylinderdZ = cms.double(options.cylinderdZ),
    applyPixelMask = cms.bool(options.applyPixelMask)
)


process.p = cms.Path(process.simhitplots)
