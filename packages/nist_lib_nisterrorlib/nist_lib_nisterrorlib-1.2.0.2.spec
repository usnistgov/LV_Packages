[Package]
Name="nist_lib_nisterrorlib"
Version="1.2.0.2"
Release=""
ID=8bf3c9c1e739ed6f921ca738f168aae9
File Format="vip"
Format Version="2014"
Display Name="ErrorLib"


[Description]
Description="Extends Labview Error Handling to create multiple errors with priorities and severities."
Summary="Extends Labview Error Handling to create multiple errors with priorities and severities."
License=""
Copyright="none"
Distribution=""
Vendor="NIST"
URL=""
Packager="Allen Goldstein"
Demo="FALSE"
Release Notes="Replaced the Error Display for improved scaling"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=14.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires=""
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=9
File 0="user.lib/NIST/NISTErrorLib/AddError.vi"
File 1="user.lib/NIST/NISTErrorLib/ClearErrors.vi"
File 2="user.lib/NIST/NISTErrorLib/eDialogType.ctl"
File 3="user.lib/NIST/NISTErrorLib/ErrorDisplay.vi"
File 4="user.lib/NIST/NISTErrorLib/ErrorLib.lvproj"
File 5="user.lib/NIST/NISTErrorLib/GeneralHandler.vi"
File 6="user.lib/NIST/NISTErrorLib/NISTErrorLib.lvlib"
File 7="user.lib/NIST/NISTErrorLib/ParseErrors.vi"
File 8="user.lib/NIST/NISTErrorLib/TestError.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_NIST_lib_NISTErrorLib.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=1
File 0="controls_NIST_lib_NISTErrorLib.mnu"
