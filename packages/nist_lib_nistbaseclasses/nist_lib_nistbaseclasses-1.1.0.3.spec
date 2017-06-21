[Package]
Name="nist_lib_nistbaseclasses"
Version="1.1.0.3"
Release=""
ID=700bf36d12790998d898fddb9b967e78
File Format="vip"
Format Version="2014"
Display Name="BaseClasses"


[Description]
Description="Base Classes for many objects"
Summary="Base Classes for many  objects"
License="NIST"
Copyright="none"
Distribution=""
Vendor="NIST"
URL=""
Packager="Allen Goldstein"
Demo="FALSE"
Release Notes=""
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
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=18
File 0="user.lib/NIST/BaseClasses/BaseClasses.lvlib"
File 1="user.lib/NIST/BaseClasses/BaseClasses.lvproj"
File 2="user.lib/NIST/BaseClasses/Object_class/BaseObject.lvclass"
File 3="user.lib/NIST/BaseClasses/Object_class/Utils/GetPathToClass.vi"
File 4="user.lib/NIST/BaseClasses/Object_class/Utils/Implementation Error.vi"
File 5="user.lib/NIST/BaseClasses/Object_class/Utils/LoadClassFromFile.vi"
File 6="user.lib/NIST/BaseClasses/Object_class/Public/Create.vi"
File 7="user.lib/NIST/BaseClasses/Object_class/Public/Destroy.vi"
File 8="user.lib/NIST/BaseClasses/documentation/BaseClasses_Specification.docx"
File 9="user.lib/NIST/BaseClasses/documentation/DISCLAIMER.txt"
File 10="user.lib/NIST/BaseClasses/documentation/LICENSE.txt"
File 11="user.lib/NIST/BaseClasses/documentation/graphics/BasePlugin_uml.vsdx"
File 12="user.lib/NIST/BaseClasses/documentation/graphics/Drawing1.vsdx"
File 13="user.lib/NIST/BaseClasses/BasePlugin_class/BasePlugin.lvclass"
File 14="user.lib/NIST/BaseClasses/BasePlugin_class/Public/Create.vi"
File 15="user.lib/NIST/BaseClasses/BasePlugin_class/Public/Destroy.vi"
File 16="user.lib/NIST/BaseClasses/BasePlugin_class/Accessors/Read PluginIniFilePath.vi"
File 17="user.lib/NIST/BaseClasses/BasePlugin_class/Accessors/Write PluginIniFilePath.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=6
File 0="_functions_nist_lib_nistbaseclasses_1.mnu"
File 1="_functions_nist_lib_nistbaseclasses_2.mnu"
File 2="_functions_nist_lib_nistbaseclasses_3.mnu"
File 3="_functions_nist_lib_nistbaseclasses_4.mnu"
File 4="_functions_nist_lib_nistbaseclasses_5.mnu"
File 5="functions_NIST_lib_NistBaseClasses.mnu"
