[Package]
Name="nist_lib_nist_qmh_template"
Version="0.1.0.1"
Release=""
ID=f3375879cb19f45faf8a235f8c0e6a64
File Format="vip"
Format Version="2014"
Display Name="NIST QMH Template"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2017, NIST"
Distribution=""
Vendor="NIST"
URL=""
Packager="gra1"
Demo="FALSE"
Release Notes="First build attempt"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="nist_lib_nisterrorlib>=1.1.0.2"
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
Num Files=13
File 0="ProjectTemplates/Source/NIST/QMH_Template/MyQMH.vi"
File 1="ProjectTemplates/Source/NIST/QMH_Template/QMH_Template.lvproj"
File 2="ProjectTemplates/Source/NIST/QMH_Template/UserEvents/clUserEventDataType.ctl"
File 3="ProjectTemplates/Source/NIST/QMH_Template/UserEvents/clUserEvents.ctl"
File 4="ProjectTemplates/Source/NIST/QMH_Template/UserEvents/ObtainUserEvents.vi"
File 5="ProjectTemplates/Source/NIST/QMH_Template/UserEvents/StopEvent.vi"
File 6="ProjectTemplates/Source/NIST/QMH_Template/Queue/clMessage.ctl"
File 7="ProjectTemplates/Source/NIST/QMH_Template/Queue/Dequeue.vi"
File 8="ProjectTemplates/Source/NIST/QMH_Template/Queue/EnqueError.vi"
File 9="ProjectTemplates/Source/NIST/QMH_Template/Queue/Enqueue.vi"
File 10="ProjectTemplates/Source/NIST/QMH_Template/Queue/ObtainQueue.vi"
File 11="ProjectTemplates/Source/NIST/QMH_Template/Queue/Queue.lvlib"
File 12="ProjectTemplates/MetaData/NIST_QMH_Template.xml"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_nist_lib_nist_qmh_template_1.mnu"
File 1="_functions_nist_lib_nist_qmh_template_2.mnu"
File 2="_functions_nist_lib_nist_qmh_template_3.mnu"
File 3="_functions_nist_lib_nist_qmh_template_4.mnu"
File 4="_functions_nist_lib_nist_qmh_template_5.mnu"
File 5="functions_NIST_lib_NIST_QMH_Template.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=6
File 0="_controls_nist_lib_nist_qmh_template_1.mnu"
File 1="_controls_nist_lib_nist_qmh_template_2.mnu"
File 2="_controls_nist_lib_nist_qmh_template_3.mnu"
File 3="_controls_nist_lib_nist_qmh_template_4.mnu"
File 4="_controls_nist_lib_nist_qmh_template_5.mnu"
File 5="controls_NIST_lib_NIST_QMH_Template.mnu"
