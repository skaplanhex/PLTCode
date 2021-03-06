import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_101_1_pND.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_103_1_bkW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_104_1_i5m.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_107_1_URP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_10_1_C9B.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_113_1_6eo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_117_1_Op8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_118_1_3CK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_119_1_7wj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_11_1_5iW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_120_1_Grc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_124_1_8MT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_125_1_zl0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_126_1_4RA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_127_1_8xI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_129_1_bTX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_12_1_e5j.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_130_1_tu2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_131_1_H65.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_132_1_n2t.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_132_1_pU6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_134_1_EcM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_135_1_RxT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_138_1_kKW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_13_1_BtX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_140_1_g8u.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_144_1_ptL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_145_1_wwZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_146_1_f7i.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_147_1_hSO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_148_1_UDg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_149_1_DwW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_14_1_0r0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_151_1_DrK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_152_1_5tk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_153_1_0aK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_156_1_QEE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_159_1_L54.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_15_1_QC6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_160_1_XId.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_161_1_pmE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_166_1_W70.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_167_1_0qk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_169_1_qwx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_16_1_4H2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_172_1_B9h.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_173_1_av6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_175_1_4VD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_176_1_n7X.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_17_1_cIC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_181_1_M4o.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_182_1_790.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_184_1_lP1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_186_1_Byz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_187_1_3ix.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_188_1_g4G.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_189_1_YjD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_18_1_keA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_190_1_crd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_191_1_K6y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_192_1_2FX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_19_1_Y8d.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_1_1_HzN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_200_1_OvB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_20_1_7PD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_21_1_Bkz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_22_1_Ndn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_23_1_dXT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_24_1_CkV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_25_1_GYy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_26_1_oCl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_27_1_2aV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_28_1_c0L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_29_1_plU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_2_1_Sd3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_30_1_nj7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_31_1_S3B.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_32_1_mif.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_33_1_2rn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_34_1_hyp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_35_1_iPi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_37_1_Lg0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_3_1_RwN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_4_1_0nH.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_55_1_Ewa.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_5_1_9vl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_6_1_GBC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_76_1_5HE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_7_1_H26.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_84_1_8iq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_8_1_U3d.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R10_HISTATS/outfile14TeVSKIM_9_1_p47.root',
	)

)
