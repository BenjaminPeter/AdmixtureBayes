import sys
from admixturebayes.runMCMC import main as _runMCMC
from admixturebayes.analyzeSamples import run_posterior_main
from admixturebayes.makePlots import main as _makePlots

def runMCMC():
    _runMCMC(sys.argv[1:])

def analyzeSamples():
    run_posterior_main(sys.argv[1:])

def makePlots():
    _makePlots(sys.argv[1:])


