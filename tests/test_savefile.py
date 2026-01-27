import unittest
import sys
import os
thisfile = os.path.dirname(os.path.abspath(__file__))
rel_path = os.path.normpath(thisfile + "/../src")
sys.path.append(rel_path)

from datetime import date
from savefilename import SaveFileName

class TestSaveFile(unittest.TestCase):
    def test_basic_use_case(self) -> None:
        testCase = SaveFileName("test")
        currentDate = date.today().strftime("%Y%m%d")
        currentTime = date.today().strftime("%H%M%S")
        test_given_name = testCase.get_given_name()
        expected_given_name = "test"
        test_basename = testCase.get_full_filename_base()
        expected_basename = currentDate + "-" + currentTime + "_" + test_given_name
        test_prop_name = testCase.get_full_prop_filename()
        expected_prop_name = expected_basename + ".caf"
        self.assertEqual(expected_given_name, test_given_name, msg="Given Name not saved correctly")
        self.assertEqual(expected_basename, test_basename, msg="Basename not created properly")
        self.assertEqual(expected_prop_name, test_prop_name, msg="Propietary save file name not created correctly")

    def test_with_empty_name(self) -> None:
        testCase = SaveFileName("")
        currentDate = date.today().strftime("%Y%m%d")
        currentTime = date.today().strftime("%H%M%S")
        test_given_name = testCase.get_given_name()
        expected_given_name = ""
        test_basename = testCase.get_full_filename_base()
        expected_basename = currentDate + "-" + currentTime + "_" + test_given_name
        test_prop_name = testCase.get_full_prop_filename()
        expected_prop_name = expected_basename + ".caf"
        self.assertEqual(expected_given_name, test_given_name, msg="Given Name not saved correctly")
        self.assertEqual(expected_basename, test_basename, msg="Basename not created properly")
        self.assertEqual(expected_prop_name, test_prop_name, msg="Propietary save file name not created correctly")


    def test_from_valid_filename(self) -> None:
        testCase = SaveFileName("", "20201212-151012_testcase.caf")
        test_given_name = testCase.get_given_name()
        expected_given_name = "testcase"
        test_basename = testCase.get_full_filename_base()
        expected_basename = "20201212-151012_testcase"
        test_prop_name = testCase.get_full_prop_filename()
        expected_full_prop_name = "20201212-151012_testcase.caf"
        self.assertEqual(test_given_name, expected_given_name)
        self.assertEqual(test_basename, expected_basename)
        self.assertEqual(test_prop_name, expected_full_prop_name)

    def test_from_empty_filename(self) -> None:
        testCase = SaveFileName("", "20201212-151012_.caf")
        test_given_name = testCase.get_given_name()
        expected_given_name = ""
        test_basename = testCase.get_full_filename_base()
        expected_basename = "20201212-151012_"
        test_prop_name = testCase.get_full_prop_filename()
        expected_full_prop_name = "20201212-151012_.caf"
        self.assertEqual(test_given_name, expected_given_name)
        self.assertEqual(test_basename, expected_basename)
        self.assertEqual(test_prop_name, expected_full_prop_name)

    def test_invalid_extension(self) -> None:
        testFilename = "Test.xml"
        self.assertRaises(ValueError, lambda : SaveFileName("", testFilename))

    def test_invalid_structure(self) -> None:
        testFilename1, testFilename2 = "13021987.caf", "bla_01011990-121015.caf"
        self.assertRaises(ValueError, lambda : SaveFileName("", testFilename1))
        self.assertRaises(ValueError, lambda : SaveFileName("", testFilename2))

    def test_change_filename(self)->None:
        testCase = SaveFileName("test")
        currentDate = date.today().strftime("%Y%m%d")
        currentTime = date.today().strftime("%H%M%S")
        testCase.update_given_name("updated")
        test_given_name = testCase.get_given_name()
        expected_given_name = "updated"
        test_basename = testCase.get_full_filename_base()
        expected_basename = currentDate + "-" + currentTime + "_" + test_given_name
        test_prop_name = testCase.get_full_prop_filename()
        expected_prop_name = expected_basename + ".caf"
        self.assertEqual(expected_given_name, test_given_name, msg="Given Name not saved correctly")
        self.assertEqual(expected_basename, test_basename, msg="Basename not created properly")
        self.assertEqual(expected_prop_name, test_prop_name, msg="Propietary save file name not created correctly")


