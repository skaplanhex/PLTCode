import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_100_1_AHG.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_10_1_69V.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_11_1_KBe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_12_1_d1y.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_13_1_NNd.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_14_1_QfZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_15_1_jbE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_16_1_P5T.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_17_1_pgi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_18_1_8RP.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_19_1_EZN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_1_1_z6T.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_20_1_DUi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_21_1_M4k.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_22_1_rSR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_23_1_vKn.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_24_1_Ypa.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_25_1_Udd.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_26_1_dgQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_27_1_rKo.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_28_1_rA3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_29_1_hbU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_2_1_o0b.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_30_1_tz5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_31_1_AIx.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_32_1_4W8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_33_1_5dE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_34_1_Ew2.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_35_1_RnF.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_36_1_E7w.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_37_1_HvD.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_38_1_wt1.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_39_1_wJU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_3_1_FpR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_40_1_pMW.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_41_1_UuM.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_42_1_5D5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_43_1_EYJ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_44_1_et7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_45_1_hYT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_46_1_zgR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_47_1_75Z.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_48_1_OIe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_49_1_PAC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_4_1_iEv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_50_1_Po4.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_51_1_H0Z.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_52_1_6as.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_53_1_tOq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_54_1_4f5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_55_1_oJO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_56_1_lNt.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_57_1_Yg7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_58_1_Fd8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_59_1_KbO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_5_1_S4P.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_60_1_G88.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_61_1_NWG.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_62_1_GKC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_63_1_wHr.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_64_1_0M1.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_65_1_eQG.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_66_1_4Ot.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_67_1_bz2.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_68_1_Cp9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_69_1_uAd.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_6_1_r7x.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_70_1_Pc3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_71_1_L1b.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_72_1_ejM.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_73_1_Ge7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_74_1_gQQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_75_1_CvM.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_76_1_khV.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_77_1_bP4.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_78_1_dR9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_79_1_Yfu.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_7_1_qOB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_80_1_XQ0.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_81_1_Okb.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_82_1_0V3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_83_1_NJw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_84_1_ZiB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_85_1_Wvg.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_86_1_iQp.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_87_1_SzC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_88_1_tLP.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_89_1_siA.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_8_1_Ec2.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_90_1_Qly.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_91_1_e4u.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_92_1_tOB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_93_1_1OY.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_94_1_VUB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_95_1_972.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_96_1_J6G.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_97_1_fZV.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_98_1_tnv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_99_1_N4f.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_9_1_F5e.root',
    )

)
