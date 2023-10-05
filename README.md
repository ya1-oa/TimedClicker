# TimedClicker
A GUI program that opens a website using a webdriver and automates clicking tasks on the site at set time intervals.

Make sure that you have in the directory of the .py file the following:

1. A folder called sunvalley, with sunvalley tcl file and themes folder.

2 folder called called driver with the chrome webdriver binary inside

3 folder called icon with desired icons inside, both an .ico and .png version.

When you are ready run the nuitka commmand to convert to C, and package all depencencies together into a binary.

nuitka --windows-icon-from-ico=icon/sec.ico --include-data-dir=icon/=icon --include-data-dir=sunvalley=sunvalley --include-data-file=driver/chromedriver.exe=driver/chromedriver.exe --include-package-data=selenium  --enable-plugin=tk-inter --enable-plugin=numpy --enable-plugin=pyqt5 --windows-disable-console  --follow-imports --onefile clicker-core.py
