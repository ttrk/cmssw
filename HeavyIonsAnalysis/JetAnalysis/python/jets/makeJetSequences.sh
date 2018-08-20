#!/bin/sh

for system in PbPb pp
do
    for sample in data jec mc mb
    do
	if [ $system == "pp" ] && [ $sample == "mb" ]; then
	    continue
	fi	
        for algo in ak
        do
            for sub in Vs Pu Cs CsSoftDrop CsFilter NONE
            do
                for radius in 1 2 3 4 5 6
                do
                    for object in PF Calo
                    do
                        subt=$sub
                        if [ $sub == "NONE" ]; then
                            subt=""
                        fi
			if [ $sample == "mb" ]; then
                            matchGenjets="HiCleanedGenJets"
			else
			    matchGenjets="HiSignalGenJets"
			fi
			genjets="HiGenJets"
                        ismc="False"
                        corrlabel="_offline"
                        domatch="True"
                        tracks="hiGeneralTracks"
			vertex="offlinePrimaryVertices"
                        pflow="particleFlowTmp"
                        domatch="False"
			doTower="True"
			doSubJets="False"
                        match=""
                        eventinfotag="generator"
			jetcorrectionlevels="\'L2Relative\',\'L3Absolute\'"
                        echo "" > $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py

                        if [ $system == "pp" ]; then
                            #corrlabel="_generalTracks"
                            tracks="generalTracks"
			    vertex="offlinePrimaryVertices"
                            genparticles="genParticles"
                            pflow="particleFlow"
			    doTower="False"
			    if [ $sample == "data" ] && [ $sub == "NONE" ] && [ $radius == 4 ] && [ $object == "PF" ]; then
				jetcorrectionlevels="\'L2Relative\',\'L3Absolute\',\'L2L3Residual\'"
			    fi
                        fi

                        if [ $sample == "mc" ] || [ $sample == "jec" ] || [ $sample == "mb" ]; then
                            ismc="True"
                        fi

                        if [ $system == "pp" ]; then
                            genjets="GenJets"
                            matchGenjets="GenJets"
                        fi

			if [ $sub == "Pu" ]; then
                            corrname=`echo ${algo} | sed 's/\(.*\)/\U\1/'`${radius}${object}${corrlabel}
#			    corrname=`echo ${algo} | sed 's/\(.*\)/\U\1/'`${sub}${radius}${object}${corrlabel}
			else 
			    corrname=`echo ${algo} | sed 's/\(.*\)/\U\1/'`${radius}${object}${corrlabel}
			fi

			if [ $sub == "CsSoftDrop" ] || [ $sub == "CsFilter" ]; then
			    doSubJets="True"
			fi
			
                        cat templateSequence_bTag_cff.py.txt \
                            | sed "s/ALGO_/$algo/g" \
                            | sed "s/SUB_/$subt/g" \
                            | sed "s/RADIUS_/$radius/g" \
                            | sed "s/OBJECT_/$object/g" \
                            | sed "s/SAMPLE_/$sample/g" \
                            | sed "s/CORRNAME_/$corrname/g" \
                            | sed "s/MATCHED_/$match/g" \
                            | sed "s/ISMC/$ismc/g" \
                            | sed "s/MATCHGENJETS/$matchGenjets/g" \
                            | sed "s/GENJETS/$genjets/g" \
                            | sed "s/GENPARTICLES/$genparticles/g" \
                            | sed "s/TRACKS/$tracks/g" \
                            | sed "s/VERTEX/$vertex/g" \
                            | sed "s/PARTICLEFLOW/$pflow/g" \
                            | sed "s/DOMATCH/$domatch/g" \
                            | sed "s/EVENTINFOTAG/$eventinfotag/g" \
			    | sed "s/JETCORRECTIONLEVELS/$jetcorrectionlevels/g" \
			    | sed "s/DOTOWERS_/$doTower/g" \
			    | sed "s/DOSUBJETS_/$doSubJets/g" \
				  >> $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py

			# skip no sub
			if [ $sample == "jec" ]; then
                            echo "${algo}${subt}${radius}${object}JetAnalyzer.genPtMin = cms.untracked.double(1)" >> $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py
			    echo "${algo}${subt}${radius}${object}JetAnalyzer.jetPtMin = cms.double(1)" >> $algo$subt$radius${object}JetSequence_${system}_${sample}_cff.py
                        fi
                    done
                done
            done
        done
    done
done
