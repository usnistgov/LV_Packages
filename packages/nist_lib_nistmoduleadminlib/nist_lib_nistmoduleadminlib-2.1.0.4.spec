[Package]
Name="nist_lib_nistmoduleadminlib"
Version="2.1.0.4"
Release=""
ID=021c0376ef477f9b6c17c82a3090a386
File Format="vip"
Format Version="2014"
Display Name="ModuleAdminLib"


[Description]
Description="Support Libraries for Clonable Modules and Pluggable Modules"
Summary="Admin Library for Cloneable and Pluggable Module Templates"
License="NIST"
Copyright="none"
Distribution=""
Vendor="NIST"
URL=""
Packager="Allen Goldstein"
Demo="FALSE"
Release Notes="Renamed.  Built from the Github trunk."
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
Requires="nist_lib_nistbaseclasses>=1.0.0.1"
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
Num Files=43
File 0="user.lib/NIST/ModuleAdminLib/ModuleAdmin.lvlib"
File 1="user.lib/NIST/ModuleAdminLib/ModuleAdmin.lvproj"
File 2="user.lib/NIST/ModuleAdminLib/ModuleAdminBase/ModuleAdminBase.lvclass"
File 3="user.lib/NIST/ModuleAdminLib/ModuleAdminBase/Reset.vi"
File 4="user.lib/NIST/ModuleAdminLib/ModuleAdminBase/Accessors/Read External Launch.vi"
File 5="user.lib/NIST/ModuleAdminLib/ModuleAdminBase/Accessors/Write External Launch.vi"
File 6="user.lib/NIST/ModuleAdminLib/ModuleAdmin/AddressedToThisModule.vi"
File 7="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Module Reset.vi"
File 8="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleAdmin.lvclass"
File 9="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleName.vi"
File 10="user.lib/NIST/ModuleAdminLib/ModuleAdmin/New.vi"
File 11="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/TestModuleSync.vi"
File 12="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/Public/DestroySyncRefnums.vi"
File 13="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/Public/WaitOnEventSync.vi"
File 14="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/Public/WaitOnModuleSync.vi"
File 15="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/Public/WaitOnStopSync.vi"
File 16="user.lib/NIST/ModuleAdminLib/ModuleAdmin/ModuleSync/Private/GetSyncRefnums.vi"
File 17="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Read CloneRegRef.vi"
File 18="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Read First_.vi"
File 19="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Read Module ID.vi"
File 20="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Read ModuleName.vi"
File 21="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Read ShowPanel_.vi"
File 22="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Write CloneRegRef.vi"
File 23="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Write First_.vi"
File 24="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Write Module ID.vi"
File 25="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Write ModuleName.vi"
File 26="user.lib/NIST/ModuleAdminLib/ModuleAdmin/Accessors/Write ShowPanel_.vi"
File 27="user.lib/NIST/ModuleAdminLib/Documentation/DISCLAIMER.txt"
File 28="user.lib/NIST/ModuleAdminLib/Documentation/LICENSE.txt"
File 29="user.lib/NIST/ModuleAdminLib/Documentation/ModuleAdmin_spec.docx"
File 30="user.lib/NIST/ModuleAdminLib/Documentation/graphics/CloneRegistration_UML.vsdx"
File 31="user.lib/NIST/ModuleAdminLib/Documentation/graphics/ModuleAdmin_UML.vsdx"
File 32="user.lib/NIST/ModuleAdminLib/CloneRegistration/CloneRegistration.lvclass"
File 33="user.lib/NIST/ModuleAdminLib/CloneRegistration/TestCloneRegClass.vi"
File 34="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/Add.vi"
File 35="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/Create.vi"
File 36="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/Destroy.vi"
File 37="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/Init.vi"
File 38="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/IsFirst.vi"
File 39="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/List.vi"
File 40="user.lib/NIST/ModuleAdminLib/CloneRegistration/Public/Remove.vi"
File 41="user.lib/NIST/ModuleAdminLib/CloneRegistration/Accessors/Read vRegistry.vi"
File 42="user.lib/NIST/ModuleAdminLib/CloneRegistration/Accessors/Write vRegistry.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=11
File 0="_functions_nist_lib_nistmoduleadminlib_1.mnu"
File 1="_functions_nist_lib_nistmoduleadminlib_10.mnu"
File 2="_functions_nist_lib_nistmoduleadminlib_2.mnu"
File 3="_functions_nist_lib_nistmoduleadminlib_3.mnu"
File 4="_functions_nist_lib_nistmoduleadminlib_4.mnu"
File 5="_functions_nist_lib_nistmoduleadminlib_5.mnu"
File 6="_functions_nist_lib_nistmoduleadminlib_6.mnu"
File 7="_functions_nist_lib_nistmoduleadminlib_7.mnu"
File 8="_functions_nist_lib_nistmoduleadminlib_8.mnu"
File 9="_functions_nist_lib_nistmoduleadminlib_9.mnu"
File 10="functions_NIST_lib_NistModuleAdminLib.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=3
File 0="_controls_nist_lib_nistmoduleadminlib_1.mnu"
File 1="_controls_nist_lib_nistmoduleadminlib_2.mnu"
File 2="controls_NIST_lib_NistModuleAdminLib.mnu"
