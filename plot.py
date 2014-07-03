from ROOT import *
from numpy import array,zeros
gROOT.SetBatch()
gStyle.SetOptStat(0)
g0acceplist=[]
g225acceplist=[]
g225maskacceplist=[]
g0errlist=[]
g225errlist=[]
g225maskerrlist=[]
g0=TGraphErrors()
g225=TGraphErrors()
g225mask=TGraphErrors()
for ps in range(32):
	if (ps==31):
		f = open('PLTBeamspotInfo_Phi0R0TELMASK.txt')
		for line in f:
			l = line.split()
			accep = float(l[-1])
			tot = float(l[-2])
			err = sqrt( accep*(1.-accep)/tot )
			print accep, tot, err
			g225maskacceplist.insert(0,accep)
			g225maskerrlist.insert(0,err)
		break
	phi = 0
	radius = ps
	fappend = ""
	if (ps > 20):
		phi = 225
		radius -= 20
		fappend = "TELMASK"
	elif (ps > 10):
		phi = 225
		radius -= 10
	filestring = "PLTBeamspotInfo_Phi%iR%i%s.txt"%(phi,radius,fappend)
	if (phi==225 and radius==0):
		filestring = "PLTBeamspotInfo_Phi0R0.txt"
	f = open(filestring)
	#only one line, but whatever
	for line in f:
		l = line.split()
		r = int(l[1])
		accep = float(l[-1])
		tot = float(l[-2])
		err = sqrt( accep*(1.-accep)/tot )
		print accep, tot, err
		if (ps > 20):
			g225maskacceplist.append(accep)
			g225maskerrlist.append(err)
		elif (ps > 10):
			g225acceplist.append(accep)
			g225errlist.append(err)
		else:
			g0acceplist.append(accep)
			g0errlist.append(err)
	f.close()
g225acceplist.insert(0,g0acceplist[0])
g225errlist.insert(0,g0errlist[0])
c = TCanvas()
for i in range(11):
	# g0.SetPoint(i,i,g0acceplist[i]/g0acceplist[0])
	# g225.SetPoint(i,i,g225acceplist[i]/g225acceplist[0])
	# g225mask.SetPoint(i,i,g225maskacceplist[i]/g225maskacceplist[0])
	g0.SetPoint(i,i,g0acceplist[i])
	g0.SetPointError(i,0,g0errlist[i])
	g225.SetPoint(i,i,g225acceplist[i])
	g225.SetPointError(i,0,g225errlist[i])
	g225mask.SetPoint(i,i,g225maskacceplist[i])
	g225mask.SetPointError(i,0,g225maskerrlist[i])

# g0 = TGraph(11,array(range(11)),array(g0acceplist))
# g225 = TGraph(11,array(range(11)),array(g225acceplist))
# g225mask = TGraph(11,array(range(11)),array(g225maskacceplist))
labels=("phi0","phi225","phi225telmask")
counter=-1
for g in (g0,g225,g225mask):
	counter += 1
	c.Clear()
	g.GetXaxis().SetTitle("r (mm)")
	g.GetYaxis().SetTitle("acceptance")
	g.GetYaxis().SetTitleOffset(1.4)
	g.SetLineWidth(2)
	g.SetLineColor(kGreen+2)
	g.Draw()
	c.SaveAs("AcceptanceVsR_"+ labels[counter] +".png")