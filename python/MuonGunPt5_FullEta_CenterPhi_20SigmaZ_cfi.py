import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_100_1_vqD.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_10_1_U42.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_11_1_5KY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_12_1_L4b.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_13_1_1vg.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_14_1_G7G.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_15_1_srM.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_16_1_0AA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_17_1_MLj.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_18_1_GFs.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_19_1_Mgy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_1_1_8fY.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_20_1_XBz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_21_1_hk1.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_22_1_Igz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_23_1_Dm9.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_24_1_RDb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_25_1_l1s.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_26_1_sl7.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_27_1_QiF.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_28_1_m06.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_29_1_472.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_2_1_vqX.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_30_1_obN.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_31_1_3pz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_32_1_61h.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_33_1_D6y.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_34_1_UmA.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_35_1_iOn.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_36_1_77n.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_37_1_hcr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_38_1_wru.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_39_1_fiV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_3_1_yHk.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_40_1_moG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_41_1_Fq5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_42_1_WHP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_43_1_rns.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_44_1_SZX.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_45_1_Q2N.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_46_1_ccT.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_47_1_SKo.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_48_1_kLc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_49_1_G8b.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_4_1_zf8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_50_1_loo.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_51_1_kak.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_52_1_xny.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_53_1_kyF.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_54_1_zD3.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_55_1_MlO.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_56_1_VV9.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_57_1_2Zp.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_58_1_fl0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_59_1_JlS.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_5_1_1Wa.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_60_1_81X.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_61_1_KK8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_62_1_9Ei.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_63_1_QPo.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_64_1_uJb.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_65_1_imF.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_66_1_K96.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_67_1_VCF.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_68_1_9BV.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_69_1_3Iz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_6_1_4ei.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_70_1_VMt.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_71_1_Bty.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_72_1_qF2.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_73_1_05h.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_74_1_Q4r.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_75_1_1tr.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_76_1_4qG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_77_1_3k5.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_78_1_wDS.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_79_1_fql.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_7_1_S7p.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_80_1_1PH.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_81_1_x3t.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_82_1_yuZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_83_1_MDG.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_84_1_Hfp.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_85_1_w6g.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_86_1_CXh.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_87_1_MJ1.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_88_1_qHP.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_89_1_avF.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_8_1_lkW.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_90_1_7T6.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_91_1_DO8.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_92_1_di6.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_93_1_WIy.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_94_1_psW.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_95_1_hmc.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_96_1_ykf.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_97_1_8o0.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_98_1_41H.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_99_1_5fz.root',
        '/store/user/skaplan/noreplica/MuonGunPt5/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_9_1_qRw.root',
    )

)