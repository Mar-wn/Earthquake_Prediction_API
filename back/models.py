from pydantic import BaseModel

class Donor(BaseModel):
    
    months_since_first: float
    months_since_last: float
    number_of_donations: int
    total_blood_donated: float
    
    def print_data(self):
        
        print(f'months_since_first: {self.months_since_first}', 
              f'months_since_last: {self.months_since_last}',
              f'number_of_donations: {self.number_of_donations}',
              f'total_blood_donated: {self.total_blood_donated}',
              sep= '\n')
        
    def transform(self, min_max_scaler):
        
        # scale features

        new_data_input = min_max_scaler.transform([[self.months_since_first,
                                                   self.months_since_last,
                                                   self.number_of_donations]]).tolist()
        # convert blood to liter
        
        new_data_input[0].append(self.total_blood_donated / 1000)
        
        
        return(new_data_input)
