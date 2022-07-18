class Preprocessor:
    """
        This class shall  be used to clean and transform the data before training.

        Written By: iNeuron Intelligence
        Version: 1.0
        Revisions: None

        """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object

def impute_missing_values(self, data, cols_with_missing_values):
    """
                                    Method Name: impute_missing_values
                                    Description: This method replaces all the missing values in the Dataframe using KNN Imputer.
                                    Output: A Dataframe which has all the missing values imputed.
                                    On Failure: Raise Exception

                                    Written By: iNeuron Intelligence
                                    Version: 1.0
                                    Revisions: None
                 """
    self.logger_object.log(self.file_object, 'Entered the impute_missing_values method of the Preprocessor class')
    self.data = data
    self.cols_with_missing_values = cols_with_missing_values
    try:
        self.imputer = CategoricalImputer()
        for col in self.cols_with_missing_values:
            self.data[col] = self.imputer.fit_transform(self.data[col])
        self.logger_object.log(self.file_object,
                               'Imputing missing values Successful. Exited the impute_missing_values method of the Preprocessor class')
        return self.data
    except Exception as e:
        self.logger_object.log(self.file_object,
                               'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(
                                   e))
        self.logger_object.log(self.file_object,
                               'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
        raise Exception()