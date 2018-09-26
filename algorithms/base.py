from qgis.core import QgsProcessingAlgorithm
from qgis.PyQt.QtCore import QCoreApplication


class SpcAlgorithm(QgsProcessingAlgorithm):

    def name(self):
        return self.__class__.__name__

    def displayName(self):
        return self.name()

    def groupId(self):
        return self.__module__.split('.')[-1]

    def group(self):
        return self.groupId()
        
    def createInstance(self):
        return self.__class__()

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)
