from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "pltsimhitplots.root",
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

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/user/skaplan/MinBiasTestEvents/outfile_101_1_VRZ.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_103_1_lQo.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_105_1_fN5.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_106_1_8GT.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_107_1_qHW.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_108_1_ajf.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_10_1_B4A.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_110_1_87x.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_111_1_7sO.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_112_1_VAh.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_114_2_GaR.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_116_2_SlD.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_117_1_IZ2.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_118_1_EUU.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_11_2_Yxy.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_120_1_jCr.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_121_2_zSp.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_124_1_X5y.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_125_1_sil.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_126_1_gS8.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_130_1_dIw.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_132_1_rcv.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_133_1_w0O.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_134_1_gPy.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_135_2_70h.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_136_1_nzr.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_137_1_a6C.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_139_1_XA2.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_13_1_01k.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_141_1_WX6.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_147_1_PGl.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_149_1_lis.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_14_1_aYA.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_151_1_GKc.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_152_1_NAV.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_153_1_CNw.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_154_1_qEp.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_155_1_WDY.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_156_1_Xx0.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_157_1_xE2.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_158_1_Vpm.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_159_1_oyI.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_15_2_NWA.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_160_1_lAV.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_161_1_bwi.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_163_1_6dt.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_165_1_waz.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_166_1_qie.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_167_1_Yy5.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_169_1_AHp.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_16_2_dnS.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_172_1_4Kj.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_173_1_Y4V.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_174_1_3Sd.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_178_1_AFn.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_17_1_ZlM.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_182_1_DnD.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_185_1_Ehd.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_186_1_2lr.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_18_1_BsA.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_190_1_yJO.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_192_1_LWA.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_193_1_QVG.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_197_1_kwl.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_198_1_Azz.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_1_1_PyP.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_200_1_DdW.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_21_1_ykv.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_22_1_Zns.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_23_2_iia.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_24_2_b3G.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_25_1_y1W.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_27_1_Hxl.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_29_2_a8Q.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_2_1_ZpX.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_30_2_fxZ.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_31_1_VI8.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_32_2_otT.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_33_1_0HG.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_34_1_Mhh.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_35_1_H7E.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_36_2_qZz.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_37_2_uef.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_39_1_JbR.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_3_1_ERh.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_43_1_53Z.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_44_2_07u.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_45_2_2zF.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_46_1_fVv.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_47_1_cFC.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_51_1_E7W.root',
								#'/store/user/skaplan/MinBiasTestEvents/outfile_53_1_KmF.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_55_2_ara.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_56_1_bqM.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_57_1_sHo.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_58_2_3b6.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_61_1_Iox.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_62_1_z0b.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_63_2_emX.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_65_1_Tlw.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_67_1_bUW.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_68_1_y5w.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_69_1_uXU.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_72_1_qCA.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_73_1_8Z9.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_75_1_6WE.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_76_1_7nz.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_77_1_mpR.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_78_1_OtG.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_79_1_Wli.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_7_1_CyT.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_80_1_NeP.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_81_1_rf3.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_82_2_SM8.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_83_2_Y8M.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_84_1_gZn.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_85_1_6cW.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_86_1_SkV.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_87_2_N1c.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_88_2_d00.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_8_2_45g.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_90_1_FCL.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_91_2_4Wq.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_93_1_gVe.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_95_1_J2E.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_98_1_rQg.root',
								'/store/user/skaplan/MinBiasTestEvents/outfile_9_1_byz.root',
								)

)


process.TFileService = cms.Service("TFileService",
fileName = cms.string(options.outfilename)
)

process.demo = cms.EDAnalyzer('PLTSimHitAnalyzer',
#feed this into .cc file
PLTHits = cms.InputTag("g4SimHits","PLTHits","SIM")
)


process.p = cms.Path(process.demo)
