# FTF
Fast Transient Finding Algorithm


Run the master2.sh or master.sh code in shell.  The command will look like: master2.sh DataSourceDirectory integerforsizeofslidingwindow integerformaxnumberofinflectionpointstolookfor.  You will need to manually change the location of the CodeSourceDirectory in the master2.sh code to where the code lives on your device.  The data files should be text files that have the following columns in this order: MJD(time) mag mag_error upper_limit_mag.  If you data does not look like this, you can either edit the dataExtract2.py code, or recast your data to look as described.

The code will create a new directory next to the data source directory called DataSourceDirectory_newWork.  In this directory you will find folders containing the lightcurves of anomylous data (as well as other nights from the same source if this data exists).  You will also find text files containing the names of all the files with suspected anomylous behavior.

The master.sh code will have extra directories where only the possible transient lightcurves are plotted, in addition to the possible transient and all other nights of that sources data as plotted in master2.sh
