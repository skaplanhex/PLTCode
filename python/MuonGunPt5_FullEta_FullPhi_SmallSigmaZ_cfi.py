import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_100_1_jWC.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_10_1_Z2J.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_11_1_40J.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_12_1_tds.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_13_1_Gi0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_14_1_VsH.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_15_1_mfr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_16_1_S6y.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_17_1_mt4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_18_1_oL5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_19_1_Tb8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_1_1_5bt.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_20_1_VS6.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_21_1_8xk.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_22_1_yQy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_23_1_eMt.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_24_1_52o.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_25_1_17t.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_26_1_iOA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_27_1_KFa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_28_1_7QG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_29_1_qnM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_2_1_bbA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_30_1_X4R.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_31_1_XE7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_32_1_rUx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_33_1_Lt5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_34_1_T5x.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_35_1_pJd.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_36_1_PqO.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_37_1_qKw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_38_1_ffo.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_39_1_2PD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_3_1_LN9.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_40_1_jGn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_41_1_cDr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_42_1_LDp.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_43_1_2Mn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_44_1_cLm.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_45_1_AvZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_46_1_7G8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_47_1_iPC.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_48_1_88g.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_49_1_o39.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_4_1_la0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_50_1_i8b.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_51_1_wLq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_52_1_m1W.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_53_1_nj3.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_54_1_jZ8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_55_1_bd7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_56_1_6Wa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_57_1_jQc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_58_1_7g4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_59_1_yVX.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_5_1_h6M.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_60_1_BgN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_61_1_Myh.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_62_1_kGT.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_63_1_EQd.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_64_1_hEq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_65_1_UuP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_66_1_PLw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_67_1_Wbs.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_68_1_p0a.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_69_1_Iyr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_6_1_312.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_70_1_ijS.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_71_1_PIG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_72_1_IB7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_73_1_7u4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_74_1_g8O.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_75_1_og5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_76_1_gJH.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_77_1_nTx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_78_1_JjP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_79_1_1eU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_7_1_NdK.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_80_1_F2J.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_81_1_vPA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_82_1_1pP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_83_1_VEP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_84_1_xPx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_85_1_V1j.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_86_1_hw5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_87_1_MxV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_88_1_LZc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_89_1_g9v.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_8_1_1AD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_90_1_Hkw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_91_1_bDq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_92_1_7Bk.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_93_1_pQV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_94_1_rYK.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_95_1_ntR.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_96_1_6Gu.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_97_1_5VE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_98_1_t0M.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_99_1_E9y.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_FullPhi_SmallSigmaZ/MuonGunEvents_9_1_Mt8.root',
    )

)
