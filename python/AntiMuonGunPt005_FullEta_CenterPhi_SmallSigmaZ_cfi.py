import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_100_1_RXN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_10_1_Lue.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_11_1_DjZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_12_1_gqk.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_13_1_kCM.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_14_1_gzn.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_15_1_cFN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_16_1_mIy.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_17_1_gzS.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_18_1_ABB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_19_1_Sef.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_1_1_M1K.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_20_1_j8K.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_21_1_EOe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_22_1_k2t.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_23_1_jpu.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_24_1_IRe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_25_1_NyQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_26_1_Pi3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_27_1_F3I.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_28_1_PjR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_29_1_7aU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_2_1_or6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_30_1_w94.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_31_1_cis.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_32_1_rIi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_33_1_fZF.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_34_1_W4Z.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_35_1_Wi1.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_36_1_5Wj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_37_1_A9X.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_38_1_nt5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_39_1_pwc.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_3_1_2kw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_40_1_KWC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_41_1_9Re.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_42_1_XRB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_43_1_x19.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_44_1_jQq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_45_1_ax8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_46_1_eZi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_47_1_UFf.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_48_1_gL9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_49_1_nbi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_4_1_qeO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_50_1_z3u.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_51_1_OJB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_52_1_clM.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_53_1_CAZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_54_1_OnT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_55_1_AsU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_56_1_TUu.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_57_1_9F7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_58_1_EhI.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_59_1_jl4.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_5_1_VJF.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_60_1_KQO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_61_1_StJ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_62_1_6Ed.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_63_1_yvx.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_64_1_dVO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_65_1_sum.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_66_1_v6h.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_67_1_KWp.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_68_1_Web.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_69_1_jnI.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_6_1_eyZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_70_1_chW.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_71_1_dZU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_72_1_rY4.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_73_1_5of.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_74_1_eoE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_75_1_4v6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_76_1_tQq.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_77_1_AnR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_78_1_sIP.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_79_1_CoO.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_7_1_SM7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_80_1_vv2.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_81_1_kUL.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_82_1_xjS.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_83_1_3Yr.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_84_1_vzv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_85_1_Iec.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_86_1_L9r.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_87_1_exT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_88_1_LOd.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_89_1_v5H.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_8_1_R8j.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_90_1_0yf.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_91_1_fKm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_92_1_Da5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_93_1_ujA.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_94_1_p4J.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_95_1_rQw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_96_1_WG9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_97_1_RXz.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_98_1_eQG.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_99_1_hAE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/FullEta_CenterPhi_SmallSigmaZ/MuonGunEvents_9_1_SBK.root',
    )

)
