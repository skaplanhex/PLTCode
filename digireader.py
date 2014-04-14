from ROOT import *
c = TCanvas()
hist = TH1F("hist","",100,0,50000)
hist.GetXaxis().SetTitle("ADC")
hist.GetYaxis().SetTitle("Number of Hits / 100 ADC")
hist.GetYaxis().SetTitleOffset(1.4)
print "opening the text file..."
digifile = open('test_digioutput.txt','r')
print "...done."
lines = digifile.readlines()
hitCounter = 0
for line in lines:
	hitCounter += 1
	if hitCounter % 1000 == 0:
		print "Investigating Hit #"+str(hitCounter)
	adc = float( line.split()[-1] )
	hist.Fill(adc)
hist.Fit("landau","","",22000,50000)
hist.Draw()
digifile.close()
c.SaveAs("adc.png")