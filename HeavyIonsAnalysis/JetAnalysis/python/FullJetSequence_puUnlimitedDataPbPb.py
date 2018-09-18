import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_HI_cff import *
from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets
from RecoHI.HiJetAlgos.hiFJRhoProducer import hiFJRhoProducer
from RecoHI.HiJetAlgos.hiFJGridEmptyAreaCalculator_cff import hiFJGridEmptyAreaCalculator
kt4PFJets.src = cms.InputTag('particleFlowTmp')
kt4PFJets.doAreaFastjet = True
kt4PFJets.jetPtMin      = cms.double(0.0)
kt4PFJets.GhostArea     = cms.double(0.005)

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_data_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_data_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akCs3PFJetSequence_PbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_PbPb_data_cff import *

highPurityTracks = cms.EDFilter("TrackSelector",
                                src = cms.InputTag("hiGeneralTracks"),
                                cut = cms.string('quality("highPurity")'))

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
offlinePrimaryVertices.TrackLabel = 'highPurityTracks'


akPu4PFJetsNoLimits = akPu4PFJets.clone(
    minimumTowersFraction = cms.double(0.)
)

akPu3PFJets.minimumTowersFraction = cms.double(0.)
akPu4PFJets.minimumTowersFraction = cms.double(0.)
akPu5PFJets.minimumTowersFraction = cms.double(0.)

akPu3CaloJets.minimumTowersFraction = cms.double(0.)
akPu4CaloJets.minimumTowersFraction = cms.double(0.)
akPu5CaloJets.minimumTowersFraction = cms.double(0.)


jetSequences = cms.Sequence(
    PFTowers + 
    kt4PFJets +
    hiFJRhoProducer +
    hiFJGridEmptyAreaCalculator + 
    akPu4PFJetsNoLimits +
    #akPu2CaloJets +
    #akPu2PFJets +
    #akCs2PFJets +
    akPu3CaloJets +
    akPu3PFJets +
    akCs3PFJets +
    akPu4CaloJets +
    akPu4PFJets +
    akCs4PFJets +
    #akCsSoftDrop4PFJets +
    #akCsSoftDrop5PFJets +

    highPurityTracks +
    offlinePrimaryVertices +

    #akPu2CaloJetSequence +
    #akPu2PFJetSequence +
    #akCs2PFJetSequence +

    akPu3CaloJetSequence +
    akPu3PFJetSequence +
    akCs3PFJetSequence +

    akPu4CaloJetSequence +
    akPu4PFJetSequence +
    akCs4PFJetSequence #+
    #akCsSoftDrop4PFJetSequence #+
    #akCsSoftDrop5PFJetSequence
)
