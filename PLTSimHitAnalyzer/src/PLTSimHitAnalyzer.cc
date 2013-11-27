// -*- C++ -*-
//
// Package:    PLTSimHitAnalyzer
// Class:      PLTSimHitAnalyzer
// 
/**\class PLTSimHitAnalyzer PLTSimHitAnalyzer.cc PLTCode/PLTSimHitAnalyzer/src/PLTSimHitAnalyzer.cc
 
 Description: [one line class summary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Steven Kaplan
//         Created:  Tue Aug 20 10:50:10 EDT 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//PSimHitContainer includes PSimHit and Vector already
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "TH2D.h"

#include <math.h>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>

//
// class declaration
//

class PLTSimHitAnalyzer : public edm::EDAnalyzer {
public:
    explicit PLTSimHitAnalyzer(const edm::ParameterSet&);
    ~PLTSimHitAnalyzer();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
    
private:
    virtual void beginJob() ;
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;
    
    virtual void beginRun(edm::Run const&, edm::EventSetup const&);
    virtual void endRun(edm::Run const&, edm::EventSetup const&);
    virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
    virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
    
    // ----------member data ---------------------------
    edm::InputTag simHitLabel;
    edm::Service<TFileService> fs;
    TH1D* htheta;
    TH1D* heta;
    TH1D* htof;
    TH1D* heloss;
    TH1D* htel3fold;
    TH1D* hdetid;
    TH1D* hparticlephi;
    TH1D* hparticleeta;
    TH1D* hhitmomentum;
    TH2D* havgpixelhitcount;
    TH1D* hRocNum;
    
    //pixel maps
    TH2D* PlusZ_PlusX_Tel0_ROC0_PixelMap;
    TH2D* PlusZ_PlusX_Tel0_ROC1_PixelMap;
    TH2D* PlusZ_PlusX_Tel0_ROC2_PixelMap;
    
    TH2D* PlusZ_PlusX_Tel1_ROC0_PixelMap;
    TH2D* PlusZ_PlusX_Tel1_ROC1_PixelMap;
    TH2D* PlusZ_PlusX_Tel1_ROC2_PixelMap;
    
    TH2D* PlusZ_PlusX_Tel2_ROC0_PixelMap;
    TH2D* PlusZ_PlusX_Tel2_ROC1_PixelMap;
    TH2D* PlusZ_PlusX_Tel2_ROC2_PixelMap;
    
    TH2D* PlusZ_PlusX_Tel3_ROC0_PixelMap;
    TH2D* PlusZ_PlusX_Tel3_ROC1_PixelMap;
    TH2D* PlusZ_PlusX_Tel3_ROC2_PixelMap;
    
    TH2D* PlusZ_MinusX_Tel0_ROC0_PixelMap;
    TH2D* PlusZ_MinusX_Tel0_ROC1_PixelMap;
    TH2D* PlusZ_MinusX_Tel0_ROC2_PixelMap;
    
    TH2D* PlusZ_MinusX_Tel1_ROC0_PixelMap;
    TH2D* PlusZ_MinusX_Tel1_ROC1_PixelMap;
    TH2D* PlusZ_MinusX_Tel1_ROC2_PixelMap;
    
    TH2D* PlusZ_MinusX_Tel2_ROC0_PixelMap;
    TH2D* PlusZ_MinusX_Tel2_ROC1_PixelMap;
    TH2D* PlusZ_MinusX_Tel2_ROC2_PixelMap;
    
    TH2D* PlusZ_MinusX_Tel3_ROC0_PixelMap;
    TH2D* PlusZ_MinusX_Tel3_ROC1_PixelMap;
    TH2D* PlusZ_MinusX_Tel3_ROC2_PixelMap;
    
    //minus z
    
    TH2D* MinusZ_PlusX_Tel0_ROC0_PixelMap;
    TH2D* MinusZ_PlusX_Tel0_ROC1_PixelMap;
    TH2D* MinusZ_PlusX_Tel0_ROC2_PixelMap;
    
    TH2D* MinusZ_PlusX_Tel1_ROC0_PixelMap;
    TH2D* MinusZ_PlusX_Tel1_ROC1_PixelMap;
    TH2D* MinusZ_PlusX_Tel1_ROC2_PixelMap;
    
    TH2D* MinusZ_PlusX_Tel2_ROC0_PixelMap;
    TH2D* MinusZ_PlusX_Tel2_ROC1_PixelMap;
    TH2D* MinusZ_PlusX_Tel2_ROC2_PixelMap;
    
    TH2D* MinusZ_PlusX_Tel3_ROC0_PixelMap;
    TH2D* MinusZ_PlusX_Tel3_ROC1_PixelMap;
    TH2D* MinusZ_PlusX_Tel3_ROC2_PixelMap;
    
    TH2D* MinusZ_MinusX_Tel0_ROC0_PixelMap;
    TH2D* MinusZ_MinusX_Tel0_ROC1_PixelMap;
    TH2D* MinusZ_MinusX_Tel0_ROC2_PixelMap;
    
    TH2D* MinusZ_MinusX_Tel1_ROC0_PixelMap;
    TH2D* MinusZ_MinusX_Tel1_ROC1_PixelMap;
    TH2D* MinusZ_MinusX_Tel1_ROC2_PixelMap;
    
    TH2D* MinusZ_MinusX_Tel2_ROC0_PixelMap;
    TH2D* MinusZ_MinusX_Tel2_ROC1_PixelMap;
    TH2D* MinusZ_MinusX_Tel2_ROC2_PixelMap;
    
    TH2D* MinusZ_MinusX_Tel3_ROC0_PixelMap;
    TH2D* MinusZ_MinusX_Tel3_ROC1_PixelMap;
    TH2D* MinusZ_MinusX_Tel3_ROC2_PixelMap;
    
    std::map< std::string,TH2D* > histMap;
    int threeFoldCount;
    
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PLTSimHitAnalyzer::PLTSimHitAnalyzer(const edm::ParameterSet& iConfig)

{
    //now do what ever initialization is needed
    simHitLabel = iConfig.getParameter<edm::InputTag>("PLTHits");
    threeFoldCount = 0;
    
}


PLTSimHitAnalyzer::~PLTSimHitAnalyzer()
{
    
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    
}


//
// member functions
//

// ------------ method called for each event  ------------
void
PLTSimHitAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace std;
    
    Handle<PSimHitContainer> simHitHandle;
    iEvent.getByLabel(simHitLabel,simHitHandle);
    
    Handle< std::vector< reco::GenParticle > > particleHandle;
    iEvent.getByLabel("genParticles",particleHandle);
    
    //keeps track of hit locations to easily count 3-fold coincidences
    std::map< int,std::vector<int> > hitTracker;
    for (std::vector<reco::GenParticle>::const_iterator iParticle = particleHandle->begin(); iParticle != particleHandle->end(); ++iParticle) {
        double particleEta = iParticle->eta();
        hparticleeta->Fill(particleEta);
        if ( 4.1<fabs(particleEta) && fabs(particleEta) < 4.4 ) {
            hparticlephi->Fill( iParticle->phi() );
        }
    }
    for (PSimHitContainer::const_iterator iHit = simHitHandle->begin(); iHit != simHitHandle->end(); ++iHit) {
        //std::cout << "HIT!!!" << std::endl;
        double mom = iHit->pabs();
        int detid = iHit->detUnitId();
        hdetid->Fill(detid);
        std::stringstream ss;
        ss << detid;
        std::string detidstring = ss.str();
        int detidsize = detidstring.size();
        //since many identifiers can be zero, the size of the integer can vary! Need to switch on all possible sizes to determine the identifiers from the detid.
        
        //There needs to be a more elegant way to do this...
        int pltNo = -1;
        int halfCarriageNo = -1;
        int telNo = -1;
        int planeNo = -1;
        int rowNo = -1;
        int columnNo = -1;
        
        if (detidsize == 1 || detidsize == 2) {
            pltNo = 0;
            halfCarriageNo = 0;
            telNo = 0;
            planeNo = 0;
            rowNo = 0;
            columnNo = detid;
        }
        else if (detidsize == 3 || detidsize == 4){
            pltNo = 0;
            halfCarriageNo = 0;
            telNo = 0;
            planeNo = 0;
            rowNo = (detid - (detid % 100))/100;
            columnNo = detid % 100;
        }
        else if (detidsize == 5){
            pltNo = 0;
            halfCarriageNo = 0;
            telNo = 0;
            planeNo = (detid - (detid % 10000))/10000;
            rowNo = ((detid % 10000)-(detid % 100))/100;
            columnNo = detid % 100;
        }
        else if (detidsize == 6){
            pltNo = 0;
            halfCarriageNo = 0;
            telNo = (detid - (detid % 100000))/100000;
            planeNo = ((detid - (100000*telNo)) - (detid % 10000))/10000;
            rowNo = ((detid % 10000)-(detid % 100))/100;
            columnNo = detid % 100;
        }
        else if (detidsize == 7){
            pltNo = 0;
            halfCarriageNo = (detid - (detid % 1000000))/1000000;
            telNo = ((detid - (1000000*halfCarriageNo)) - (detid % 100000))/100000;
            planeNo = (detid-(1000000*halfCarriageNo)-(100000*telNo)-(detid % 10000))/10000;
            rowNo = ((detid % 10000)-(detid % 100))/100;
            columnNo = detid % 100;
        }
        else if (detidsize == 8){
            int temp [8];
            //fill array with digits in detid and use the array for the various ids
            for(int i =0; i<8; i++){
                char aChar = detidstring.at(i);
                int anInt = atoi(&aChar); //convert char to int
                temp[i] = anInt;
            }
            pltNo = temp[0];
            halfCarriageNo = temp[1];
            telNo = temp[2];
            planeNo = temp[3];
            rowNo = 10*temp[4]+temp[5];
            columnNo = 10*temp[6]+temp[7];
        }
        else{
            std::cout << "DETID = " << detid << " NOT EXPECTED!! INVESTIGATE!!" << std::endl;
        }
        if (pltNo == -1 || halfCarriageNo == -1 || telNo == -1 || planeNo == -1 || rowNo == -1 || columnNo == -1) {
            std::cout << "ONE OF THE ELEMENTS WEREN'T SET CORRECTLY FOR DETID = " << detid << ". INVESTIGATE!!!" << std::endl;
        }
        havgpixelhitcount->Fill(columnNo,rowNo);
        hRocNum->Fill(planeNo);
        //fill single ROC histograms
        //first figure out which histogram to fill
        std::string ipSide;
        std::string carriageSide;
        std::string tel;
        std::string roc;
        
        if (pltNo == 0) {
            ipSide = "MinusZ";
        }
        else if (pltNo == 1){
            ipSide = "PlusZ";
        }
        
        if (halfCarriageNo == 0) {
            carriageSide = "MinusX";
        }
        else if (halfCarriageNo == 1){
            carriageSide = "PlusX";
        }
        ss.str("");
        ss << telNo;
        tel = std::string("Tel")+ss.str();
        
        ss.str("");
        ss << planeNo;
        roc = std::string("ROC")+ss.str();
        
        std::string histString = ipSide+"_"+carriageSide+"_"+tel+"_"+roc+"_PixelMap";
        //finally, fill the proper histogram
        histMap[histString]->Fill(columnNo,rowNo);
        // three digit address giving side of IP, half carriage, and telescope
        int planeLoc = 100*pltNo + 10*halfCarriageNo + telNo;
        // if there hasn't been a hit in that telescope yet
        if (hitTracker.count(planeLoc) == 0) {
            hitTracker[planeLoc] = std::vector<int>(1,planeNo);
            //std::cout << "Telescope Added" << std::endl;
        }
        // if there has been a hit, add the plane number of this hit to the others
        else{
            hitTracker[planeLoc].push_back(planeNo);
            //std::cout << "Hit added to telescope" << std::endl;
        }
        hhitmomentum->Fill(mom);
        double theta = iHit->thetaAtEntry();
        double eta = -log(tan(theta/2.));
        htheta->Fill(theta);
        heta->Fill(eta);
        htof->Fill(iHit->timeOfFlight());
        heloss->Fill(iHit->energyLoss());
        //        std::cout << " " << std::endl;
        //        std::cout << "PDGID: " << iHit->particleType() << std::endl;
        //        std::cout << "Energy Loss: " << iHit->energyLoss() << std::endl;
        //        std::cout << "DetID: " << iHit->detUnitId() << std::endl;
        //        std::cout << " " << std::endl;
    }
    //loop through the hit tracker to see if there are any 3-fold coincidences
    for (std::map< int , std::vector<int> >::const_iterator iTel = hitTracker.begin(); iTel != hitTracker.end(); ++iTel) {
        std::vector<int> telHits = iTel->second;
        if (telHits.size()<3) {
            continue;
        }
        else{
            bool containsZero = false;
            bool containsOne = false;
            bool containsTwo = false;
            for (unsigned int i = 0; i < telHits.size(); i++) {
                int pNo = telHits[i]; //plane number of hit in given telescope
                if (pNo == 0) {
                    containsZero = true;
                }
                else if (pNo == 1){
                    containsOne = true;
                }
                else if (pNo == 2){
                    containsTwo = true;
                }
            }
            bool existsThreeFoldCoin = containsZero && containsOne && containsTwo; //if >=3 hits distributed among all three planes
            if (existsThreeFoldCoin) {
                htel3fold->Fill(iTel->first);
                threeFoldCount++;
            }
        } //end else statement (telescopes with at least three hits)
    }//end loop over telescopes
}


// ------------ method called once each job just before starting event loop  ------------
void 
PLTSimHitAnalyzer::beginJob()
{
    htheta = fs->make<TH1D>("htheta","Particle Theta", 1000,-4,4);
    heta = fs->make<TH1D>("heta","Particle Eta",1000,-5,5);
    htof = fs->make<TH1D>("htof","Time of Flight from IP (ns)",100,0,25);
    heloss = fs->make<TH1D>("heloss","Energy Loss",100,0,1);
    htel3fold = fs->make<TH1D>("htel3fold","Three-Fold Coincidences By Telescope",114,-0.5,113);
    hdetid = fs->make<TH1D>("hdetid","Det ID of PSimHits",11330000,-0.5,11329999);
    hparticleeta = fs->make<TH1D>("hparticleeta","Eta of genParticles",200,-6,6);
    hparticlephi = fs->make<TH1D>("hparticlephi","Phi of genParticles within eta=(4.1,4.4)",100,0,3.1416);
    hhitmomentum = fs->make<TH1D>("hhitmomentum","SimHit |p| At Entry",1000,0,1000);
    havgpixelhitcount = fs->make<TH2D>("havgpixelhitcount","Normalized Pixel Hit Count For All ROCs",52,-0.5,51.5,80,-0.5,79.5);
    hRocNum = fs->make<TH1D>("hRocNum","ROC Number Of PSimHit",3,-0.5,2.5);
    PlusZ_PlusX_Tel0_ROC0_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel0_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel0_ROC1_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel0_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel0_ROC2_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel0_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel1_ROC0_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel1_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel1_ROC1_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel1_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel1_ROC2_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel1_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel2_ROC0_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel2_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel2_ROC1_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel2_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel2_ROC2_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel2_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel3_ROC0_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel3_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel3_ROC1_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel3_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_PlusX_Tel3_ROC2_PixelMap = fs->make<TH2D>("PlusZ_PlusX_Tel3_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel0_ROC0_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel0_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel0_ROC1_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel0_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel0_ROC2_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel0_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel1_ROC0_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel1_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel1_ROC1_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel1_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel1_ROC2_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel1_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel2_ROC0_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel2_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel2_ROC1_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel2_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel2_ROC2_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel2_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel3_ROC0_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel3_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel3_ROC1_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel3_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    PlusZ_MinusX_Tel3_ROC2_PixelMap = fs->make<TH2D>("PlusZ_MinusX_Tel3_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    
    MinusZ_PlusX_Tel0_ROC0_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel0_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel0_ROC1_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel0_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel0_ROC2_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel0_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel1_ROC0_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel1_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel1_ROC1_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel1_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel1_ROC2_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel1_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel2_ROC0_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel2_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel2_ROC1_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel2_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel2_ROC2_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel2_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel3_ROC0_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel3_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel3_ROC1_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel3_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_PlusX_Tel3_ROC2_PixelMap = fs->make<TH2D>("MinusZ_PlusX_Tel3_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel0_ROC0_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel0_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel0_ROC1_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel0_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel0_ROC2_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel0_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel1_ROC0_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel1_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel1_ROC1_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel1_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel1_ROC2_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel1_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel2_ROC0_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel2_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel2_ROC1_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel2_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel2_ROC2_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel2_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel3_ROC0_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel3_ROC0_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel3_ROC1_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel3_ROC1_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    MinusZ_MinusX_Tel3_ROC2_PixelMap = fs->make<TH2D>("MinusZ_MinusX_Tel3_ROC2_PixelMap","Pixel Hit Multiplicity",52,-0.5,51.5,80,-0.5,79.5);
    
    //build the map to elegantly fill the histogram!
    histMap["PlusZ_PlusX_Tel0_ROC0_PixelMap"] = PlusZ_PlusX_Tel0_ROC0_PixelMap;
    histMap["PlusZ_PlusX_Tel0_ROC1_PixelMap"] = PlusZ_PlusX_Tel0_ROC1_PixelMap;
    histMap["PlusZ_PlusX_Tel0_ROC2_PixelMap"] = PlusZ_PlusX_Tel0_ROC2_PixelMap;
    histMap["PlusZ_PlusX_Tel1_ROC0_PixelMap"] = PlusZ_PlusX_Tel1_ROC0_PixelMap;
    histMap["PlusZ_PlusX_Tel1_ROC1_PixelMap"] = PlusZ_PlusX_Tel1_ROC1_PixelMap;
    histMap["PlusZ_PlusX_Tel1_ROC2_PixelMap"] = PlusZ_PlusX_Tel1_ROC2_PixelMap;
    histMap["PlusZ_PlusX_Tel2_ROC0_PixelMap"] = PlusZ_PlusX_Tel2_ROC0_PixelMap;
    histMap["PlusZ_PlusX_Tel2_ROC1_PixelMap"] = PlusZ_PlusX_Tel2_ROC1_PixelMap;
    histMap["PlusZ_PlusX_Tel2_ROC2_PixelMap"] = PlusZ_PlusX_Tel2_ROC2_PixelMap;
    histMap["PlusZ_PlusX_Tel3_ROC0_PixelMap"] = PlusZ_PlusX_Tel3_ROC0_PixelMap;
    histMap["PlusZ_PlusX_Tel3_ROC1_PixelMap"] = PlusZ_PlusX_Tel3_ROC1_PixelMap;
    histMap["PlusZ_PlusX_Tel3_ROC2_PixelMap"] = PlusZ_PlusX_Tel3_ROC2_PixelMap;
    histMap["PlusZ_MinusX_Tel0_ROC0_PixelMap"] = PlusZ_MinusX_Tel0_ROC0_PixelMap;
    histMap["PlusZ_MinusX_Tel0_ROC1_PixelMap"] = PlusZ_MinusX_Tel0_ROC1_PixelMap;
    histMap["PlusZ_MinusX_Tel0_ROC2_PixelMap"] = PlusZ_MinusX_Tel0_ROC2_PixelMap;
    histMap["PlusZ_MinusX_Tel1_ROC0_PixelMap"] = PlusZ_MinusX_Tel1_ROC0_PixelMap;
    histMap["PlusZ_MinusX_Tel1_ROC1_PixelMap"] = PlusZ_MinusX_Tel1_ROC1_PixelMap;
    histMap["PlusZ_MinusX_Tel1_ROC2_PixelMap"] = PlusZ_MinusX_Tel1_ROC2_PixelMap;
    histMap["PlusZ_MinusX_Tel2_ROC0_PixelMap"] = PlusZ_MinusX_Tel2_ROC0_PixelMap;
    histMap["PlusZ_MinusX_Tel2_ROC1_PixelMap"] = PlusZ_MinusX_Tel2_ROC1_PixelMap;
    histMap["PlusZ_MinusX_Tel2_ROC2_PixelMap"] = PlusZ_MinusX_Tel2_ROC2_PixelMap;
    histMap["PlusZ_MinusX_Tel3_ROC0_PixelMap"] = PlusZ_MinusX_Tel3_ROC0_PixelMap;
    histMap["PlusZ_MinusX_Tel3_ROC1_PixelMap"] = PlusZ_MinusX_Tel3_ROC1_PixelMap;
    histMap["PlusZ_MinusX_Tel3_ROC2_PixelMap"] = PlusZ_MinusX_Tel3_ROC2_PixelMap;
    histMap["MinusZ_PlusX_Tel0_ROC0_PixelMap"] = MinusZ_PlusX_Tel0_ROC0_PixelMap;
    histMap["MinusZ_PlusX_Tel0_ROC1_PixelMap"] = MinusZ_PlusX_Tel0_ROC1_PixelMap;
    histMap["MinusZ_PlusX_Tel0_ROC2_PixelMap"] = MinusZ_PlusX_Tel0_ROC2_PixelMap;
    histMap["MinusZ_PlusX_Tel1_ROC0_PixelMap"] = MinusZ_PlusX_Tel1_ROC0_PixelMap;
    histMap["MinusZ_PlusX_Tel1_ROC1_PixelMap"] = MinusZ_PlusX_Tel1_ROC1_PixelMap;
    histMap["MinusZ_PlusX_Tel1_ROC2_PixelMap"] = MinusZ_PlusX_Tel1_ROC2_PixelMap;
    histMap["MinusZ_PlusX_Tel2_ROC0_PixelMap"] = MinusZ_PlusX_Tel2_ROC0_PixelMap;
    histMap["MinusZ_PlusX_Tel2_ROC1_PixelMap"] = MinusZ_PlusX_Tel2_ROC1_PixelMap;
    histMap["MinusZ_PlusX_Tel2_ROC2_PixelMap"] = MinusZ_PlusX_Tel2_ROC2_PixelMap;
    histMap["MinusZ_PlusX_Tel3_ROC0_PixelMap"] = MinusZ_PlusX_Tel3_ROC0_PixelMap;
    histMap["MinusZ_PlusX_Tel3_ROC1_PixelMap"] = MinusZ_PlusX_Tel3_ROC1_PixelMap;
    histMap["MinusZ_PlusX_Tel3_ROC2_PixelMap"] = MinusZ_PlusX_Tel3_ROC2_PixelMap;
    histMap["MinusZ_MinusX_Tel0_ROC0_PixelMap"] = MinusZ_MinusX_Tel0_ROC0_PixelMap;
    histMap["MinusZ_MinusX_Tel0_ROC1_PixelMap"] = MinusZ_MinusX_Tel0_ROC1_PixelMap;
    histMap["MinusZ_MinusX_Tel0_ROC2_PixelMap"] = MinusZ_MinusX_Tel0_ROC2_PixelMap;
    histMap["MinusZ_MinusX_Tel1_ROC0_PixelMap"] = MinusZ_MinusX_Tel1_ROC0_PixelMap;
    histMap["MinusZ_MinusX_Tel1_ROC1_PixelMap"] = MinusZ_MinusX_Tel1_ROC1_PixelMap;
    histMap["MinusZ_MinusX_Tel1_ROC2_PixelMap"] = MinusZ_MinusX_Tel1_ROC2_PixelMap;
    histMap["MinusZ_MinusX_Tel2_ROC0_PixelMap"] = MinusZ_MinusX_Tel2_ROC0_PixelMap;
    histMap["MinusZ_MinusX_Tel2_ROC1_PixelMap"] = MinusZ_MinusX_Tel2_ROC1_PixelMap;
    histMap["MinusZ_MinusX_Tel2_ROC2_PixelMap"] = MinusZ_MinusX_Tel2_ROC2_PixelMap;
    histMap["MinusZ_MinusX_Tel3_ROC0_PixelMap"] = MinusZ_MinusX_Tel3_ROC0_PixelMap;
    histMap["MinusZ_MinusX_Tel3_ROC1_PixelMap"] = MinusZ_MinusX_Tel3_ROC1_PixelMap;
    histMap["MinusZ_MinusX_Tel3_ROC2_PixelMap"] = MinusZ_MinusX_Tel3_ROC2_PixelMap;
    
    
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PLTSimHitAnalyzer::endJob() 
{
    double entries = havgpixelhitcount->GetEntries();
    havgpixelhitcount->Scale(1./entries);
    std::cout << "Number of 3-fold coincidences: " << threeFoldCount << std::endl;
}

// ------------ method called when starting to processes a run  ------------
void 
PLTSimHitAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PLTSimHitAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PLTSimHitAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PLTSimHitAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PLTSimHitAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PLTSimHitAnalyzer);
