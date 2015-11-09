import FWCore.ParameterSet.Config as cms

# Calo geometry service model
#
# removed by tommaso
#
#ECAL conditions
#  include "CalibCalorimetry/EcalTrivialCondModules/data/EcalTrivialCondRetriever.cfi"
#
#TPG condition needed by ecalRecHit producer if TT recovery is ON
from RecoLocalCalo.EcalRecProducers.ecalRecHitTPGConditions_cff import *
#ECAL reconstruction
from RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalPreshowerRecHit_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalCompactTrigPrim_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalTPSkim_cfi import *
ecalLocalRecoSequence = cms.Sequence(ecalGlobalUncalibRecHit*ecalDetIdToBeRecovered*ecalRecHit*ecalCompactTrigPrim*ecalTPSkim+ecalPreshowerRecHit)
ecalLocalRecoSequence_nopreshower = cms.Sequence(ecalGlobalUncalibRecHit*ecalRecHit)
###ecalRecHit.ChannelStatusToBeExcluded = [ 3, 4, 8, 9, 10, 11, 12, 13, 14 ]
### change the parameter types properly after importing from 53X into 75X
ecalRecHit.ChannelStatusToBeExcluded = cms.vstring(   'kNoisy',
                                               'kNNoisy',
                                               'kFixedG6',
                                               'kFixedG1',
                                               'kFixedG0',
                                               'kNonRespondingIsolated',
                                               'kDeadVFE',
                                               'kDeadFE',
                                               'kNoDataNoTP',)
ecalRecHit.flagsMapDBReco = cms.PSet(
        kGood  = cms.vstring('kOk','kDAC','kNoLaser','kNoisy'),
        kNoisy = cms.vstring('kNNoisy','kFixedG6','kFixedG1'),
        kNeighboursRecovered = cms.vstring('kFixedG0',
										   'kNonRespondingIsolated',
										   'kDeadVFE'),
        kTowerRecovered = cms.vstring('kDeadFE'),
        kDead           = cms.vstring('kNoDataNoTP')
        )
###
