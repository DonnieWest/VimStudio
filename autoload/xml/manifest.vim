" Vim XML data file
" Last Change: 2016-10-30

let g:xmldata_manifest = {
\ 'vimxmlentities': ['lt', 'gt', 'amp', 'apos', 'quot'],
\ 'vimxmlroot': ['manifest'],
\ 'provider': [
\ ['intent-filter', 'meta-data', 'path-permission'],
\ {'android:authorities': [], 'android:enabled': [], 'android:exported': [], 'android:grantUriPermissions': [], 'android:label': [], 'android:name': [], 'android:permission': [], 'android:syncable': [], 'android:writePermission': []}
\ ],
\ 'manifest': [
\ ['application', 'instrumentation', 'permission', 'supports-screens', 'uses-feature', 'uses-library', 'uses-permission', 'uses-permission-sdk-m', 'uses-sdk'],
\ {'android:installLocation': [], 'android:largeHeap': [], 'android:theme': [], 'android:uiOptions': [], 'android:versionCode': [], 'android:versionName': [], 'package': []}
\ ],
\ 'uses-permission': [
\ [],
\ {'android:maxSdkVersion': [], 'android:name': [], 'tools:node': []}
\ ],
\ 'meta-data': [
\ [],
\ {'android:name': [], 'android:resource': [], 'android:value': []}
\ ],
\ 'data': [
\ [],
\ {'android:host': [], 'android:mimeType': [], 'android:path': [], 'android:pathPattern': [], 'android:pathPrefix': [], 'android:scheme': []}
\ ],
\ 'path-permission': [
\ [],
\ {'android:pathPrefix': [], 'android:readPermission': []}
\ ],
\ 'uses-library': [
\ [],
\ {'android:name': [], 'android:required': []}
\ ],
\ 'activity': [
\ ['intent-filter', 'layout', 'meta-data'],
\ {'android:allowEmbedded': [], 'android:clearTaskOnLaunch': [], 'android:configChanges': [], 'android:enabled': [], 'android:excludeFromRecents': [], 'android:exported': [], 'android:icon': [], 'android:label': [], 'android:launchMode': [], 'android:lockTaskMode': [], 'android:logo': [], 'android:minHeight': [], 'android:minWidth': [], 'android:name': [], 'android:parentActivityName': [], 'android:persistableMode': [], 'android:relinquishTaskIdentity': [], 'android:resizeableActivity': [], 'android:screenOrientation': [], 'android:supportsPictureInPicture': [], 'android:taskAffinity': [], 'android:theme': [], 'android:uiOptions': [], 'android:windowSoftInputMode': [], 'tools:replace': []}
\ ],
\ 'activity-alias': [
\ ['intent-filter', 'meta-data'],
\ {'android:label': [], 'android:name': [], 'android:targetActivity': []}
\ ],
\ 'permission': [
\ [],
\ {'android:description': [], 'android:label': [], 'android:name': [], 'android:protectionLevel': []}
\ ],
\ 'category': [
\ [],
\ {'android:name': []}
\ ],
\ 'intent-filter': [
\ ['action', 'category', 'data'],
\ {'android:autoVerify': [], 'android:icon': [], 'android:label': [], 'android:priority': [], 'tools:ignore': [], 'tools:node': []}
\ ],
\ 'supports-screens': [
\ [],
\ {'android:anyDensity': [], 'android:compatibleWidthLimitDp': [], 'android:largeScreens': [], 'android:normalScreens': [], 'android:requiresSmallestWidthDp': [], 'android:smallScreens': [], 'android:xlargeScreens': []}
\ ],
\ 'action': [
\ [],
\ {'android:name': []}
\ ],
\ 'receiver': [
\ ['intent-filter', 'meta-data'],
\ {'android:description': [], 'android:directBootAware': [], 'android:enabled': [], 'android:exported': [], 'android:label': [], 'android:name': [], 'android:permission': [], 'tools:ignore': []}
\ ],
\ 'layout': [
\ [],
\ {'android:defaultHeight': [], 'android:defaultWidth': [], 'android:gravity': [], 'android:minHeight': [], 'android:minWidth': []}
\ ],
\ 'service': [
\ ['intent-filter', 'meta-data'],
\ {'android:directBootAware': [], 'android:enabled': [], 'android:exported': [], 'android:label': [], 'android:name': [], 'android:permission': [], 'android:process': [], 'tools:ignore': []}
\ ],
\ 'uses-feature': [
\ [],
\ {'android:glEsVersion': [], 'android:name': [], 'android:required': []}
\ ],
\ 'application': [
\ ['activity', 'activity-alias', 'meta-data', 'provider', 'receiver', 'service', 'uses-library', 'uses-permission'],
\ {'android:allowBackup': [], 'android:backupAgent': [], 'android:banner': [], 'android:debuggable': [], 'android:description': [], 'android:fullBackupContent': [], 'android:hardwareAccelerated': [], 'android:hasCode': [], 'android:icon': [], 'android:isGame': [], 'android:label': [], 'android:largeHeap': [], 'android:logo': [], 'android:manageSpaceActivity': [], 'android:name': [], 'android:resizeableActivity': [], 'android:restoreAnyVersion': [], 'android:roundIcon': [], 'android:screenOrientation': [], 'android:supportsPictureInPicture': [], 'android:supportsRtl': [], 'android:theme': [], 'android:vmSafeMode': [], 'tools:ignore': [], 'tools:replace': []}
\ ],
\ 'uses-sdk': [
\ [],
\ {'android:minSdkVersion': [], 'android:targetSdkVersion': [], 'tools:overrideLibrary': []}
\ ],
\ 'uses-permission-sdk-m': [
\ [],
\ {'android:name': []}
\ ],
\ 'instrumentation': [
\ [],
\ {'android:functionalTest': [], 'android:handleProfiling': [], 'android:label': [], 'android:name': [], 'android:targetPackage': []}
\ ],
\ }
