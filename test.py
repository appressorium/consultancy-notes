# TODO : test integration

from os import getcwd
from os.path import join, getsize
from pathlib import Path, PosixPath
import unittest
import bill_oleg.mockbuild as omb
import pprint

class mocktesting(unittest.TestCase):

  def test_cwd(self):

    here = Path.cwd()
    self.assertIsNotNone(here)

  def test_reports(self):

    here = Path.cwd() # TBD pass this in

    DICOMDIR    = PosixPath(here, 'DICOM/')
    STDDIR      = PosixPath(here, 'STD/')
    RAWDIR      = PosixPath(here, 'RAW/')
    RESULTDIR   = PosixPath(here, 'RESULT/')
    TESTDIR     = PosixPath(here, 'TEST/')
    TEMPLATEDIR = PosixPath(here, 'TEMPLATE/')
     
    statinfo = Path.stat(PosixPath(RESULTDIR, 'T1Wunwarped_CSF.nii.gz'))
    self.assertIsNotNone(statinfo.st_size)

  def test_reportfiles(self):
    
    here = Path.cwd()
    STDDIR      = PosixPath(here, 'STD/')
    
    print() 
    print('\n-- our imaginary output still doesn\'t make sense,') 
    print('   but it does reflect stat checks against the filesystem') 
    print('-- note that foo.gz clocks in at empty, so we could') 
    print('   raise a flag to the end user, if we wanted.') 
    print('-- note that there is no hardcoding of file names, just') 
    print('   walks in search of file names, and test against constants\n') 

    sil = omb.mock_walk_std()

    try:
        for info in sil:
            print(info[0], info[1].st_size)

    except FileNotFoundError as fnferr:
        print(fnferr)
    except Error as generr:
        print(generr)
        raise

  """
    strategy: describe constants, test outcomes

    pass them in, from the program
    this makes the program more verbose,
        but it makes it easy to spot worflow changes from the end user via test 
    
    alternately, we could scan checksums against some property file. might work
   
  """
  def test_create_designation_list(self):

    omb_dl = omb.describe_designation_list()
    self.assertEqual(omb_dl, {

    'CSF_GM_WM'     : r'T1WunwarpedTissueMasks.nii.gz'                              ,
    'CSF'           : r'T1Wunwarped_CSF.nii.gz'                                     ,
    'GM'            : r'T1Wunwarped_GM.nii.gz'                                      ,
    'WM'            : r'T1Wunwarped_WM.nii.gz'                                      ,
    'controls'      : r'whatToGetExcavatedFromcontrolDatabaseToT1Wunwarped.sqlite'  ,
    'T1W'           : r'T1Wunwarped.nii.gz'                                         ,
    'HiResDTI'      : r'HiResDTIRegToT1.nii.gz'                                     ,
    'HiRsMD'        : r'HiResDTIRegToT1_MD.nii.gz'                                  ,
    'HiResFA'       : r'HiResDTIRegToT1_FA.nii.gz'                  
    
    })

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(omb_dl)

if __name__ == '__main__':
    unittest.main()

