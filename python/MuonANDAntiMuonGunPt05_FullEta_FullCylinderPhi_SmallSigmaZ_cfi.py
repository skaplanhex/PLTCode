import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_100_1_t7I.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_10_1_nVN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_11_1_XCC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_12_1_3L2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_13_1_1Yc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_14_1_ucB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_15_1_6mc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_16_1_mDb.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_17_1_B7B.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_18_1_KFT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_19_1_Izh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_1_1_7UB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_20_1_Qwf.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_21_1_RvY.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_22_1_MTZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_23_1_auv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_24_1_lDY.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_25_1_qje.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_26_1_RMw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_27_1_dQX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_28_1_JEy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_29_1_ge8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_2_1_8Bd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_30_1_Z3C.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_31_1_RRc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_32_1_t1r.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_33_1_LAZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_34_1_d1U.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_35_1_NNt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_36_1_8Ih.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_37_1_usu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_38_1_v4Z.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_39_1_x2z.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_3_1_k9Y.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_40_1_2Bc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_41_1_qdJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_42_1_hqo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_43_1_YtR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_44_1_EZ7.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_45_1_1kV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_46_1_WRB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_47_1_SWA.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_48_1_Ui2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_49_1_8bR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_4_1_sGi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_50_1_IBX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_51_1_DJN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_52_1_1jq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_53_1_3W8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_55_1_2Tm.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_56_1_8rN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_57_1_zmB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_58_1_0mH.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_59_1_Tg4.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_5_1_LnX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_60_1_JLC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_61_1_7bB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_62_1_Tcp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_63_1_TGc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_64_1_Ycc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_65_1_bWq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_66_1_MYu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_67_1_2db.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_68_1_hmK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_69_1_aCO.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_6_1_nvm.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_70_1_hEi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_71_1_8R6.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_72_1_gOl.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_73_1_0oI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_74_1_74y.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_75_1_Mjv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_76_1_Yip.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_77_1_VXN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_78_1_Qfn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_79_1_1Vn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_7_1_4q9.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_80_1_VVL.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_81_1_NJH.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_82_1_Cux.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_83_1_VPn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_84_1_tdP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_85_1_xma.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_86_1_AcD.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_87_1_Mzo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_88_1_DPd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_89_1_Cfw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_8_1_84c.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_90_1_07P.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_91_1_3yv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_92_1_EQJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_93_1_cwN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_94_1_b05.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_95_1_LaB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_96_1_dCV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_97_1_afh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_98_1_W83.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_99_1_2Wk.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_9_1_KHN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_100_1_CWy.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_10_1_iYv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_11_1_c6R.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_12_1_0SY.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_13_1_RzY.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_14_1_tbh.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_15_1_Tua.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_16_1_9Ss.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_17_1_w3J.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_18_1_FNs.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_19_1_yXN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_1_1_dYq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_20_1_pCU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_21_1_AXw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_22_1_2Yj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_23_1_o7t.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_24_1_XbE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_25_1_oyy.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_26_1_kpX.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_27_1_ROm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_28_1_wVb.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_29_1_2qL.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_2_1_jpU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_30_1_BXB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_31_1_JN8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_32_1_SEi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_33_1_mpQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_34_1_VSU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_35_1_CLT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_36_1_SNw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_37_1_ehP.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_38_1_nlm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_39_1_v55.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_3_1_4UJ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_40_1_s3r.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_41_1_r4H.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_42_1_6BR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_43_1_0XX.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_44_1_A71.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_45_1_Usz.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_46_1_9m9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_47_1_iBr.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_48_1_d8I.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_49_1_omE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_4_1_Vvs.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_50_1_hne.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_51_1_Cj6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_52_1_Cxf.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_53_1_JaX.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_54_1_xQR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_55_1_9fN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_56_1_MY1.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_57_1_4az.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_58_1_alJ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_59_1_Nuk.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_5_1_mJq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_60_1_sGo.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_61_1_U0C.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_62_1_JB9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_63_1_Y7t.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_64_1_nYi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_65_1_lhZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_66_1_R3N.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_67_1_j0E.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_68_1_EQr.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_69_1_fxZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_6_1_k2H.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_70_1_BYS.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_71_1_MQG.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_72_1_drs.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_73_1_FDb.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_74_1_o6v.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_75_1_Fvk.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_76_1_vJZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_77_1_yJA.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_78_1_vfq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_79_1_JqK.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_7_1_xbR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_80_1_8sf.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_81_1_1pg.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_82_1_t9w.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_83_1_xyP.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_84_1_eh9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_85_1_zAe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_86_1_bRA.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_87_1_Q09.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_88_1_Krj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_89_1_iBL.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_8_1_STv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_90_1_rid.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_91_1_Qum.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_92_1_l9s.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_93_1_zRt.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_94_1_UOj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_95_1_sp3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_96_1_5ke.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_97_1_5FQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_98_1_Dqa.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_99_1_bNz.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt05/FullEta_FullCylinderPhi_SmallSigmaZ/MuonGunEvents_9_1_eYY.root',
    )

)
