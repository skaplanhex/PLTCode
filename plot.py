from ROOT import *
from numpy import array,zeros
gROOT.SetBatch()
gStyle.SetOptStat(0)
f = open("PLTBeamspotInfo.txt")

rList = []
accepList = []
errors = []
g = TGraphErrors()
for line in f:
	l = line.split()
	r = int(l[1])
	accep = float(l[-1])
	tot = int(l[-2])
	err = sqrt( accep*(1.-accep) )/tot
	rList.append(r)
	accepList.append(accep)
	errors.append(err)
	g.SetPoint(r,r,accep)
	g.SetPointError(r,0.,err)
#g = TGraphErrors(array(rList), array(accepList),zeros(len(rList)), array(errors) )

c = TCanvas()
g.GetXaxis().SetTitle("r (mm)")
g.GetYaxis().SetTitle("acceptance")
g.GetYaxis().SetTitleOffset(1.4)
g.SetLineWidth(2)
g.SetLineColor(kGreen+2)
g.Draw()
c.SaveAs("AcceptanceVsR_Phi0.png")