import os
from os.path import join, getsize
from pathlib import Path, PosixPath

print('\nHello. Thinking through quickly what to test and how to test it.')
print('The idea, as stated, is that we build out a system based on testing.')
print('This is a bit too focused on mechanics, but it gets the point across.')
print()
print('-- walks STDDIR seeking proper input')
print('-- unit test suite, built quickly, modestly provisioned')
print('-- extensible with basic refactoring. Mostly just a quick hack')
print()
print('Happy to go for functionality, doctrings, whatever. You sent no')
print('   instruction for now. This seems sane though, in terms of')
print('   what it is that I do without any particular direction.')
print()
print('-- `find STD` yields the following demo filesystem')
print('   ( comparing foo, foo.gz, etc, which are filtered later )\n')

import subprocess
subprocess.run(["find", "STD"])

print()

def mock_walk_std():
    
    here = os.getcwd()
    STDDIR      = PosixPath(here, 'STD/')
    p = Path(STDDIR)

    filelist = list(p.glob('**/*.gz'))
    statinfolist = [[file, Path.stat(file)] for file in filelist]
    return statinfolist

def describe_designation_list():

    print()
    print('-- by tossing our expectations into a data structure, we can')
    print('   ensure that they are met, and, watch for end user changes\n')

    designation_list = {

    'CSF_GM_WM'     : r'T1WunwarpedTissueMasks.nii.gz'                              ,
    'CSF'           : r'T1Wunwarped_CSF.nii.gz'                                     ,
    'GM'            : r'T1Wunwarped_GM.nii.gz'                                      ,
    'WM'            : r'T1Wunwarped_WM.nii.gz'                                      ,
    'controls'      : r'whatToGetExcavatedFromcontrolDatabaseToT1Wunwarped.sqlite'  ,
    'T1W'           : r'T1Wunwarped.nii.gz'                                         ,
    'HiResDTI'      : r'HiResDTIRegToT1.nii.gz'                                     ,
    'HiRsMD'        : r'HiResDTIRegToT1_MD.nii.gz'                                  ,
    'HiResFA'       : r'HiResDTIRegToT1_FA.nii.gz'                  

    # , 'baz' : r'baz'
    }

    return designation_list

# run via test, per README

