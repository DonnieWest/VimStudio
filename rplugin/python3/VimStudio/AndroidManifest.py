import xml.etree.ElementTree as ET
from .ProjectController import ProjectController

class AndroidManifest:

    def __init__(self):
        self.Manifest = ProjectController().findAndroidManifest()

    def getPackage(self):
        tree = ET.parse(self.Manifest)
        root = tree.getroot()
        package = root.get("package")
        return package

    def getMainActivityName(self):
        activity = self.getMainActivity()
        return activity.split(".")[-1]

    def getMainActivity(self):
        tree = ET.parse(self.Manifest)
        root = tree.getroot()
        activities = root.iter("activity")
        for activity in activities:
            actions = activity.iter("action")
            for action in actions:
                if action.get('{http://schemas.android.com/apk/res/android}name') == 'android.intent.action.MAIN':
                    MainActivity = activity.get('{http://schemas.android.com/apk/res/android}name')
                    return MainActivity

    def pathToMainActivity(self):
        path = self.getMainActivity()
        return("./src/main/java/" + path.replace(".", "/") + ".java")
