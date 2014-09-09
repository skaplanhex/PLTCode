import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_100_1_s8P.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_10_1_RKm.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_11_1_ZDi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_12_1_ESS.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_13_1_NQC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_14_1_PJP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_15_1_4EQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_16_1_9Vn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_17_1_wSg.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_18_1_rxJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_19_1_XFy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_1_1_Leu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_20_1_yeZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_21_1_PIm.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_22_1_5eR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_23_1_AuI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_24_1_xS5.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_25_1_fZ4.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_26_1_dDX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_27_1_Hcs.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_28_1_mF6.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_29_1_22Z.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_2_1_N3P.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_30_1_nNp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_31_1_nVQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_32_1_YzK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_33_1_M9G.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_34_1_Hnv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_35_1_MUF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_36_1_YRz.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_37_1_F2o.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_38_1_kKe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_39_1_wXQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_3_1_8Gc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_40_1_uBi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_41_1_oz2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_42_1_W4K.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_43_1_G4g.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_44_1_ynl.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_45_1_Ee3.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_46_1_4kC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_47_1_hfp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_48_1_H3j.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_49_1_n8P.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_4_1_1wo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_50_1_mnV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_51_1_2uG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_52_1_9iM.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_53_1_LMr.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_54_1_77w.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_55_1_HcP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_56_1_wJR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_57_1_gmJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_58_1_eHw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_59_1_sil.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_5_1_30A.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_60_1_myB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_61_1_Ml9.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_62_1_w08.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_63_1_y5c.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_64_1_nSV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_65_1_Hbh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_66_1_uER.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_67_1_rLB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_68_1_Hsp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_69_1_NHd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_6_1_nES.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_70_1_1Hy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_71_1_m8o.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_72_1_gIO.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_73_1_mC3.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_74_1_ZpK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_75_1_PmW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_76_1_Gli.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_77_1_bdt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_78_1_faA.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_79_1_YuG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_7_1_fFF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_80_1_Gxf.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_81_1_oGU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_82_1_eTd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_83_1_zDe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_84_1_KhZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_85_1_Bai.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_86_1_HN4.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_87_1_Ixl.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_88_1_6X0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_89_1_XrM.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_8_1_6pi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_90_1_5ZX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_91_1_z1h.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_92_1_Cap.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_93_1_gAP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_94_1_pcu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_95_1_kBJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_96_1_DVB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_97_1_3uo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_98_1_9fz.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_99_1_7zU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_9_1_SbQ.root',
    )

)
