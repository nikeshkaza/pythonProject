import pandas as pd
from IncomePrediction.code.IncomePrediction_final.application_logging import logger

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.

    Written By: iNeuron Intelligence
    Version: 1.0
    Revisions: None

    """
    #file_object = open("IncomePrediction/code/IncomePrediction_final/Training_Logs/ModelTrainingLog.txt", 'a+')
    #log_writer = logger.App_Logger()

    def __init__(self, file_object, logger_object):
        self.training_file='/Users/nikeshkaza/PycharmProjects/pythonProject/IncomePrediction/code/IncomePrediction_final/Training_FileFromDB/InputFile.csv'
        self.file_object=file_object
        self.logger_object=logger_object

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception

         Written By: iNeuron Intelligence
        Version: 1.0
        Revisions: None

        """
        self.logger_object.log(self.file_object,'Entered the get_data method of the Data_Getter class')
        try:
            self.data= pd.read_csv(self.training_file) # reading the data file
            self.logger_object.log(self.file_object,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()


data_getter=Data_Getter(open("/Users/nikeshkaza/PycharmProjects/pythonProject/IncomePrediction/code/IncomePrediction_final/Training_Logs/ModelTrainingLog.txt", 'a+'),logger.App_Logger())
data=data_getter.get_data()
print(data)