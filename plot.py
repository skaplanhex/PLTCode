from ROOT import *
gROOT.SetBatch()
gStyle.SetOptStat(0)
f = TFile("PixelNoPUPlots.root","READ")
hist = f.Get("demo/havgpixelhitcount")
c = TCanvas()
hist.Draw("colz")
c.SaveAs("pixelavg.png")