
import FWCore.ParameterSet.Config as cms

def addHLTdummybranches( process):

  process.hltanalysis.dummyBranches.extend( [
      
      "HLT_HIPuAK4CaloJet40_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet40_Eta5p1_v2"
      ,"HLT_HIPuAK4CaloJet60_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet80_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet80_Eta5p1ForZS_v1"
      ,"HLT_HIPuAK4CaloJet100_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet110_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet120_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet150_Eta5p1_v1"
      ,"HLT_HIPuAK4CaloJet40_Eta5p1_Cent30_100_v1"
      ,"HLT_HIPuAK4CaloJet60_Eta5p1_Cent30_100_v1"
      ,"HLT_HIPuAK4CaloJet80_Eta5p1_Cent30_100_v1"
      ,"HLT_HIPuAK4CaloJet100_Eta5p1_Cent30_100_v1"
      ,"HLT_HIPuAK4CaloJet40_Eta5p1_Cent50_100_v1"
      ,"HLT_HIPuAK4CaloJet60_Eta5p1_Cent50_100_v1"
      ,"HLT_HIPuAK4CaloJet80_Eta5p1_Cent50_100_v1"
      ,"HLT_HIPuAK4CaloJet100_Eta5p1_Cent50_100_v1"
      ,"HLT_HIPuAK4CaloJet80_Jet35_Eta1p1_v1"
      ,"HLT_HIPuAK4CaloJet80_Jet35_Eta0p7_v1"
      ,"HLT_HIPuAK4CaloJet100_Jet35_Eta1p1_v1"
      ,"HLT_HIPuAK4CaloJet100_Jet35_Eta0p7_v1"
      ,"HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloDJet60_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloDJet80_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloBJetCSV60_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloBJetCSV80_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloBJetSSV60_Eta2p1_v1"
      ,"HLT_HIPuAK4CaloBJetSSV80_Eta2p1_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent0_10_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent0_10_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v3"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v3"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt30_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt30_Cent0_10_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt30_Cent0_10_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt30_Cent30_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt30_Cent50_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt40_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt40_Cent0_10_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt40_Cent0_10_v2"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt40_Cent30_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt40_Cent50_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt50_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt60_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt70_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt60_Cent30_100_v1"
      ,"HLT_HIDmesonHITrackingGlobal_Dpt60_Cent50_100_v1"
      ,"HLT_HISinglePhoton10_Eta1p5_v1"
      ,"HLT_HISinglePhoton10_Eta1p5_v2"
      ,"HLT_HISinglePhoton15_Eta1p5_v1"
      ,"HLT_HISinglePhoton15_Eta1p5_v2"
      ,"HLT_HISinglePhoton20_Eta1p5_v1"
      ,"HLT_HISinglePhoton20_Eta1p5_v2"
      ,"HLT_HISinglePhoton30_Eta1p5_v1"
      ,"HLT_HISinglePhoton40_Eta1p5_v1"
      ,"HLT_HISinglePhoton50_Eta1p5_v1"
      ,"HLT_HISinglePhoton60_Eta1p5_v1"
      ,"HLT_HISinglePhoton10_Eta1p5_Cent50_100_v1"
      ,"HLT_HISinglePhoton15_Eta1p5_Cent50_100_v1"
      ,"HLT_HISinglePhoton20_Eta1p5_Cent50_100_v1"
      ,"HLT_HISinglePhoton30_Eta1p5_Cent50_100_v1"
      ,"HLT_HISinglePhoton40_Eta1p5_Cent50_100_v1"
      ,"HLT_HISinglePhoton10_Eta1p5_Cent30_100_v1"
      ,"HLT_HISinglePhoton15_Eta1p5_Cent30_100_v1"
      ,"HLT_HISinglePhoton20_Eta1p5_Cent30_100_v1"
      ,"HLT_HISinglePhoton30_Eta1p5_Cent30_100_v1"
      ,"HLT_HISinglePhoton40_Eta1p5_Cent30_100_v1"
      ,"HLT_HISinglePhoton40_Eta2p1_v1"
      ,"HLT_HISinglePhoton10_Eta3p1_v1"
      ,"HLT_HISinglePhoton10_Eta3p1_v2"
      ,"HLT_HISinglePhoton15_Eta3p1_v1"
      ,"HLT_HISinglePhoton15_Eta3p1_v2"
      ,"HLT_HISinglePhoton20_Eta3p1_v1"
      ,"HLT_HISinglePhoton20_Eta3p1_v2"
      ,"HLT_HISinglePhoton30_Eta3p1_v1"
      ,"HLT_HISinglePhoton40_Eta3p1_v1"
      ,"HLT_HISinglePhoton50_Eta3p1_v1"
      ,"HLT_HISinglePhoton60_Eta3p1_v1"
      ,"HLT_HISinglePhoton10_Eta3p1_Cent50_100_v1"
      ,"HLT_HISinglePhoton15_Eta3p1_Cent50_100_v1"
      ,"HLT_HISinglePhoton20_Eta3p1_Cent50_100_v1"
      ,"HLT_HISinglePhoton30_Eta3p1_Cent50_100_v1"
      ,"HLT_HISinglePhoton40_Eta3p1_Cent50_100_v1"
      ,"HLT_HISinglePhoton10_Eta3p1_Cent30_100_v1"
      ,"HLT_HISinglePhoton15_Eta3p1_Cent30_100_v1"
      ,"HLT_HISinglePhoton20_Eta3p1_Cent30_100_v1"
      ,"HLT_HISinglePhoton30_Eta3p1_Cent30_100_v1"
      ,"HLT_HISinglePhoton40_Eta3p1_Cent30_100_v1"
      ,"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1"
      ,"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v1"
      ,"HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v1"
      ,"HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v1"
      ,"HLT_HIL2Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v2"
      ,"HLT_HIL2Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v1"
      ,"HLT_HIUCC100_v1"
      ,"HLT_HIUCC100_v2"
      ,"HLT_HIUCC100_v3"
      ,"HLT_HIUCC020_v1"
      ,"HLT_HIUCC020_v2"
      ,"HLT_HIUCC020_v3"
      ,"HLT_HIQ2Bottom005_Centrality1030_v1"
      ,"HLT_HIQ2Bottom005_Centrality1030_v2"
      ,"HLT_HIQ2Bottom005_Centrality1030_v3"
      ,"HLT_HIQ2Top005_Centrality1030_v1"
      ,"HLT_HIQ2Top005_Centrality1030_v2"
      ,"HLT_HIQ2Top005_Centrality1030_v3"
      ,"HLT_HIQ2Bottom005_Centrality3050_v1"
      ,"HLT_HIQ2Bottom005_Centrality3050_v2"
      ,"HLT_HIQ2Bottom005_Centrality3050_v3"
      ,"HLT_HIQ2Top005_Centrality3050_v1"
      ,"HLT_HIQ2Top005_Centrality3050_v2"
      ,"HLT_HIQ2Top005_Centrality3050_v3"
      ,"HLT_HIQ2Bottom005_Centrality5070_v1"
      ,"HLT_HIQ2Bottom005_Centrality5070_v2"
      ,"HLT_HIQ2Bottom005_Centrality5070_v3"
      ,"HLT_HIQ2Top005_Centrality5070_v1"
      ,"HLT_HIQ2Top005_Centrality5070_v2"
      ,"HLT_HIQ2Top005_Centrality5070_v3"
      ,"HLT_HIFullTrack12_L1MinimumBiasHF2_AND_v1"
      ,"HLT_HIFullTrack12_L1Centrality010_v1"
      ,"HLT_HIFullTrack12_L1Centrality010_v2"
      ,"HLT_HIFullTrack12_L1Centrality30100_v1"
      ,"HLT_HIFullTrack18_L1MinimumBiasHF2_AND_v1"
      ,"HLT_HIFullTrack18_L1Centrality010_v1"
      ,"HLT_HIFullTrack18_L1Centrality010_v2"
      ,"HLT_HIFullTrack18_L1Centrality30100_v1"
      ,"HLT_HIFullTrack24_v1"
      ,"HLT_HIFullTrack24_L1Centrality30100_v1"
      ,"HLT_HIFullTrack34_v1"
      ,"HLT_HIFullTrack34_L1Centrality30100_v1"
      ,"HLT_HIFullTrack45_v1"
      ,"HLT_HIFullTrack45_L1Centrality30100_v1"
      ,"HLT_HIL1DoubleMu0_v1"
      ,"HLT_HIL1DoubleMu0_part1_v1"
      ,"HLT_HIL1DoubleMu0_part2_v1"
      ,"HLT_HIL1DoubleMu0_part3_v1"
      ,"HLT_HIL1DoubleMu0_2HF_v1"
      ,"HLT_HIL1DoubleMu0_2HF0_v1"
      ,"HLT_HIL1DoubleMu10_v1"
      ,"HLT_HIL2DoubleMu0_NHitQ_v1"
      ,"HLT_HIL2DoubleMu0_NHitQ_v2"
      ,"HLT_HIL2DoubleMu0_NHitQ_2HF_v1"
      ,"HLT_HIL2DoubleMu0_NHitQ_2HF0_v1"
      ,"HLT_HIL2Mu3_NHitQ10_2HF_v1"
      ,"HLT_HIL2Mu3_NHitQ10_2HF0_v1"
      ,"HLT_HIL3Mu3_NHitQ15_2HF_v1"
      ,"HLT_HIL3Mu3_NHitQ15_2HF0_v1"
      ,"HLT_HIL2Mu5_NHitQ10_2HF_v1"
      ,"HLT_HIL2Mu5_NHitQ10_2HF0_v1"
      ,"HLT_HIL3Mu5_NHitQ15_2HF_v1"
      ,"HLT_HIL3Mu5_NHitQ15_2HF0_v1"
      ,"HLT_HIL2Mu7_NHitQ10_2HF_v1"
      ,"HLT_HIL2Mu7_NHitQ10_2HF0_v1"
      ,"HLT_HIL3Mu7_NHitQ15_2HF_v1"
      ,"HLT_HIL3Mu7_NHitQ15_2HF0_v1"
      ,"HLT_HIL2Mu15_v1"
      ,"HLT_HIL2Mu15_v2"
      ,"HLT_HIL2Mu15_2HF_v1"
      ,"HLT_HIL2Mu15_2HF0_v1"
      ,"HLT_HIL3Mu15_v1"
      ,"HLT_HIL3Mu15_2HF_v1"
      ,"HLT_HIL3Mu15_2HF0_v1"
      ,"HLT_HIL2Mu20_v1"
      ,"HLT_HIL2Mu20_2HF_v1"
      ,"HLT_HIL2Mu20_2HF0_v1"
      ,"HLT_HIL3Mu20_v1"
      ,"HLT_HIL3Mu20_2HF_v1"
      ,"HLT_HIL3Mu20_2HF0_v1"
      ,"HLT_HIL1DoubleMu0_2HF_Cent30100_v1"
      ,"HLT_HIL1DoubleMu0_2HF0_Cent30100_v1"
      ,"HLT_HIL2DoubleMu0_2HF_Cent30100_NHitQ_v1"
      ,"HLT_HIL1DoubleMu0_Cent30_v1"
      ,"HLT_HIL2DoubleMu0_2HF0_Cent30100_NHitQ_v1"
      ,"HLT_HIL2DoubleMu0_Cent30_OS_NHitQ_v1"
      ,"HLT_HIL2DoubleMu0_Cent30_NHitQ_v1"
      ,"HLT_HIL3DoubleMu0_Cent30_v1"
      ,"HLT_HIL3DoubleMu0_Cent30_OS_m2p5to4p5_v1"
      ,"HLT_HIL3DoubleMu0_Cent30_OS_m7to14_v1"
      ,"HLT_HIL3DoubleMu0_OS_m2p5to4p5_v1"
      ,"HLT_HIL3DoubleMu0_OS_m7to14_v1"
      ,"HLT_HIUPCL1SingleMuOpenNotHF2_v1"
      ,"HLT_HIUPCSingleMuNotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotHF2_v1"
      ,"HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1SingleEG2NotHF2_v1"
      ,"HLT_HIUPCSingleEG2NotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleEG2NotHF2_v1"
      ,"HLT_HIUPCDoubleEG2NotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1SingleEG5NotHF2_v1"
      ,"HLT_HIUPCSingleEG5NotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotHF1_v1"
      ,"HLT_HIUPCDoubleMuNotHF1Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleEG2NotZDCAND_v1"
      ,"HLT_HIUPCL1DoubleEG2NotZDCANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotZDCAND_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotZDCANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1EG2NotZDCAND_v1"
      ,"HLT_HIUPCEG2NotZDCANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1MuOpenNotZDCAND_v1"
      ,"HLT_HIUPCL1MuOpenNotZDCANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1NotHFplusANDminusTH0BptxAND_v1"
      ,"HLT_HIUPCL1NotHFplusANDminusTH0BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1NotHFMinimumbiasHFplusANDminustTH0_v1"
      ,"HLT_HIUPCL1NotHFMinimumbiasHFplusANDminustTH0Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotHFMinimumbiasHFplusANDminustTH0_v1"
      ,"HLT_HIUPCL1DoubleMuOpenNotHFMinimumbiasHFplusANDminustTH0Pixel_SingleTrack_v1"
      ,"HLT_HIL1CastorMediumJet_v1"
      ,"HLT_HIL1CastorMediumJetAK4CaloJet20_v1"
      ,"HLT_HICastorMediumJetPixel_SingleTrack_v1"
      ,"HLT_HICastorMediumJetPixel_SingleTrack_v2"
      ,"HLT_HIUPCL1NotMinimumBiasHF2_AND_v1"
      ,"HLT_HIUPCL1NotMinimumBiasHF2_ANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1ZdcOR_BptxAND_v1"
      ,"HLT_HIUPCL1ZdcOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1ZdcXOR_BptxAND_v1"
      ,"HLT_HIUPCL1ZdcXOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1NotZdcOR_BptxAND_v1"
      ,"HLT_HIUPCL1NotZdcOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIZeroBias_v1"
      ,"HLT_HICentralityVeto_v1"
      ,"HLT_HICentralityVeto_v2"
      ,"HLT_HIL1Tech5_BPTX_PlusOnly_v1"
      ,"HLT_HIL1Tech6_BPTX_MinusOnly_v1"
      ,"HLT_HIL1Tech7_NoBPTX_v1"
      ,"HLT_HIL1MinimumBiasHF1OR_v1"
      ,"HLT_HIL1MinimumBiasHF2OR_v1"
      ,"HLT_HIL1MinimumBiasHF1AND_v1"
      ,"HLT_HIL1MinimumBiasHF1ANDExpress_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part1_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part2_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part3_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part4_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part5_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part6_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part7_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part8_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part9_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part10_v1"
      ,"HLT_HIL1MinimumBiasHF2AND_part11_v1"
      ,"HLT_HIL1MinimumBiasHF2ANDExpress_v1"
      ,"HLT_HIL1HFplusANDminusTH0Express_v1"
      ,"HLT_HIL1MinimumBiasHF1ANDPixel_SingleTrack_v1"
      ,"HLT_HIL1MinimumBiasHF2ANDPixel_SingleTrack_v1"
      ,"HLT_HIZeroBiasPixel_SingleTrack_v1"
      ,"HLT_HIL1Centralityext30100MinimumumBiasHF1AND_v1"
      ,"HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part1_v1"
      ,"HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part2_v1"
      ,"HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part3_v1"
      ,"HLT_HIL1Centralityext50100MinimumumBiasHF1AND_v1"
      ,"HLT_HIL1Centralityext50100MinimumumBiasHF2AND_v1"
      ,"HLT_HIL1Centralityext70100MinimumumBiasHF1AND_v1"
      ,"HLT_HIL1Centralityext010MinimumumBiasHF1ANDForZS_v1"
      ,"HLT_HIPhysics_v1"
      ,"HLT_HIPhysicsForZS_v1"
      ,"HLT_HIRandom_v1"
      ,"HLT_EcalCalibration_v1"
      ,"HLT_HcalCalibration_v1"
      ,"HLT_HIPhysicsNoZS_v1"
      ])

def addHLTdummybranchesForPP( process):

  process.hltanalysis.dummyBranches.extend( [
      "HLT_PixelTracks_Multiplicity60_v1"
      ,"HLT_PixelTracks_Multiplicity60_v2"
      ,"HLT_PixelTracks_Multiplicity60_v3"
      ,"HLT_PixelTracks_Multiplicity85_v1"
      ,"HLT_PixelTracks_Multiplicity85_v2"
      ,"HLT_PixelTracks_Multiplicity110_v1"
      ,"HLT_PixelTracks_Multiplicity110_v2"
      ,"HLT_PixelTracks_Multiplicity135_v1"
      ,"HLT_PixelTracks_Multiplicity135_v2"
      ,"HLT_PixelTracks_Multiplicity160_v1"
      ,"HLT_PixelTracks_Multiplicity160_v2"
      ,"HLT_Physics_v1"
      ,"HLT_Physics_v2"
      ,"HLT_Random_v1"
      ,"HLT_EcalCalibration_v1"
      ,"HLT_HcalCalibration_v1"
      ,"HLT_L1Tech6_BPTX_MinusOnly_v1"
      ,"HLT_L1Tech5_BPTX_PlusOnly_v1"
      ,"HLT_L1Tech5_BPTX_PlusOnly_v2"
      ,"HLT_L1Tech7_NoBPTX_v1"
      ,"HLT_L1TOTEM1_MinBias_v1"
      ,"HLT_L1TOTEM2_ZeroBias_v1"
      ,"HLT_L1MinimumBiasHF1OR_v1"
      ,"HLT_L1MinimumBiasHF2OR_v1"
      ,"HLT_L1MinimumBiasHF1AND_v1"
      ,"HLT_L1MinimumBiasHF2AND_v1"
      ,"HLT_L1MinimumBiasHF2ORNoBptxGating_v1"
      ,"HLT_ZeroBias_v1"
      ,"HLT_ZeroBias_v2"
      ,"HLT_ZeroBias_part0_v1"
      ,"HLT_ZeroBias_part0_v2"
      ,"HLT_ZeroBias_part1_v1"
      ,"HLT_ZeroBias_part1_v2"
      ,"HLT_ZeroBias_part2_v1"
      ,"HLT_ZeroBias_part2_v2"
      ,"HLT_ZeroBias_part3_v1"
      ,"HLT_ZeroBias_part3_v2"
      ,"HLT_ZeroBias_part4_v1"
      ,"HLT_ZeroBias_part4_v2"
      ,"HLT_ZeroBias_part5_v1"
      ,"HLT_ZeroBias_part5_v2"
      ,"HLT_ZeroBias_part6_v1"
      ,"HLT_ZeroBias_part6_v2"
      ,"HLT_ZeroBias_part7_v1"
      ,"HLT_ZeroBias_part7_v2"
      ,"HLT_ZeroBias_part8_v1"
      ,"HLT_ZeroBias_part8_v2"
      ,"HLT_ZeroBias_part9_v1"
      ,"HLT_ZeroBias_part9_v2"
      ,"HLT_ZeroBias_part10_v1"
      ,"HLT_ZeroBias_part10_v2"
      ,"HLT_ZeroBias_part11_v1"
      ,"HLT_ZeroBias_part11_v2"
      ,"HLT_ZeroBias_part12_v1"
      ,"HLT_ZeroBias_part12_v2"
      ,"HLT_ZeroBias_part13_v1"
      ,"HLT_ZeroBias_part13_v2"
      ,"HLT_ZeroBias_part14_v1"
      ,"HLT_ZeroBias_part14_v2"
      ,"HLT_ZeroBias_part15_v1"
      ,"HLT_ZeroBias_part15_v2"
      ,"HLT_ZeroBias_part16_v1"
      ,"HLT_ZeroBias_part16_v2"
      ,"HLT_ZeroBias_part17_v1"
      ,"HLT_ZeroBias_part17_v2"
      ,"HLT_ZeroBias_part18_v1"
      ,"HLT_ZeroBias_part18_v2"
      ,"HLT_ZeroBias_part19_v1"
      ,"HLT_ZeroBias_part19_v2"
      ,"HLT_AK4CaloJet40_Eta5p1_v1"
      ,"HLT_AK4CaloJet60_Eta5p1_v1"
      ,"HLT_AK4CaloJet80_Eta5p1_v1"
      ,"HLT_AK4CaloJet100_Eta5p1_v1"
      ,"HLT_AK4CaloJet110_Eta5p1_v1"
      ,"HLT_AK4CaloJet120_Eta5p1_v1"
      ,"HLT_AK4CaloJet150_v1"
      ,"HLT_AK4PFJet40_Eta5p1_v1"
      ,"HLT_AK4PFJet60_Eta5p1_v1"
      ,"HLT_AK4PFJet80_Eta5p1_v1"
      ,"HLT_AK4PFJet100_Eta5p1_v1"
      ,"HLT_AK4PFJet110_Eta5p1_v1"
      ,"HLT_AK4PFJet120_Eta5p1_v1"
      ,"HLT_AK4CaloJet80_Jet35_Eta1p1_v1"
      ,"HLT_AK4CaloJet80_Jet35_Eta0p7_v1"
      ,"HLT_AK4CaloJet100_Jet35_Eta1p1_v1"
      ,"HLT_AK4CaloJet100_Jet35_Eta0p7_v1"
      ,"HLT_AK4CaloJet80_45_45_Eta2p1_v1"
      ,"HLT_HISinglePhoton10_Eta1p5_v1"
      ,"HLT_HISinglePhoton15_Eta1p5_v1"
      ,"HLT_HISinglePhoton20_Eta1p5_v1"
      ,"HLT_HISinglePhoton30_Eta1p5_v1"
      ,"HLT_HISinglePhoton40_Eta1p5_v1"
      ,"HLT_HISinglePhoton50_Eta1p5_v1"
      ,"HLT_HISinglePhoton60_Eta1p5_v1"
      ,"HLT_HISinglePhoton10_Eta3p1_v1"
      ,"HLT_HISinglePhoton15_Eta3p1_v1"
      ,"HLT_HISinglePhoton20_Eta3p1_v1"
      ,"HLT_HISinglePhoton30_Eta3p1_v1"
      ,"HLT_HISinglePhoton40_Eta3p1_v1"
      ,"HLT_HISinglePhoton50_Eta3p1_v1"
      ,"HLT_HISinglePhoton60_Eta3p1_v1"
      ,"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1"
      ,"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v1"
      ,"HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v1"
      ,"HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v1"
      ,"HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v1"
      ,"HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v1"
      ,"HLT_HIL1DoubleMu0_v1"
      ,"HLT_HIL1DoubleMu10_v1"
      ,"HLT_HIL2DoubleMu0_NHitQ_v1"
      ,"HLT_HIL3DoubleMu0_OS_m2p5to4p5_v1"
      ,"HLT_HIL3DoubleMu0_OS_m7to14_v1"
      ,"HLT_HIL2Mu3_NHitQ10_v1"
      ,"HLT_HIL3Mu3_NHitQ15_v1"
      ,"HLT_HIL2Mu5_NHitQ10_v1"
      ,"HLT_HIL3Mu5_NHitQ15_v1"
      ,"HLT_HIL2Mu7_NHitQ10_v1"
      ,"HLT_HIL3Mu7_NHitQ15_v1"
      ,"HLT_HIL2Mu15_v1"
      ,"HLT_HIL3Mu15_v1"
      ,"HLT_HIL2Mu20_v1"
      ,"HLT_HIL3Mu20_v1"
      ,"HLT_FullTrack18ForPPRef_v1"
      ,"HLT_FullTrack18ForPPRef_v2"
      ,"HLT_FullTrack18ForPPRef_v3"
      ,"HLT_FullTrack24ForPPRef_v1"
      ,"HLT_FullTrack24ForPPRef_v2"
      ,"HLT_FullTrack24ForPPRef_v3"
      ,"HLT_FullTrack34ForPPRef_v1"
      ,"HLT_FullTrack34ForPPRef_v2"
      ,"HLT_FullTrack34ForPPRef_v3"
      ,"HLT_FullTrack34ForPPRef_v4"
      ,"HLT_FullTrack45ForPPRef_v1"
      ,"HLT_FullTrack45ForPPRef_v2"
      ,"HLT_FullTrack45ForPPRef_v3"
      ,"HLT_FullTrack53ForPPRef_v1"
      ,"HLT_FullTrack53ForPPRef_v2"
      ,"HLT_FullTrack53ForPPRef_v3"
      ,"HLT_HIUPCL1DoubleMuOpenNotHF2_v1"
      ,"HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1"
      ,"HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_AND_v1"
      ,"HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1NotMinimumBiasHF2_AND_v1"
      ,"HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1ZdcOR_BptxAND_v1"
      ,"HLT_HIUPCZdcOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1ZdcXOR_BptxAND_v1"
      ,"HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIUPCL1NotZdcOR_BptxAND_v1"
      ,"HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrack_v1"
      ,"HLT_HIL1CastorMediumJet_v1"
      ,"HLT_HICastorMediumJetPixel_SingleTrack_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt8_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt15_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt20_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt30_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt40_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt50_v1"
      ,"HLT_DmesonPPTrackingGlobal_Dpt60_v1"
      ,"HLT_L1MinimumBiasHF1OR_part0_v1"
      ,"HLT_L1MinimumBiasHF1OR_part1_v1"
      ,"HLT_L1MinimumBiasHF1OR_part2_v1"
      ,"HLT_L1MinimumBiasHF1OR_part3_v1"
      ,"HLT_L1MinimumBiasHF1OR_part4_v1"
      ,"HLT_L1MinimumBiasHF1OR_part5_v1"
      ,"HLT_L1MinimumBiasHF1OR_part6_v1"
      ,"HLT_L1MinimumBiasHF1OR_part7_v1"
      ,"HLT_L1MinimumBiasHF1OR_part8_v1"
      ,"HLT_L1MinimumBiasHF1OR_part9_v1"
      ,"HLT_L1MinimumBiasHF1OR_part10_v1"
      ,"HLT_L1MinimumBiasHF1OR_part11_v1"
      ,"HLT_L1MinimumBiasHF1OR_part12_v1"
      ,"HLT_L1MinimumBiasHF1OR_part13_v1"
      ,"HLT_L1MinimumBiasHF1OR_part14_v1"
      ,"HLT_L1MinimumBiasHF1OR_part15_v1"
      ,"HLT_L1MinimumBiasHF1OR_part16_v1"
      ,"HLT_L1MinimumBiasHF1OR_part17_v1"
      ,"HLT_L1MinimumBiasHF1OR_part18_v1"
      ,"HLT_L1MinimumBiasHF1OR_part19_v1"
      ,"HLT_AK4PFBJetBCSV60_Eta2p1_v1"
      ,"HLT_AK4PFBJetBCSV80_Eta2p1_v1"
      ,"HLT_AK4PFDJet60_Eta2p1_v1"
      ,"HLT_AK4PFDJet80_Eta2p1_v1"
      ,"HLT_AK4PFBJetBSSV60_Eta2p1_v1"
      ,"HLT_AK4PFBJetBSSV80_Eta2p1_v1"
      ,"L1_Centrality_ext70_100_HFplusANDminusTH0"
      ,"L1_TOTEM_2"
      ])

