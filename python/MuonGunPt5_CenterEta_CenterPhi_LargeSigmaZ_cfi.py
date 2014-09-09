import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_100_1_AT1.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_10_1_gSE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_11_1_Sb4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_12_1_j9J.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_13_1_3gT.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_14_1_Fu4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_15_1_Xvi.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_16_1_8YK.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_17_1_tEc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_18_1_Sp2.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_19_1_rpU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_1_1_d7g.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_20_1_b5T.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_21_1_urJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_22_1_qUc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_23_1_jeR.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_24_1_VbB.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_25_1_GW4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_26_1_IIU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_27_1_eP8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_28_1_VUG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_29_1_w52.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_2_1_aKJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_30_1_uxM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_31_1_49h.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_32_1_y4i.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_33_1_dgw.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_34_1_NXV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_35_1_xTM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_36_1_QZU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_37_1_PAM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_38_1_uy2.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_39_1_tCE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_3_1_9a4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_40_1_Nak.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_41_1_swS.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_42_1_y7E.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_43_1_r51.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_44_1_3w2.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_45_1_Ddg.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_46_1_PgI.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_47_1_ruc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_48_1_h9T.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_49_1_S0q.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_4_1_E1k.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_50_1_0qs.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_51_1_cIv.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_52_1_7qy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_53_1_5aK.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_54_1_saZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_55_1_Wpr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_56_1_Ojt.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_57_1_Ix5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_58_1_iGo.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_59_1_AEu.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_5_1_VLx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_60_1_mXE.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_61_1_a4G.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_62_1_Aq3.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_63_1_kyA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_64_1_4eq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_65_1_pEe.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_66_1_ILa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_67_1_6hZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_68_1_Gma.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_69_1_0Vq.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_6_1_5qb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_70_1_8GN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_71_1_gqx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_72_1_g7n.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_73_1_59d.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_74_1_xxD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_75_1_vp2.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_76_1_cbU.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_77_1_0kQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_78_1_wyi.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_79_1_5p3.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_7_1_AAQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_80_1_UfY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_81_1_nA7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_82_1_RBc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_83_1_Ztc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_84_1_C4w.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_85_1_xOx.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_86_1_Rs0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_87_1_2Ie.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_88_1_v8V.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_89_1_zRi.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_8_1_jmN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_90_1_oLJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_91_1_PGp.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_92_1_x8P.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_93_1_dRz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_94_1_nJb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_95_1_aGX.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_96_1_Cz8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_97_1_teg.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_98_1_4P4.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_99_1_lFA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/CenterEta_CenterPhi_LargeSigmaZ/MuonGunEvents_9_1_Kc9.root',
    )

)
