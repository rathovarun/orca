#!/usr/bin/python

"""Test of line navigation."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(PauseAction(3000))
sequence.append(KeyComboAction("<Control>Home"))
sequence.append(KeyComboAction("Down"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "1. Line Down",
    ["BRAILLE LINE:  '\xbb\xa0search tips\xa0  $l Submit Search push button'",
     "     VISIBLE:  '\xbb\xa0search tips\xa0  $l Submit Search', cursor=1",
     "SPEECH OUTPUT: '\xbb\xa0'",
     "SPEECH OUTPUT: 'search tips'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '\xa0 '",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Search'",
     "SPEECH OUTPUT: 'Submit Search'",
     "SPEECH OUTPUT: 'push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "2. Line Down",
    ["BRAILLE LINE:  'Home Page'",
     "     VISIBLE:  'Home Page', cursor=1",
     "SPEECH OUTPUT: 'Home Page'",
     "SPEECH OUTPUT: 'Sun Developer Network'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "3. Line Down",
    ["BRAILLE LINE:  'APIs Downloads Products Support Training Participate'",
     "     VISIBLE:  'APIs Downloads Products Support ', cursor=1",
     "SPEECH OUTPUT: 'APIs'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Downloads'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Products'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Support'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Training'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Participate'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "4. Line Down",
    ["BRAILLE LINE:  ''",
     "     VISIBLE:  '', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "5. Line Down",
    ["BRAILLE LINE:  'Installation Notes document frame'",
     "     VISIBLE:  'Installation Notes document fram', cursor=1",
     "SPEECH OUTPUT: 'blank'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "6. Line Down",
    ["BRAILLE LINE:  'JavaTM SE 6 Release Notes'",
     "     VISIBLE:  'JavaTM SE 6 Release Notes', cursor=1",
     "SPEECH OUTPUT: 'JavaTM SE 6 Release Notes'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "7. Line Down",
    ["BRAILLE LINE:  'JavaTM SE 6 Release Notes'",
     "     VISIBLE:  'JavaTM SE 6 Release Notes', cursor=5",
     "SPEECH OUTPUT: 'JavaTM SE 6 Release Notes'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "8. Line Down",
    ["BRAILLE LINE:  'JavaTM SE 6 Release Notes'",
     "     VISIBLE:  'JavaTM SE 6 Release Notes', cursor=7",
     "SPEECH OUTPUT: 'JavaTM SE 6 Release Notes'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "9. Line Down",
    ["BRAILLE LINE:  'Linux Installation (32-bit) h1'",
     "     VISIBLE:  'Linux Installation (32-bit) h1', cursor=1",
     "SPEECH OUTPUT: 'Linux Installation (32-bit)'",
     "SPEECH OUTPUT: 'heading level 1'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "10. Line Down",
    ["BRAILLE LINE:  'separator'",
     "     VISIBLE:  'separator', cursor=1",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "11. Line Down",
    ["BRAILLE LINE:  'JDK Documentation'",
     "     VISIBLE:  'JDK Documentation', cursor=1",
     "SPEECH OUTPUT: 'JDK Documentation'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "12. Line Down",
    ["BRAILLE LINE:  'Contents h2'",
     "     VISIBLE:  'Contents h2', cursor=1",
     "SPEECH OUTPUT: 'Contents'",
     "SPEECH OUTPUT: 'heading level 2'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "13. Line Down",
    ["BRAILLE LINE:  'System Requirements'",
     "     VISIBLE:  'System Requirements', cursor=1",
     "SPEECH OUTPUT: 'System Requirements'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "14. Line Down",
    ["BRAILLE LINE:  'JDK Installation Instructions'",
     "     VISIBLE:  'JDK Installation Instructions', cursor=1",
     "SPEECH OUTPUT: 'JDK Installation Instructions'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "15. Line Down",
    ["BRAILLE LINE:  'System RequirementsJDK Installation Instructions\xa0\xa0\xa0Installation of Self-Extracting Binary'",
     "     VISIBLE:  '\xa0\xa0\xa0Installation of Self-Extracti', cursor=2",
     "SPEECH OUTPUT: 'System Requirements'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'",
     "SPEECH OUTPUT: 'JDK Installation Instructions'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "\xa0\xa0\xa0'",
     "SPEECH OUTPUT: 'Installation of Self-Extracting Binary'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "16. Line Down",
    ["BRAILLE LINE:  '\xa0\xa0\xa0Installation of RPM File'",
     "     VISIBLE:  '\xa0\xa0\xa0Installation of RPM File', cursor=1",
     "SPEECH OUTPUT: '\xa0\xa0\xa0'",
     "SPEECH OUTPUT: 'Installation of RPM File'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "17. Line Down",
    ["BRAILLE LINE:  'Java Plugin Browser Registration Instructions'",
     "     VISIBLE:  'Java Plugin Browser Registration', cursor=1",
     "SPEECH OUTPUT: 'Java Plugin Browser Registration Instructions'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "18. Line Down",
    ["BRAILLE LINE:  'Java Web Start Installation Notes'",
     "     VISIBLE:  'Java Web Start Installation Note', cursor=1",
     "SPEECH OUTPUT: 'Java Web Start Installation Notes'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "19. Line Down",
    ["BRAILLE LINE:  'Troubleshooting'",
     "     VISIBLE:  'Troubleshooting', cursor=1",
     "SPEECH OUTPUT: 'Troubleshooting'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "20. Line Down",
    ["BRAILLE LINE:  'System Requirements h2'",
     "     VISIBLE:  'System Requirements h2', cursor=1",
     "SPEECH OUTPUT: 'System Requirements'",
     "SPEECH OUTPUT: 'heading level 2'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "21. Line Down",
    ["BRAILLE LINE:  'See supported System Configurations for information about supported platforms, operating systems, desktop managers, and browsers.'",
     "     VISIBLE:  'See supported System Configurati', cursor=1",
     "SPEECH OUTPUT: 'See supported '",
     "SPEECH OUTPUT: 'System Configurations'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for information about supported platforms, operating systems, desktop managers, and browsers. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "22. Line Down",
    ["BRAILLE LINE:  'For issues, see the Troubleshooting section below.'",
     "     VISIBLE:  'For issues, see the Troubleshoot', cursor=1",
     "SPEECH OUTPUT: 'For issues, see the '",
     "SPEECH OUTPUT: 'Troubleshooting'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' section below. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "23. Line Down",
    ["BRAILLE LINE:  'Installation Instructions h2'",
     "     VISIBLE:  'Installation Instructions h2', cursor=1",
     "SPEECH OUTPUT: 'Installation Instructions'",
     "SPEECH OUTPUT: 'heading level 2'"]))

# There's some crazy bug here that makes us treat the lines that follow as a single line
# I think it's a Gecko bug. But for now, we'll skip past it as this seems an edge case.
sequence.append(KeyComboAction("Down"))
sequence.append(KeyComboAction("Down"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "24. Line Down",
    ["BRAILLE LINE:  '\u2022Java Web Start Installation Notes'",
     "     VISIBLE:  '\u2022Java Web Start Installation Not', cursor=1",
     "SPEECH OUTPUT: '\u2022'",
     "SPEECH OUTPUT: 'Java Web Start Installation Notes'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "25. Line Down",
    ["BRAILLE LINE:  'Install formats - This version of the JDK is available in two installation formats. \u2022Self-extracting Binary File - This file can be used to install the JDK in a location chosen by the user. This one can be installed by anyone (not only root users), and it can'",
     "     VISIBLE:  'Install formats - This version o', cursor=1",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Install formats - This version of the JDK is available in two installation formats. '",
     "SPEECH OUTPUT: '\u2022Self-extracting Binary File - This file can be used to install the JDK in a location chosen by the user. This one can be installed by anyone (not only root users), and it can '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "26. Line Down",
    ["BRAILLE LINE:  'Install formats - This version of the JDK is available in two installation formats. \u2022Self-extracting Binary File - This file can be used to install the JDK in a location chosen by the user. This one can be installed by anyone (not only root users), and it can'",
     "     VISIBLE:  '\u2022Self-extracting Binary File - T', cursor=1",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Install formats - This version of the JDK is available in two installation formats. '",
     "SPEECH OUTPUT: '\u2022Self-extracting Binary File - This file can be used to install the JDK in a location chosen by the user. This one can be installed by anyone (not only root users), and it can '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "27. Line Down",
    ["BRAILLE LINE:  'easily be installed in any location. As long as you are not root user, it cannot displace the system version of the Java platform suppled by Linux. To use this file, see'",
     "     VISIBLE:  'easily be installed in any locat', cursor=1",
     "SPEECH OUTPUT: 'easily be installed in any location. As long as you are not root user, it cannot displace the system version of the Java platform suppled by Linux. To use this file, see '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "28. Line Down",
    ["BRAILLE LINE:  'Installation of Self-Extracting Binary below. '",
     "     VISIBLE:  'Installation of Self-Extracting ', cursor=1",
     "SPEECH OUTPUT: 'Installation of Self-Extracting Binary'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' below. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "29. Line Down",
    ["BRAILLE LINE:  '\u2022RPM Packages - A rpm.bin file containing RPM packages, installed with the rpm utility. Requires root access to install. RPM packages are the recommended method for'",
     "     VISIBLE:  '\u2022RPM Packages - A rpm.bin file c', cursor=1",
     "SPEECH OUTPUT: '\u2022RPM Packages - A rpm.bin file containing RPM packages, installed with the rpm utility. Requires root access to install. RPM packages are the recommended method for '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "30. Line Down",
    ["BRAILLE LINE:  'installation on Linux. To use this bundle, see Installation of RPM File below.'",
     "     VISIBLE:  'installation on Linux. To use th', cursor=1",
     "SPEECH OUTPUT: 'installation on Linux. To use this bundle, see '",
     "SPEECH OUTPUT: 'Installation of RPM File'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' below. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "31. Line Down",
    ["BRAILLE LINE:  'Choose the install format that is most suitable to your needs. table cell'",
     "     VISIBLE:  'Choose the install format that i', cursor=1",
     "SPEECH OUTPUT: 'Choose the install format that is most suitable to your needs. '",
     "SPEECH OUTPUT: 'blank'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "32. Line Down",
    ["BRAILLE LINE:  'Note: For any text on this page containing the following notation, you must substitute the appropriate JDK update version number for the notation.'",
     "     VISIBLE:  'Note: For any text on this page ', cursor=1",
     "SPEECH OUTPUT: 'Note: For any text on this page containing the following notation, you must substitute the appropriate JDK update version number for the notation. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "33. Line Down",
    ["BRAILLE LINE:  '<version>'",
     "     VISIBLE:  '<version>', cursor=1",
     "SPEECH OUTPUT: '<version>",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "34. Line Down",
    ["BRAILLE LINE:  ''",
     "     VISIBLE:  '', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "35. Line Down",
    ["BRAILLE LINE:  'For example, if you were downloading update 6_01, the following command:'",
     "     VISIBLE:  'For example, if you were downloa', cursor=1",
     "SPEECH OUTPUT: 'For example, if you were downloading update 6_01, the following command: '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "36. Line Down",
    ["BRAILLE LINE:  './jdk-6<version>-linux-i586.bin'",
     "     VISIBLE:  './jdk-6<version>-linux-i586.bin', cursor=1",
     "SPEECH OUTPUT: './jdk-6<version>-linux-i586.bin",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "37. Line Down",
    ["BRAILLE LINE:  ''",
     "     VISIBLE:  '', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "38. Line Down",
    ["BRAILLE LINE:  'would become:'",
     "     VISIBLE:  'would become:', cursor=1",
     "SPEECH OUTPUT: 'would become: '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "39. Line Down",
    ["BRAILLE LINE:  './jdk-6u1-linux-i586.bin'",
     "     VISIBLE:  './jdk-6u1-linux-i586.bin', cursor=1",
     "SPEECH OUTPUT: './jdk-6u1-linux-i586.bin",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "40. Line Down",
    ["BRAILLE LINE:  ''",
     "     VISIBLE:  '', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "41. Line Down",
    ["BRAILLE LINE:  'Installation of Self-Extracting Binary h3'",
     "     VISIBLE:  'Installation of Self-Extracting ', cursor=1",
     "SPEECH OUTPUT: 'Installation of Self-Extracting Binary'",
     "SPEECH OUTPUT: 'heading level 3'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "42. Line Down",
    ["BRAILLE LINE:  'Use these instructions if you want to use the self-extracting binary file to install the JDK. If you want to install RPM packages instead, see Installation of RPM File. '",
     "     VISIBLE:  'Use these instructions if you wa', cursor=1",
     "SPEECH OUTPUT: 'Use these instructions if you want to use the self-extracting binary file to install the JDK. If you want to install RPM packages instead, see '",
     "SPEECH OUTPUT: 'Installation of RPM File'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "43. Line Down",
    ["BRAILLE LINE:  '1. Download and check the download file size to ensure that you have downloaded the full, uncorrupted software bundle.'",
     "     VISIBLE:  '1. Download and check the downlo', cursor=1",
     "SPEECH OUTPUT: '1. Download and check the download file size to ensure that you have downloaded the full, uncorrupted software bundle.'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "44. Line Down",
    ["BRAILLE LINE:  'You can download to any directory you choose; it does not have to be the directory where you want to install the JDK.'",
     "     VISIBLE:  'You can download to any director', cursor=1",
     "SPEECH OUTPUT: 'You can download to any directory you choose; it does not have to be the directory where you want to install the JDK. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "45. Line Down",
    ["BRAILLE LINE:  'Before you download the file, notice its byte size provided on the download page on the web site. Once the download has completed, compare that file size to the'",
     "     VISIBLE:  'Before you download the file, no', cursor=1",
     "SPEECH OUTPUT: 'Before you download the file, notice its byte size provided on the download page on the web site. Once the download has completed, compare that file size to the '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "46. Line Down",
    ["BRAILLE LINE:  'size of the downloaded file to make sure they are equal.'",
     "     VISIBLE:  'size of the downloaded file to m', cursor=1",
     "SPEECH OUTPUT: 'size of the downloaded file to make sure they are equal. '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "47. Line Down",
    ["BRAILLE LINE:  '2. Make sure that execute permissions are set on the self-extracting binary.'",
     "     VISIBLE:  '2. Make sure that execute permis', cursor=1",
     "SPEECH OUTPUT: '2. Make sure that execute permissions are set on the self-extracting binary. '"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
