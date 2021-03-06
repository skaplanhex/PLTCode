import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_100_1_SUH.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_10_1_iil.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_11_1_brE.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_12_1_dLI.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_13_1_NdH.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_14_1_yIq.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_15_1_cSs.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_16_1_hjF.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_17_1_uLO.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_18_1_s0c.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_19_1_VKe.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_1_1_h6J.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_20_1_yr3.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_21_1_fap.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_22_1_BXN.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_23_1_6c1.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_24_1_vie.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_25_1_lxg.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_26_1_DlT.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_27_1_x5O.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_28_1_q3g.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_29_1_aaY.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_2_1_cNn.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_30_1_bwn.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_31_1_g7I.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_32_1_TYZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_33_1_jco.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_34_1_pXj.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_35_1_kQF.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_36_1_YyW.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_37_1_Vcm.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_38_1_sk8.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_39_1_BCZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_3_1_IhM.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_40_1_1zV.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_41_1_NC6.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_42_1_2KH.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_43_1_aRc.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_44_1_r1V.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_45_1_jzK.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_46_1_NP6.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_47_1_66A.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_48_1_Qwm.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_49_1_VLZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_4_1_xVP.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_50_1_Q4D.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_51_1_NWc.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_52_1_OkQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_53_1_gtk.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_54_1_nXt.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_55_1_cdb.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_56_1_Jq8.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_57_1_F3R.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_58_1_wXY.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_59_1_YHc.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_5_1_Nhe.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_60_1_398.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_61_1_zQ4.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_62_1_qcf.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_63_1_eXY.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_64_1_eYR.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_65_1_Eum.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_66_1_PXF.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_67_1_XxD.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_68_1_7Po.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_69_1_5dp.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_6_1_dJ2.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_70_1_aUQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_71_1_o7y.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_72_1_Ljg.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_73_1_TY2.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_74_1_KGQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_75_1_pub.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_76_1_slY.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_77_1_lNv.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_78_1_VTz.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_79_1_Dfd.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_7_1_U7l.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_80_1_37s.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_81_1_Df0.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_82_1_MJj.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_83_1_Qr2.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_84_1_tIu.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_85_1_EmS.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_86_1_QyM.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_87_1_O3u.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_88_1_w61.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_89_1_0ZG.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_8_1_4V6.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_90_1_k9s.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_91_1_5yN.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_92_1_1No.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_93_1_peS.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_94_1_hrY.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_95_1_gXc.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_96_1_8PA.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_97_1_xu9.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_98_1_qfV.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_99_1_bw0.root',
        '/store/user/skaplan/noreplica/MuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_9_1_2Ok.root',
    )

)
