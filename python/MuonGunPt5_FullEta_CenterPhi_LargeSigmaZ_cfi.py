import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_100_1_srU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_10_1_jPE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_11_1_vHU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_12_1_Lwb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_13_1_oAa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_14_1_eem.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_15_1_lqr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_16_1_d0W.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_17_1_iYx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_18_1_a68.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_19_1_Pui.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_1_1_1wQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_20_1_c0u.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_21_1_o8H.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_22_1_oZ0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_23_1_yzK.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_24_1_3Om.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_25_1_EYy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_26_1_q4q.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_27_1_MSY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_28_1_b6i.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_29_1_zvC.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_2_1_6PR.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_30_1_GjN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_31_1_VDn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_32_1_B4G.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_33_1_tNl.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_34_1_XgG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_35_1_sOc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_36_1_Zp9.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_37_1_djH.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_38_1_DLu.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_39_1_KaO.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_3_1_Pf6.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_40_1_qjM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_41_1_Czm.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_42_1_wO7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_43_1_mVw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_44_1_B1g.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_45_1_eOm.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_46_1_dgR.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_47_1_1un.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_48_1_mbT.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_49_1_dm5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_4_1_QHH.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_50_1_J1H.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_51_1_qIE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_52_1_vyf.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_53_1_6pe.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_54_1_NWt.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_55_1_1HO.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_56_1_OyV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_57_1_Npq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_58_1_znY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_59_1_rqL.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_5_1_Vd1.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_60_1_x10.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_61_1_WI9.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_62_1_68W.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_63_1_aX8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_64_1_b1X.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_65_1_gav.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_66_1_pqj.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_67_1_tGD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_68_1_Shy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_69_1_Bhb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_6_1_D5V.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_70_1_dfc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_71_1_kAw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_72_1_QCn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_73_1_MQa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_74_1_R0J.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_75_1_cju.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_76_1_DO3.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_77_1_NY1.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_78_1_cxg.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_79_1_xQn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_7_1_XS0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_80_1_RmU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_81_1_221.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_82_1_zqY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_83_1_5nD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_84_1_H1D.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_85_1_3Zi.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_86_1_QzZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_87_1_qCb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_88_1_oUN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_89_1_ip0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_8_1_CJn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_90_1_X2M.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_91_1_wKG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_92_1_tZl.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_93_1_nUA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_94_1_D3t.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_95_1_3b5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_96_1_QH5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_97_1_fB4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_98_1_qfP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_99_1_b6q.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_LargeSigmaZ/MuonGunEvents_9_1_ON3.root',
    )

)
