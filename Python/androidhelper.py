#-------------------------------------------------------------------------------
# Name:         androidhelper.py
#
# Purpose:      To simplify Python-for-Android SL4A development in IDEs with a
#               "hepler" class derived from the default Android class containing
#               SL4A facade functions & API documentation
#
# Usage:        copy androidhelper.py into either the folder containing your
#               SL4A python script or to some location on the python import path
#               that your IDE can see and in your script, instead of:
#
#                   import android
#
#               use the following import code:
#
#                   try:
#                       import androidhelper as android
#                   except:
#                       import android
#
# Sources:      Derived from API documentation in HTML files contained in
#               /android-scripting/android/ScriptingLayerForAndroid/assets/sl4adoc.zip
#
# Version:      for SL4A Release R5, created on 7-Apr-2012
#
# Author(s):    Hariharan Srinath (srinathdevelopment@gmail.com) with inputs
#               from Robbie Matthews (rjmatthews62@gmail.com)
#
# Copyright:    Copyright (C) 2012, Hariharan Srinath, Robbie Matthews
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import android

class Android(android.Android):
        def setResultBoolean(self,resultCode,resultValue):
                '''
                setResultBoolean(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Boolean)
                '''
                return self._rpc("setResultBoolean",resultCode,resultValue)

        def setResultBooleanArray(self,resultCode,resultValue):
                '''
                setResultBooleanArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Boolean)
                '''
                return self._rpc("setResultBooleanArray",resultCode,resultValue)

        def setResultByte(self,resultCode,resultValue):
                '''
                setResultByte(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Byte)
                '''
                return self._rpc("setResultByte",resultCode,resultValue)

        def setResultByteArray(self,resultCode,resultValue):
                '''
                setResultByteArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Byte)
                '''
                return self._rpc("setResultByteArray",resultCode,resultValue)

        def setResultChar(self,resultCode,resultValue):
                '''
                setResultChar(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Character)
                '''
                return self._rpc("setResultChar",resultCode,resultValue)

        def setResultCharArray(self,resultCode,resultValue):
                '''
                setResultCharArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Character)
                '''
                return self._rpc("setResultCharArray",resultCode,resultValue)

        def setResultDouble(self,resultCode,resultValue):
                '''
                setResultDouble(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Double)
                '''
                return self._rpc("setResultDouble",resultCode,resultValue)

        def setResultDoubleArray(self,resultCode,resultValue):
                '''
                setResultDoubleArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Double)
                '''
                return self._rpc("setResultDoubleArray",resultCode,resultValue)

        def setResultFloat(self,resultCode,resultValue):
                '''
                setResultFloat(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Float)
                '''
                return self._rpc("setResultFloat",resultCode,resultValue)

        def setResultFloatArray(self,resultCode,resultValue):
                '''
                setResultFloatArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Float)
                '''
                return self._rpc("setResultFloatArray",resultCode,resultValue)

        def setResultInteger(self,resultCode,resultValue):
                '''
                setResultInteger(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Integer)
                '''
                return self._rpc("setResultInteger",resultCode,resultValue)

        def setResultIntegerArray(self,resultCode,resultValue):
                '''
                setResultIntegerArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Integer)
                '''
                return self._rpc("setResultIntegerArray",resultCode,resultValue)

        def setResultLong(self,resultCode,resultValue):
                '''
                setResultLong(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Long)
                '''
                return self._rpc("setResultLong",resultCode,resultValue)

        def setResultLongArray(self,resultCode,resultValue):
                '''
                setResultLongArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Long)
                '''
                return self._rpc("setResultLongArray",resultCode,resultValue)

        def setResultSerializable(self,resultCode,resultValue):
                '''
                setResultSerializable(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Serializable)
                '''
                return self._rpc("setResultSerializable",resultCode,resultValue)

        def setResultShort(self,resultCode,resultValue):
                '''
                setResultShort(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Short)
                '''
                return self._rpc("setResultShort",resultCode,resultValue)

        def setResultShortArray(self,resultCode,resultValue):
                '''
                setResultShortArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (Short)
                '''
                return self._rpc("setResultShortArray",resultCode,resultValue)

        def setResultString(self,resultCode,resultValue):
                '''
                setResultString(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (String)
                '''
                return self._rpc("setResultString",resultCode,resultValue)

        def setResultStringArray(self,resultCode,resultValue):
                '''
                setResultStringArray(resultCode,resultValue)
                Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
                        resultCode (Integer) The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1)
                        resultValue (String)
                '''
                return self._rpc("setResultStringArray",resultCode,resultValue)

        def environment(self):
                '''
                environment(self)
                A map of various useful environment details
                Map returned:
                TZ = Timezone
                id = Timezone ID
                display = Timezone display name
                offset = Offset from UTC (in ms)
                SDK = SDK Version
                download = default download path
                appcache = Location of application cache
                sdcard = Space on sdcard
                availblocks = Available blocks
                blockcount = Total Blocks
                blocksize = size of block.
                '''
                return self._rpc("environment")

        def getClipboard(self):
                '''
                getClipboard(self)
                Read text from the clipboard.
                returns: (String) The text in the clipboard.
                '''
                return self._rpc("getClipboard")

        def getConstants(self,classname):
                '''
                getConstants(classname)
                Get list of constants (static final fields) for a class
                        classname (String) Class to get constants from
                '''
                return self._rpc("getConstants",classname)

        def getInput(self,title="SL4A Input",message="Please enter value:"):
                '''
                getInput(title="SL4A Input",message="Please enter value:")
                Queries the user for a text input.
                        title (String) title of the input box (default=SL4A Input)
                        message (String) message to display above the input box (default=Please enter value:)
                Deprecated in r3. Use dialogGetInput instead.
                '''
                return self._rpc("getInput",title,message)

        def getIntent(self):
                '''
                getIntent(self)
                Returns the intent that launched the script.
                '''
                return self._rpc("getIntent")

        def getPackageVersion(self,packageName):
                '''
                getPackageVersion(packageName)
                Returns package version name.
                        packageName (String)
                '''
                return self._rpc("getPackageVersion",packageName)

        def getPackageVersionCode(self,packageName):
                '''
                getPackageVersionCode(packageName)
                Returns package version code.
                        packageName (String)
                '''
                return self._rpc("getPackageVersionCode",packageName)

        def getPassword(self,title="SL4A Password Input",message="Please enter password:"):
                '''
                getPassword(title="SL4A Password Input",message="Please enter password:")
                Queries the user for a password.
                        title (String) title of the input box (default=SL4A Password Input)
                        message (String) message to display above the input box (default=Please enter password:)
                Deprecated in r3. Use dialogGetPassword instead.
                '''
                return self._rpc("getPassword",title,message)

        def log(self,message):
                '''
                log(message)
                Writes message to logcat.
                        message (String)
                '''
                return self._rpc("log",message)

        def makeIntent(self,action,uri=None,type=None,extras=None,categories=None,packagename=None,classname=None,flags=None):
                '''
                makeIntent(action,uri=None,type=None,extras=None,categories=None,packagename=None,classname=None,flags=None)
                Create an Intent.
                        action (String)
                        uri (String)  (optional)
                        type (String) MIME type/subtype of the URI (optional)
                        extras (JSONObject) a Map of extras to add to the Intent (optional)
                        categories (JSONArray) a List of categories to add to the Intent (optional)
                        packagename (String) name of package. If used, requires classname to be useful (optional)
                        classname (String) name of class. If used, requires packagename to be useful (optional)
                        flags (Integer) Intent flags (optional)
                returns: (Intent) An object representing an Intent
                '''
                return self._rpc("makeIntent",action,uri,type,extras,categories,packagename,classname,flags)

        def makeToast(self,message):
                '''
                makeToast(message)
                Displays a short-duration Toast notification.
                        message (String)
                '''
                return self._rpc("makeToast",message)

        def notify(self,title,message):
                '''
                notify(title,message)
                Displays a notification that will be canceled when the user clicks on it.
                        title (String) title
                        message (String)
                '''
                return self._rpc("notify",title,message)

        def requiredVersion(self,requiredVersion):
                '''
                requiredVersion(requiredVersion)
                Checks if version of SL4A is greater than or equal to the specified version.
                        requiredVersion (Integer)
                '''
                return self._rpc("requiredVersion",requiredVersion)

        def sendBroadcast(self,action,uri=None,type=None,extras=None,packagename=None,classname=None):
                '''
                sendBroadcast(action,uri=None,type=None,extras=None,packagename=None,classname=None)
                Send a broadcast.
                        action (String)
                        uri (String)  (optional)
                        type (String) MIME type/subtype of the URI (optional)
                        extras (JSONObject) a Map of extras to add to the Intent (optional)
                        packagename (String) name of package. If used, requires 