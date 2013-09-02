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
#include "TH2D.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <math.h>
// user defines
#ifndef SKDEBUG
#define SKDEBUG

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
    TH1D *htheta;
    TH1D *heta;
    TH1D *hmom;
    TH1D *htof;
    TH1D *heloss;
    int hitCount;
    
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
    hitCount = 0;
    
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
    
    Handle<PSimHitContainer> simHitHandle;
    iEvent.getByLabel(simHitLabel,simHitHandle);
    
#ifdef SKDEBUG
    for (PSimHitContainer::const_iterator iHit = simHitHandle->begin(); iHit != simHitHandle->end(); ++iHit) {
        double theta = iHit->thetaAtEntry();
        double eta = -log(tan(theta/2.));
        if( iHit->detUnitId() > 199 ){
            theta *= -1;
        }
        if( iHit->detUnitId() > 199 ){
            eta *= -1;
        }
        htheta->Fill(theta);
        heta->Fill(eta);
        hmom->Fill(iHit->pabs());
        htof->Fill(iHit->timeOfFlight());
        heloss->Fill(iHit->energyLoss());
//        std::cout << " " << std::endl;
//        std::cout << "PDGID: " << iHit->particleType() << std::endl;
//        std::cout << "Energy Loss: " << iHit->energyLoss() << std::endl;
//        std::cout << "DetID: " << iHit->detUnitId() << std::endl;
//        std::cout << " " << std::endl;
        hitCount++;
    }
    
    
    
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
PLTSimHitAnalyzer::beginJob()
{
    htheta = fs->make<TH1D>("htheta","Particle Theta", 1000,-4,4);
    heta = fs->make<TH1D>("heta","Particle Eta",1000,-5,5);
    hmom = fs->make<TH1D>("hmom","Particle Momentum",200,0,200);
    htof = fs->make<TH1D>("htof","Time of Flight from IP (ns)",100,0,25);
    heloss = fs->make<TH1D>("heloss","Energy Loss",100,0,1);
    
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PLTSimHitAnalyzer::endJob() 
{
    std::cout << "Hit Count: " << hitCount << std::endl;
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
#endif