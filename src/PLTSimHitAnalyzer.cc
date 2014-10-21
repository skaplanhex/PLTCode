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

#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/LocalVector.h"

#include "SimDataFormats/Track/interface/SimTrack.h"

#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "DataFormats/VertexReco/interface/Vertex.h"


#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "TH2D.h"
#include "TRandom2.h"
#include "TTree.h"

#include <math.h>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#include <tuple>
#include <cstdlib>
#include <fstream>
//for split()
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>

using namespace edm;
using namespace std;


// declare PLTHit class to make integrating the binary conversion code easier
// also helps simplify having to deal with PSimHit class (weird linking errors not worth debugging) 
class PLTHit {
public:
    PLTHit(int channel, int roc, int column, int row, int adc, int event)
        :channel(channel),roc(roc),column(column),row(row),adc(adc),event(event){};
    PLTHit(float pabs, float tof, float eloss, int pdgid, unsigned int detid, float theta, float phi)
    :thePabs(pabs),theTof(tof),theEnergyLoss(eloss),theParticleType(pdgid),theDetUnitId(detid),theThetaAtEntry(theta),thePhiAtEntry(phi){};
    ~PLTHit(){};
    int Channel(){ return channel; }
    int ROC(){ return roc; }
    int Column(){ return column; }
    int Row(){ return row; }
    int ADC(){ return adc; }
    int Event(){ return event; }
    unsigned int detUnitId(){ return theDetUnitId; }
    float energyLoss(){ return theEnergyLoss; }
    float pabs(){ return thePabs; }
    LocalVector momentumAtEntry(){ return LocalVector(theThetaAtEntry,thePhiAtEntry,thePabs); }
private:
    int channel;
    int roc;
    int column;
    int row;
    int adc;
    int event;
    float thePabs;          // momentum
    float theTof;           // Time Of Flight 
    float theEnergyLoss;    // Energy loss
    int   theParticleType;
    unsigned int theDetUnitId;
    float theThetaAtEntry;
    float thePhiAtEntry;

};
// keep for use in beamspot study if ever needed, but I may change the class later
class PLTSimHit {
public:
    PLTSimHit(int channel, int roc, int column, int row, int adc, double pt, double eta)
        :channel(channel),roc(roc),column(column),row(row),adc(adc),pt(pt),eta(eta){};
    ~PLTSimHit(){};
    int Channel(){ return channel; }
    int ROC(){ return roc; }
    int Column(){ return column; }
    int Row(){ return row; }
    int ADC(){ return adc; }
    double Pt(){ return pt; }
    double Eta(){ return eta; }
private:
    int channel;
    int roc;
    int column;
    int row;
    int adc;
    double pt;
    double eta;

};

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
    virtual std::vector<int> analyzeDetId(int);
    virtual int getChannel(int,int,int);
    virtual int getChannelFromHit(PLTHit);
    virtual int getROC(PLTHit);
    virtual bool aboveThreshold(const PSimHit&);
    virtual int getPUEventNumber(int, int);
    virtual std::tuple<int,int> countThreeFoldCoincidences(const map< int,vector<PLTHit> >&);
    //virtual int countThreeFoldCoincidencesInCylinder(const map< int,vector<PLTHit> >&,double,double);
    virtual std::tuple<double,double> PixelGlobalXY(int,int);
    virtual std::tuple<bool,double,double> isFromIP(PLTHit);
    virtual bool maskROC2Pixel(int,int);
    virtual bool maskTelescope(int);
    virtual std::vector<PLTSimHit*> initializeHitVector(int,int,int,int,int,double,double);
    virtual void makeBinary();
    
    // ----------member data ---------------------------
    edm::InputTag simHitLabel;
    edm::Service<TFileService> fs;
    TH1D* hSimHitTheta;
    TH1D* hGenTheta;
    TH1D* heta;
    TH1D* htof;
    TH1D* heloss;
    TH1D* helossPlane;
    TH1D* htel3fold;
    TH1D* hdetid;
    TH1D* hparticlephi;
    TH1D* hparticleeta;
    TH1D* hhitmomentum;
    TH2D* havgpixelhitcount;
    TH1D* hRocNum;
    TH1D* simVertexMult;
    TH1D* hPhiHits;
    TH1D* hEtaHits;
    TH1D* hHitPt;
    TH1D* h3foldPt;
    TH1D* hrMin;
    TH1D* hrMax;
    
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

    // TH2D* rMin_zMin;
    // TH2D* rMin_zMin_lowP;
    // TH2D* rMin_zMin_highP;
    
    std::map< std::string,TH2D* > histMap;
    std::ofstream hitInfo;
    std::ofstream beamspotInfo; //holds acceptance vs. r for each phi scenario

    double cylinderdZ;
    double cylinderR;
    bool confineToIP;
    std::tuple<double,double,double> beamSpotPoint;

    std::ofstream trackInfo;
    bool inDigiMode;
    bool doPileup;
    bool doBeamspotStudy;
    bool phiAtZero;
    bool runFourTelescopes;
    bool wantBinaryOutput;
    int r;
    std::string digiFileName;
    int threshold;
    long eventCounter;
    std::map<int,int> eventsWithThreeFoldCoin;
    std::map< int,std::ofstream* > puMap; //key = #PU events, value = digifile ofstream* for that #PU events
    std::map< int,std::string > puFilenameMap;
    std::map< int,int > threeFoldMap; // key = #PU events, value = # of 3 fold coincidences for that PU scenario. Will always be used with nPU=0 (main events only, i.e. doPileup=false)
    std::map< int,int > threeFoldFromIPMap; // key = #PU events, value = # of 3 fold coincidences for that PU scenario matched to IP. Will always be used with nPU=0 (main events only, i.e. doPileup=false)
    std::vector<int> puScenarios;
    typedef std::map<int,std::ofstream*>::iterator puIter;
    
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
    trackInfo.open("trackInfo.txt");
    simHitLabel = iConfig.getParameter<edm::InputTag>("PLTHits");
    inDigiMode = iConfig.exists("digiFileName") && iConfig.exists("threshold");
    if ( (!iConfig.exists("digiFileName") && iConfig.exists("threshold")) || (iConfig.exists("digiFileName") && !iConfig.exists("threshold")) )
        throw cms::Exception("DigiIssue") << "Digi mode not set up properly. Make sure BOTH digiFileName AND threshold are both set!\n";
    doPileup = (iConfig.exists("doPileup") ? iConfig.getParameter<bool>("doPileup") : false);
    if ( doPileup && (!inDigiMode) ){ //for the case that neither digiFileName nor threshold are set, but doPileup is set to true
        throw cms::Exception("PileupIssue") << "Digi mode not set up properly. Make sure BOTH digiFileName AND threshold are both set!\n";
    }
    if (inDigiMode){
        digiFileName = iConfig.getParameter<std::string>("digiFileName");
        threshold = iConfig.getParameter<int>("threshold");
        wantBinaryOutput = (iConfig.exists("wantBinaryOutput") ? iConfig.getParameter<bool>("wantBinaryOutput") : false);
    }
    else{ //set to some dummy values to not have issues later
        digiFileName = "";
        threshold = 0;
        wantBinaryOutput = false;
    }
    doBeamspotStudy = (iConfig.exists("doBeamspotStudy") ? iConfig.getParameter<bool>("doBeamspotStudy") : false);
    phiAtZero = (iConfig.exists("phiAtZero") ? iConfig.getParameter<bool>("phiAtZero") : true);
    runFourTelescopes = (iConfig.exists("runFourTelescopes") ? iConfig.getParameter<bool>("runFourTelescopes") : false);
    r = (iConfig.exists("r") ? iConfig.getParameter<int>("r") : 0);
    if( (doBeamspotStudy) && ( !iConfig.exists("r") || !iConfig.exists("phiAtZero") )  ) //if both r and phiAtZero are not passed if doing beamspot study
        throw cms::Exception("BeamSpotIssue") << "BeamSpot mode not set up properly. Make sure BOTH phiAtZero AND r are both set!\n";

    //print options to screen
    std::cout << "PLTSimHitAnalyzer run with the following options:\n" << std::endl;
    std::cout << "inDigiMode = " << inDigiMode << std::endl;
    std::cout << "wantBinaryOutput = " << wantBinaryOutput << std::endl;
    std::cout << "doPileup = " << doPileup << std::endl;
    std::cout << "doBeamspotStudy = " << doBeamspotStudy << std::endl;

    //digiFileName is a base string for naming of the output files.  Amend it for the various files needed.
    if (inDigiMode){
        hitInfo.open(digiFileName+".txt");
    }
    //open in append mode 
    if (doBeamspotStudy){
        stringstream ss;
        int phi = 0;
        if (!phiAtZero) phi = 225;
        std::string telmask="";
        if (runFourTelescopes) telmask="TELMASK";
        ss << "PLTBeamspotInfo_Phi" << phi << "R" << r << telmask << ".txt";
        std::string temp = ss.str();
        beamspotInfo.open( temp.c_str() );
        ss.str("");
    }
    // hitInfo_ThreeFold.open(digiFileName+"_threefold.txt");
    eventCounter = 0;
    eventsWithThreeFoldCoin[0] = 0;

    cylinderR = (iConfig.exists("cylinderR") ? iConfig.getParameter<double>("cylinderR") : -1. );
    cylinderdZ = (iConfig.exists("cylinderdZ") ? iConfig.getParameter<double>("cylinderdZ") : -1. );
    confineToIP = (cylinderR != -1.) && (cylinderdZ != -1.);
    if (((cylinderR == -1.) && (cylinderdZ != -1.)) || ((cylinderR != -1.) && (cylinderdZ == -1.))){
        throw cms::Exception("IPConfineIssue") << "Need to set both cylinder R and dZ explicitly!";
    }
    beamSpotPoint = std::make_tuple(0.,0.,0.);

    //pileup stuff
    if (doPileup){
        //just in this one place, define all the pileup scenarios under study
        puScenarios.push_back(1);
        puScenarios.push_back(2);
        puScenarios.push_back(3);
        puScenarios.push_back(5);
        puScenarios.push_back(10);
        puScenarios.push_back(15);
        puScenarios.push_back(20);
        // puScenarios.push_back(25);
        puScenarios.push_back(30);
        // puScenarios.push_back(35);
        puScenarios.push_back(40);

        for(unsigned int i=0; i<puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            stringstream ss;
            ss << "puTextFiles/"+digiFileName+"_PU" << nPU << ".txt";
            puFilenameMap[nPU] = ss.str();
            puMap[nPU] = new std::ofstream(puFilenameMap[nPU]);
        }
    }
    
}


PLTSimHitAnalyzer::~PLTSimHitAnalyzer()
{
    
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    if (inDigiMode && !wantBinaryOutput) hitInfo.close(); //if the binary is made, this is already closed in the makeBinary() function
    if (doBeamspotStudy) beamspotInfo.close();
    trackInfo.close();
    
}


//
// member functions
//
std::vector<int> PLTSimHitAnalyzer::analyzeDetId(int detid){
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
    std::vector<int> infoVector;
    infoVector.push_back(pltNo);
    infoVector.push_back(halfCarriageNo);
    infoVector.push_back(telNo);
    infoVector.push_back(planeNo);
    infoVector.push_back(rowNo);
    infoVector.push_back(columnNo);
    return infoVector;
}

int PLTSimHitAnalyzer::getROC(PLTHit hit){
    int detid = hit.detUnitId();
    std::vector<int> infoVector = analyzeDetId(detid);
    return infoVector.at(3);
}

int PLTSimHitAnalyzer::getChannel(int pltNum, int halfCarriageNum, int telNum){
    int channelNum = -1;
    if(pltNum == 0){
        if(halfCarriageNum == 0){
            switch(telNum){
                case 0:
                    channelNum = 1;
                    break;
                case 1:
                    channelNum = 2;
                    break;
                case 2:
                    channelNum = 3;
                    break;
                case 3:
                    channelNum = 4;
                    break;
            }
        }
        else{
            switch(telNum){
                case 0:
                    channelNum = 5;
                    break;
                case 1:
                    channelNum = 6;
                    break;
                case 2:
                    channelNum = 7;
                    break;
                case 3:
                    channelNum = 8;
                    break;
            }
        }
    }
    else{
        if(halfCarriageNum == 0){
            switch(telNum){
                case 0:
                    channelNum = 9;
                    break;
                case 1:
                    channelNum = 10;
                    break;
                case 2:
                    channelNum = 11;
                    break;
                case 3:
                    channelNum = 12;
                    break;
            }
        }
        else{
            switch(telNum){
                case 0:
                    channelNum = 13;
                    break;
                case 1:
                    channelNum = 14;
                    break;
                case 2:
                    channelNum = 15;
                    break;
                case 3:
                    channelNum = 16;
                    break;
            }
        }
    }
    return channelNum;
}
int PLTSimHitAnalyzer::getChannelFromHit(PLTHit hit){
    int detid = hit.detUnitId();
    vector<int> infoVector = analyzeDetId(detid);
    if (infoVector.size() != 6) cout << "Issue with detid!!!" << endl;
    return getChannel( infoVector.at(0),infoVector.at(1),infoVector.at(2) );
}
//every event number will be either a "signal" MinBias event or a "pileup" MinBias event -- figure out which signal event each event number corresponds to
int PLTSimHitAnalyzer::getPUEventNumber(int actualEventNum, int numPileupEvents){ 
    double ratio = (1.0*actualEventNum)/(1.0*(numPileupEvents+1));
    int event = static_cast<int>(ratio+1.);
    if ( ratio == 1.0*(event-1.) )
        event--;
    return event;
}
//set up to mask pixels in ROC2 to get a 6x6mm active area in the center of the sensor
bool PLTSimHitAnalyzer::maskROC2Pixel(int row, int col){
    if( ((0<=row) && (row <=9)) || ((70<=row) && (row<=79)) )
        return true;
    else if( ((0<=col) && (col<=6)) || ((45<=col) && (col<=51)) )
        return true;
    else
        return false;
}
bool PLTSimHitAnalyzer::aboveThreshold(const PSimHit& hit){

    double numberOfElectrons = ( (hit.energyLoss()*(1e9))/3.6 ); //convert to eV then to electrons
    if (numberOfElectrons > threshold) return true;
    else return false;
}
bool PLTSimHitAnalyzer::maskTelescope(int tel){
    if ( (tel == 1) || (tel == 3) )
        return true;
    else
        return false;
}
std::vector<PLTSimHit*> PLTSimHitAnalyzer::initializeHitVector(int channel, int roc, int column, int row, int adc, double pt, double eta){
    std::vector<PLTSimHit*> hitVector;
    hitVector.push_back( new PLTSimHit(channel,roc,column,row,adc,pt,eta) );
    return hitVector;

}
tuple<int,int> PLTSimHitAnalyzer::countThreeFoldCoincidences(const map< int,vector<PLTHit> >& hitTracker){

    int threeFoldCount = 0;
    int threeFoldFromIPCount = 0;
    for (std::map< int , std::vector<PLTHit> >::const_iterator iTel = hitTracker.begin(); iTel != hitTracker.end(); ++iTel) {
        std::vector<PLTHit> telHits = iTel->second;
        std::vector<double> hitPts(3,-1.); //initializes with length=3 and entries each=-1.
        if (telHits.size()<3) {
            continue;
        }
        else{
            bool containsZero = false;
            bool containsOne = false;
            bool containsTwo = false;
            std::vector<PLTHit> roc0Hits;
            for (unsigned int i = 0; i < telHits.size(); i++) {
                //int pNo = telHits.at(i)->ROC(); //plane number of hit in given telescope
                int pNo = getROC( telHits.at(i) );
                //double thisHitPt = telHits.at(i)->Pt();
                if (pNo == 0) {
                    roc0Hits.push_back( telHits.at(i) );
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
                if(confineToIP){ //if pileup study is run, count 3 fold coincidences consistent with originating from the IP
                    for (unsigned int i = 0; i < roc0Hits.size(); i++){
                        bool fromIP;
                        double rMin,zMin;
                        std::tie(fromIP,rMin,zMin) = isFromIP( roc0Hits.at(i) );
                        if ( fromIP ){
                            threeFoldFromIPCount++;
                            // rMin_zMin->Fill(rMin,zMin);
                            float hitP = roc0Hits.at(i).pabs();
                            trackInfo << rMin << " " << zMin << " " << hitP << "\n";
                            // if (hitP < 1.) rMin_zMin_lowP->Fill(rMin,zMin);
                            // else rMin_zMin_highP->Fill(rMin,zMin);
                            break;
                        }
                    }
                }//end if confineToIP
            }
        } //end else statement (telescopes with at least three hits)
    }//end loop over telescopes

    //if confineToIP = false, we don't care about the second number, but if true, we care about both.  Just return them both in each case.
    return make_tuple(threeFoldCount,threeFoldFromIPCount);
}
std::tuple<double,double> PLTSimHitAnalyzer::PixelGlobalXY(int row, int column){
    // FOR ROC0 ONLY!!!

    // some geometry measurments needed (all length measurments are in mm unless I say otherwise)
    const double PIXELHEIGHT = 0.1;
    const double PIXELWIDTH = 0.15;
    const double ROW0_R = 52.6;
    const double COLUMN0_X = -3.825;

    double rowR = ROW0_R - row*PIXELHEIGHT; //minus sign because row 79 is lowest in y
    double columnX = COLUMN0_X + column*PIXELWIDTH; // columns go up in x

    return std::make_tuple(columnX,rowR);

}
//returns isFromIP, rMin, and zMin together to cut down on computation time
std::tuple<bool,double,double> PLTSimHitAnalyzer::isFromIP(PLTHit hit){

    // Get pixel address, this will set x0,y0,z0 for a linear fit. Extrapolate line using momentum vector

    // beamspot info
    double bsX,bsY,bsZ;
    std::tie(bsX,bsY,bsZ) = beamSpotPoint;

    int detid = hit.detUnitId();
    LocalVector direction = hit.momentumAtEntry().unit();
    // multiply each component by -1 to flip the vector
    double slopeX = (-5.e-3)*direction.x();
    double slopeY = (-5.e-3)*direction.y();
    double slopeZ = (-5.e-3)*direction.z();

    // cout << "slopes: " << slopeX << " " << slopeY << " " << slopeZ << endl;

    std::vector<int> infoVector = analyzeDetId(detid);
    if (infoVector.size() != 6) throw cms::Exception("DetID Issue") << "There's an issue with the hit detid!!\n"; 
    // int pltNo = infoVector.at(0);
    // int halfCarriageNo = infoVector.at(1);
    // int telNo = infoVector.at(2);
    // int planeNo = infoVector.at(3);
    int rowNo = infoVector.at(4);
    int columnNo = infoVector.at(5);

    // global xyz coordinates of the hit
    double hitX,hitY,hitZ;
    std::tie(hitX,hitY) = PixelGlobalXY(rowNo,columnNo);
    hitZ = 1726.75; // front face of ROC0, same for all hits
    // cout << "hit location: " << hitX << " " << hitY << " " << hitZ << endl;

    // make line as a parametric function in 3D
    int nSteps = 1000000;
    double rMin = 1e9;
    double rMax = -1;
    double zMin = 1e9;
    bool fromIP = false;
    for(int iStep = 1; iStep < nSteps; iStep++){

        //get x,y,z of this step, check if it's in the cylinder
        double x = hitX + slopeX*iStep;
        double y = hitY + slopeY*iStep;
        double z = hitZ + slopeZ*iStep;

        double rFromBS = sqrt( (x-bsX)*(x-bsX) + (y-bsY)*(y-bsY) );
        double zFromBS = fabs(z-bsZ);

        if (rFromBS < rMin && zFromBS < cylinderdZ/2.) rMin = rFromBS;
        if (rFromBS > rMax && zFromBS < cylinderdZ/2.) rMax = rFromBS;
        if (zFromBS < zMin && zFromBS < cylinderdZ/2.) zMin = zFromBS;

        //if (iStep % 50000 == 0 || iStep == 1 || fabs(z)<cylinderdZ/2.) cout << "point on track: " << iStep << " " << x << " " << y << " " << z << endl;

        // if the coordinates are in the cylinder
        if ( rFromBS<cylinderR && zFromBS < cylinderdZ/2. ) fromIP = true;
    }
    hrMin->Fill(rMin);
    hrMax->Fill(rMax);
    return make_tuple(fromIP,rMin,zMin);

}
// ------------ method called for each event  ------------
void PLTSimHitAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    eventCounter++;

    edm::Handle<PSimHitContainer> simHitHandle;
    iEvent.getByLabel(simHitLabel,simHitHandle);
    
    edm::Handle< std::vector< reco::GenParticle > > particleHandle;
    iEvent.getByLabel("genParticles",particleHandle);

    // edm::Handle< std::vector< SimTrack > > simTrackHandle;
    // bool simTracksPresent = iEvent.getByLabel("g4SimHits",simTrackHandle);

    // //do SimTracks stuff here:
    // if(simTracksPresent){
    //     for(std::vector<SimTrack>::const_iterator iTrack = simTrackHandle->begin(); iTrack != simTrackHandle->end(); ++iTrack){
    //         const math::XYZTLorentzVectorD trackP4 = iTrack->trackerSurfaceMomentum();
    //         double trackPx = trackP4.px();
    //         double trackPy = trackP4.py();
    //         double trackPt = sqrt(trackPx*trackPx + trackPy*trackPy);
    //     }
    // }

    // edm::Handle< std::vector< reco::Vertex > > vertexHandle;
    // iEvent.getByLabel("offlinePrimaryVertices",vertexHandle);

    // //make vertex multiplicity plot
    // simVertexMult->Fill(vertexHandle->size());

    //keeps track of hit locations to easily count 3-fold coincidences
    std::map< int,std::vector<PLTHit> > hitTracker; //hits from main event
    
    //keeps track of eloss in each ROC
    std::map< int,double > energyTracker; 
    for (int i=0; i!=3; i++)
        energyTracker[i] = 0.;

    //loop over genParticles

    for (std::vector<reco::GenParticle>::const_iterator iParticle = particleHandle->begin(); iParticle != particleHandle->end(); ++iParticle) {
        double particleEta = iParticle->eta();
        double particleTheta = iParticle->theta();
        hparticleeta->Fill(particleEta);
        hGenTheta->Fill(particleTheta);
        if ( 4.1<fabs(particleEta) && fabs(particleEta) < 4.4 ) {
            hparticlephi->Fill( iParticle->phi() );
        }
    }
    for (PSimHitContainer::const_iterator iHit = simHitHandle->begin(); iHit != simHitHandle->end(); ++iHit) {
        PSimHit hit = *(&(*iHit));
        if ( !aboveThreshold(hit) ) continue;
        //std::cout << "HIT!!!" << std::endl;
        double mom = iHit->pabs();
        int detid = iHit->detUnitId();
        //cout << "hit detid: " << detid << endl;
        hdetid->Fill(detid);

        //analyze detid to get position of hit in the PLT
        std::vector<int> infoVector = analyzeDetId(detid);
        if (infoVector.size() != 6) throw cms::Exception("DetID Issue") << "There's an issue with the hit detid!!\n"; 
        int pltNo = infoVector.at(0);
        int halfCarriageNo = infoVector.at(1);
        int telNo = infoVector.at(2);
        int planeNo = infoVector.at(3);
        int rowNo = infoVector.at(4);
        int columnNo = infoVector.at(5);


        //Fill single ROC histograms
        std::stringstream ss;
        std::string ipSide;
        std::string carriageSide;
        std::string tel;
        std::string roc;

        //debug string
        std::string hitDebug;
        ss << "pltNo="<<pltNo << " halfCarriageNo=" << halfCarriageNo << " telNo=" << telNo << "planeNo=" << planeNo << " rowNo=" << rowNo << " columnNo=" << columnNo << "\n";
        hitDebug = ss.str();
        ss.str("");
        
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
        if ( histMap.count(histString) == 0 ){
            continue; //forget weird hits
            //throw cms::Exception("PixelHistogramIssue") << hitDebug << "\n";
        }
        else if ( histMap.count(histString) > 0 ){
            histMap[histString]->Fill(columnNo,rowNo);
            //fill histograms for each roc
            havgpixelhitcount->Fill(columnNo,rowNo);
            hRocNum->Fill(planeNo);
        }
        // three digit address giving side of IP, half carriage, and telescope
        // int planeLoc = 100*pltNo + 10*halfCarriageNo + telNo;

        hhitmomentum->Fill(mom);
        double theta = iHit->thetaAtEntry();
        double eta = -log(tan(theta/2.));
        double coshEta = cosh(eta);
        double hitPt = mom/coshEta;
        hHitPt->Fill(hitPt);
        hSimHitTheta->Fill(theta);
        heta->Fill(eta);
        htof->Fill(iHit->timeOfFlight());
        heloss->Fill(1000000*iHit->energyLoss()); //plot in keV

        //if( planeNo < 0 || planeNo > 2 ) throw cms::Exception("PlaneNumberIssue") << "Plane number not 0,1,2. " << hitDebug; 
        energyTracker.at(planeNo) += iHit->energyLoss();
        //        std::cout << " " << std::endl;
        //        std::cout << "PDGID: " << iHit->particleType() << std::endl;
        //        std::cout << "Energy Loss: " << iHit->energyLoss() << std::endl;
        //        std::cout << "DetID: " << iHit->detUnitId() << std::endl;
        //        std::cout << " " << std::endl;
        int channelNum = getChannel(pltNo,halfCarriageNo,telNo);
        double numberOfElectrons = ( (iHit->energyLoss()*(1e9))/3.6 ); //convert to eV then to electrons

        //to get adc, use GainCal coefficient of 1.538462e-2 and round to nearest int
        const double GAINCAL = 1.538462e-2;
        int adc = round( numberOfElectrons*GAINCAL );

        if ( (numberOfElectrons > threshold) && inDigiMode ){
            //fill the normal digi output
            hitInfo << channelNum << " " << planeNo << " " << columnNo << " " << rowNo << " " << adc << " " << eventCounter << "\n";

            //fill the pileup output if desired
            if(doPileup){
                //for each pileup scenario
                for(puIter it = puMap.begin(); it != puMap.end(); ++it){
                    int numPU = it->first;
                    ( *(it->second) ) << channelNum << " " << planeNo << " " << columnNo << " " << rowNo << " " << adc << " " << getPUEventNumber(eventCounter,numPU) << "\n";
                }
            }
        }
        //separate conditions by beamspot study or no

        //only count ROC2 hits for 3-fold coincidence if they pass the pixel mask
        // if ( doBeamspotStudy && (!runFourTelescopes) ) {
        //     if (hitTracker.count(planeLoc) == 0) {
        //         if (planeNo != 2)
        //             hitTracker[planeLoc] = initializeHitVector(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta);
        //         else if ( (planeNo == 2) && !maskROC2Pixel(rowNo,columnNo) )
        //             hitTracker[planeLoc] = initializeHitVector(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta);
        //     }
        //     // if there has been a hit, add the plane number of this hit to the others
        //     else{
        //         if (planeNo != 2)
        //             hitTracker[planeLoc].push_back(new PLTSimHit(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta));
        //         else if ( (planeNo == 2) && !maskROC2Pixel(rowNo,columnNo) )
        //             hitTracker[planeLoc].push_back(new PLTSimHit(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta));
        //     }
        // }
        // else if ( doBeamspotStudy && runFourTelescopes && (!maskTelescope(telNo)) ){
        //     if (hitTracker.count(planeLoc) == 0) {
        //         if (planeNo != 2)
        //             hitTracker[planeLoc] = initializeHitVector(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta);
        //         else if ( (planeNo == 2) && !maskROC2Pixel(rowNo,columnNo) )
        //             hitTracker[planeLoc] = initializeHitVector(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta);
        //     }
        //     // if there has been a hit, add the plane number of this hit to the others
        //     else{
        //         if (planeNo != 2)
        //             hitTracker[planeLoc].push_back(new PLTSimHit(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta));
        //         else if ( (planeNo == 2) && !maskROC2Pixel(rowNo,columnNo) )
        //             hitTracker[planeLoc].push_back(new PLTSimHit(channelNum,planeNo,columnNo,rowNo,adc,hitPt,eta));
        //     }
        // }
        // else{
            // if there hasn't been a hit in that telescope yet
        PLTHit newHit(hit.pabs(),hit.timeOfFlight(),hit.energyLoss(),hit.particleType(),hit.detUnitId(),hit.thetaAtEntry(),hit.phiAtEntry());
        if (hitTracker.count(channelNum) == 0) {
            std::vector<PLTHit> vec;
            vec.push_back(newHit);
            hitTracker[channelNum] = vec;
            //std::cout << "Telescope Added" << std::endl;
        }
        // if there has been a hit, add the plane number of this hit to the others
        else{
            hitTracker[channelNum].push_back(newHit);
            //std::cout << "Hit added to telescope" << std::endl;
        }
        // }
    }//end loop over PLT hits

    for(int i = 0; i != 3; i++){
        double planeEnergy = 1000000.*energyTracker.at(i); //GeV -> keV
        if (planeEnergy > 0.)
            helossPlane->Fill( planeEnergy );
    }

    //add in hits from pileup
    map<int,TTree*> puTreeMap;
    map<int,map< int,vector<PLTHit> >> puHitTracker; //hits from main event + hits from PU in all PU scenarios (keys)
    if (doPileup){
        TFile puInFile("pileuptrees.root"); 

        for (unsigned int i = 0; i<puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            // NOTE: GET THE TREE CORRESPONDING TO THAT PU SCENARIO!
            // PUT ALL TREES IN ROOT FILE FIRST!!!! DO IT IN A WAY THAT'S EASY FOR THE LOOP TO DETERMINE WHICH TO USE AUTOMATICALLY
            TString treeName = TString::Format("tree_PU%i",nPU);
            TTree* tree = (TTree*)( puInFile.Get(treeName) );
            puTreeMap[nPU] = tree;
        }

        // random number generator, 0 sets the seed randomly
        TRandom2 tr(0);

        // loop over PU scenarios and build puHitTracker
        for(unsigned int i =0; i < puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            // cout << "nPU: " << nPU << endl;
            //initialize hitTracker for each nPU with the hitTracker from the real event
            puHitTracker[nPU] = hitTracker;
            //add hits to the hittracker from pileup
            TTree* tree = puTreeMap[nPU];
            int treeNEvents = tree->GetEntries();

            int nHits;
            vector<float>* pabs = 0;
            vector<float>* energyLoss = 0;
            vector<float>* thetaAtEntry = 0;
            vector<float>* phiAtEntry = 0;
            vector<float>* tof = 0;
            vector<int>* particleType = 0;
            vector<int>* detUnitId = 0;
            vector<int>* trackId = 0;

            tree->SetBranchAddress("nHits",&nHits);
            tree->SetBranchAddress("pabs",&pabs);
            tree->SetBranchAddress("energyLoss",&energyLoss);
            tree->SetBranchAddress("thetaAtEntry",&thetaAtEntry);
            tree->SetBranchAddress("phiAtEntry",&phiAtEntry);
            tree->SetBranchAddress("tof",&tof);
            tree->SetBranchAddress("particleType",&particleType);
            tree->SetBranchAddress("detUnitId",&detUnitId);
            tree->SetBranchAddress("trackId",&trackId);

            for(int j=0; j<nPU; j++){

                int entryNum = tr.Integer(treeNEvents); //random integer in [0,treeNEvents-1]
                tree->GetEntry(entryNum);
                // cout << "got entry " << entryNum << endl;
                // if there are no hits in this PU event, move on to the next one
                if (nHits == 0) continue;
                else{
                    // loop over all the hits in the PU event, create PSimHit, find out what channel it belongs to, then add it to the puHitTracker for that channel
                    for (int iHit=0; iHit < nHits; iHit++){
                        PLTHit puHit(pabs->at(iHit),tof->at(iHit),energyLoss->at(iHit),particleType->at(iHit),detUnitId->at(iHit),thetaAtEntry->at(iHit),phiAtEntry->at(iHit));
                        int puChannel = getChannelFromHit(puHit);
                        if (puHitTracker[nPU].count(puChannel) == 0){
                            vector<PLTHit> newVec;
                            newVec.push_back(puHit);
                            puHitTracker[nPU][puChannel] = newVec;
                        }
                        else{
                            puHitTracker[nPU][puChannel].push_back(puHit);
                        }
                    } //end loop over hits in a PUevent
                } //end block on nPUHits>0
            } //end loop for each PU scenario
        } //end loop over the PU scenarios

        // now analyze the puHitTracker to see if there are any 3 fold coincidences:

    } //end doPileup block

    int threeFoldCount;
    int threeFoldFromIPCount;
    std::tie(threeFoldCount,threeFoldFromIPCount) = countThreeFoldCoincidences(hitTracker);
    threeFoldMap[0] += threeFoldCount;
    threeFoldFromIPMap[0] += threeFoldFromIPCount;
    if (threeFoldCount > 0) eventsWithThreeFoldCoin[0]++;
    if(doPileup){
        for (unsigned int i = 0; i<puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            int puThreeFoldCount;
            int puThreeFoldFromIPCount;
            std::tie(puThreeFoldCount,puThreeFoldFromIPCount) = countThreeFoldCoincidences(puHitTracker[nPU]);
            threeFoldMap[nPU] += puThreeFoldCount;
            threeFoldFromIPMap[nPU] += puThreeFoldFromIPCount;
            //cout << nPU << " " << puThreeFoldCount << endl;
        }
    }
      
} //end analyze method


// ------------ method called once each job just before starting event loop  ------------
void PLTSimHitAnalyzer::beginJob()
{
    hSimHitTheta = fs->make<TH1D>("hSimHitTheta","SimHit Theta", 300,0,3.1416);
    hGenTheta = fs->make<TH1D>("hGenTheta","GenParticle Theta", 300,0,3.1416);
    heta = fs->make<TH1D>("heta","Particle Eta",1000,-5,5);
    htof = fs->make<TH1D>("htof","Time of Flight from IP (ns)",100,0,25);
    heloss = fs->make<TH1D>("heloss","Energy Loss",500,0,500);
    helossPlane = fs->make<TH1D>("helossPlane","Energy Loss",500,0,500);
    htel3fold = fs->make<TH1D>("htel3fold","Three-Fold Coincidences By Telescope",114,-0.5,113);
    hdetid = fs->make<TH1D>("hdetid","Det ID of PSimHits",11330000,-0.5,11329999);
    hparticleeta = fs->make<TH1D>("hparticleeta","Eta of genParticles",200,-6,6);
    hparticlephi = fs->make<TH1D>("hparticlephi","Phi of genParticles within eta=(4.1,4.4)",100,0,3.1416);
    hhitmomentum = fs->make<TH1D>("hhitmomentum","SimHit |p| At Entry",1000,0,1000);
    havgpixelhitcount = fs->make<TH2D>("havgpixelhitcount","Normalized Pixel Hit Count For All ROCs",52,-0.5,51.5,80,-0.5,79.5);
    hRocNum = fs->make<TH1D>("hRocNum","ROC Number Of PSimHit",3,-0.5,2.5);
    simVertexMult = fs->make<TH1D>("simVertexMult","SimVertex Multiplicity",101,-0.5,100.5);
    hPhiHits = fs->make<TH1D>("hPhiHits","Events with At Least One Hit vs. Phi",1000,1.8,2.1);
    hEtaHits = fs->make<TH1D>("hEtaHits","Events with At Least One Hit vs. Eta",1000,3.9,4.6);
    hHitPt = fs->make<TH1D>("hHitPt","pT of PLT PSimHits",500,0,50);
    h3foldPt = fs->make<TH1D>("h3foldPt","pT of 3-fold coincidence track",500,0,50);
    hrMin = fs->make<TH1D>("hrMin","rMin",400,0,200);
    hrMax = fs->make<TH1D>("hrMax","rMax",400,0,200);
    // rMin_zMin = fs->make<TH2D>("rMin_zMin","rMin_zMin",100,0,100,1000,0,100);
    // rMin_zMin_lowP = fs->make<TH2D>("rMin_zMin_lowP","rMin_zMin_lowP",1000000,0,1000000,1000,0,100);
    // rMin_zMin_highP = fs->make<TH2D>("rMin_zMin_highP","rMin_zMin_highP",1000000,0,1000000,1000,0,100);
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
//The vast majority of the translation to binary code was written by Dean Hidas
void PLTSimHitAnalyzer::makeBinary()
{
    std::cout << "" << std::endl;
    std::cout << "*****************************************************" << std::endl;
    std::cout << "*                                                   *" << std::endl;
    std::cout << "*   Now producing a binary of the hit information   *" << std::endl;
    std::cout << "*            This should be fairly quick            *" << std::endl;
    std::cout << "*                                                   *" << std::endl;
    std::cout << "*****************************************************" << std::endl;
    hitInfo.close();

    std::string InFileName = digiFileName+".txt";
    std::ifstream InFile(InFileName.c_str());
    if (!InFile.is_open()) {
        std::cerr << "ERROR: cannot open input file: " << InFileName << std::endl;
        throw;
    }

    std::string OutFileName = digiFileName+"_BINARY.dat";
    std::ofstream fout(OutFileName.c_str(), std::ios::binary);
    if (!fout.is_open()) {
        std::cerr << "ERROR: cannot open output file" << std::endl;
        throw;
    }

    uint32_t n, n2;

    int Channel, ROC, Column, Row, ADC, EventNumber;
    int LastEventNumber = -1;
    bool IsFirstEvent = true;
    std::vector<PLTHit> Hits;

    for ( ; InFile >> Channel >> ROC >> Column >> Row >> ADC >> EventNumber; ) {
        if (IsFirstEvent) {
            LastEventNumber = EventNumber;
            IsFirstEvent = false;
        }
        if (EventNumber != LastEventNumber) {

            // Delete all hits and clear vector
            n2 = (5 << 8);
            n =  0x50000000;
            n |= LastEventNumber;
            fout.write( (char*) &n2, sizeof(uint32_t) );
            fout.write( (char*) &n, sizeof(uint32_t) );


            for (size_t ihit = 0; ihit != Hits.size(); ++ihit) {
                n = 0x00000000;
                PLTHit* Hit = &Hits[ihit];
                //printf("Channel ROC Row Col ADC: %2i %1i %2i %2i %4i %12i\n", Hit->Channel(), Hit->ROC(), Hit->Row(), Hit->Column(), Hit->ADC(), ievent);
                //fprintf(ff, "%2i %1i %2i %2i %4i %i\n", Hit->Channel(), Hit->ROC(), Hit->Column(), Hit->Row(), Hit->ADC(), EventNumber);
                // printf("%2i %1i %2i %2i %4i %i\n", Hit->Channel(), Hit->ROC(), Hit->Column(), Hit->Row(), Hit->ADC(), EventNumber);

                n |= (Hit->Channel() << 26);
                n |= ( (Hit->ROC() + 1) << 21);

                if (Hit->Column() % 2 == 0) {
                  n |= ( ((80 - Hit->Row()) * 2) << 8 );
                } else {
                  // checked, correct
                  n |= ( ((80 - Hit->Row()) * 2 + 1) << 8 );
                }

                if (Hit->Column() % 2 == 0) {
                  n |= ( ((Hit->Column()) / 2) << 16  );
                } else {
                  n |= (( (Hit->Column() - 1) / 2) << 16  );
                }
                n |= Hit->ADC();


                //if (Hit->ROC() == 2) {
                //  printf("WORD: %X\n", (n &  0x3e00000));
                //}

                fout.write( (char*) &n, sizeof(uint32_t) );
            }

            if (Hits.size() % 2 == 0) {
                // even number of hits.. need to fill out the word.. just print the number over two as 2x32  words
                n  = 0xa0000000;
                n2 = 0x00000000;
                n  |= (Hits.size() / 2 + 2);
                fout.write( (char*) &n2, sizeof(uint32_t) );
                fout.write( (char*) &n, sizeof(uint32_t) );
            } else {
                // Print number of hits in 1x32 bit
                n  = 0x00000000;
                fout.write( (char*) &n, sizeof(uint32_t) );
                fout.write( (char*) &n, sizeof(uint32_t) );
                n  = 0xa0000000;
                n  |= (Hits.size() / 2 + 1);
                fout.write( (char*) &n, sizeof(uint32_t) );
            }

            LastEventNumber = EventNumber;
            Hits.clear();
        }

        Hits.push_back( PLTHit(Channel, ROC, Column, Row, ADC, EventNumber) );

    }



    // Delete all hits and clear vector
    n2 = (5 << 8);
    n =  0x50000000;
    n |= LastEventNumber;
    fout.write( (char*) &n2, sizeof(uint32_t) );
    fout.write( (char*) &n, sizeof(uint32_t) );


      for (size_t ihit = 0; ihit != Hits.size(); ++ihit) {
        n = 0x00000000;
        PLTHit* Hit = &Hits[ihit];
        //printf("Channel ROC Row Col ADC: %2i %1i %2i %2i %4i %12i\n", Hit->Channel(), Hit->ROC(), Hit->Row(), Hit->Column(), Hit->ADC(), ievent);
        //fprintf(ff, "%2i %1i %2i %2i %4i %i\n", Hit->Channel(), Hit->ROC(), Hit->Column(), Hit->Row(), Hit->ADC(), EventNumber);
        // printf("%2i %1i %2i %2i %4i %i\n", Hit->Channel(), Hit->ROC(), Hit->Column(), Hit->Row(), Hit->ADC(), EventNumber);

        n |= (Hit->Channel() << 26);
        n |= ( (Hit->ROC() + 1) << 21);

        if (Hit->Column() % 2 == 0) {
          n |= ( ((80 - Hit->Row()) * 2) << 8 );
        } else {
          // checked, correct
          n |= ( ((80 - Hit->Row()) * 2 + 1) << 8 );
        }

        if (Hit->Column() % 2 == 0) {
          n |= ( ((Hit->Column()) / 2) << 16  );
        } else {
          n |= (( (Hit->Column() - 1) / 2) << 16  );
        }
        n |= Hit->ADC();


        //if (Hit->ROC() == 2) {
        //  printf("WORD: %X\n", (n &  0x3e00000));
        //}

        fout.write( (char*) &n, sizeof(uint32_t) );
      }

      if (Hits.size() % 2 == 0) {
        // even number of hits.. need to fill out the word.. just print the number over two as 2x32  words
        n  = 0xa0000000;
        n2 = 0x00000000;
        n  |= (Hits.size() / 2 + 2);
        fout.write( (char*) &n2, sizeof(uint32_t) );
        fout.write( (char*) &n, sizeof(uint32_t) );
      } else {
        // Print number of hits in 1x32 bit
        n  = 0x00000000;
        fout.write( (char*) &n, sizeof(uint32_t) );
        fout.write( (char*) &n, sizeof(uint32_t) );
        n  = 0xa0000000;
        n  |= (Hits.size() / 2 + 1);
        fout.write( (char*) &n, sizeof(uint32_t) );
      }

    fout.close();

}

// ------------ method called once each job just after ending the event loop  ------------
void PLTSimHitAnalyzer::endJob() 
{
    double entries = havgpixelhitcount->GetEntries();
    havgpixelhitcount->Scale(1./entries);

    double acceptance = 1.0*eventsWithThreeFoldCoin[0]/eventCounter;
    cout << "(numEvents,numEventsWithThreefoldCoin,acceptance) = " << "(" << eventCounter << "," << eventsWithThreeFoldCoin[0] << "," << acceptance << ")" << endl;
    //count the acceptances as fn of nPU
    if (doPileup){
        //close the pileup file ofstreams
        for(puIter it = puMap.begin(); it != puMap.end(); ++it){
            it->second->close();
        }
        cout << "no IP matching" << endl;
        cout << " " << endl;
        cout << 1 << " " << threeFoldMap[0] << endl;
        for (unsigned int i = 0; i < puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            cout << nPU+1 << " " << threeFoldMap[nPU] << endl;
        }
        cout << " " << endl;
        cout << "IP matching" << endl;
        cout << 1 << " " << threeFoldFromIPMap[0] << endl;
        for (unsigned int i = 0; i < puScenarios.size(); i++){
            int nPU = puScenarios.at(i);
            cout << nPU+1 << " " << threeFoldFromIPMap[nPU] << endl;
        }

        // loop over pu 3 fold counts and write out a text file with the acceptance info
        // std::ofstream puOut;
        // puOut.open("./puTextFiles/"+digiFileName+"_PUAccepInfo.txt");
        // for(std::map<int,int>::const_iterator it = puThreeFoldMap.begin(); it!=puThreeFoldMap.end(); ++it){
        //     int nPU = it->first;
        //     int n3Fold = it->second;
        //     cout << nPU << " " << n3Fold << " " << getPUEventNumber(eventCounter,nPU) << endl;
        //     puOut << nPU << " " << n3Fold << " " << getPUEventNumber(eventCounter,nPU) << "\n";
        // }
        // puOut.close();
    }

    if (doBeamspotStudy){
        std::cout << "************BeamSpot Study Results**********" << std::endl;
        std::cout << "Number of events with 3-fold coincidences: " << eventsWithThreeFoldCoin[0] << std::endl;
        std::cout << "Number of total events: " << eventCounter << std::endl;
        std::cout << "---> acceptance = " << acceptance << std::endl;
        std::cout << "This information is now being recorded in the text file." << std::endl;
        beamspotInfo << phiAtZero << " " << r << " " <<  eventsWithThreeFoldCoin[0] << " " <<  eventCounter << " " << acceptance <<  "\n";
    }
    if (wantBinaryOutput) makeBinary();
    //std::cout << "Number of 3-fold coincidences: " << threeFoldCount << std::endl;
}

// ------------ method called when starting to processes a run  ------------
void PLTSimHitAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void PLTSimHitAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void PLTSimHitAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void PLTSimHitAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PLTSimHitAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PLTSimHitAnalyzer);
