# -*- coding: utf-8 -*-

##########################
# AUTHOR : AMAN SINGHAL
##########################

# our modules
from .api_calls import weather, timezone, translation, pdfapi

# This class is used to define switch case for API calling
class ApiAdapter:
    # Here we are creating a switch case for each API which we have integrated
    def __init__(self, api_parameters):
        self.api_parameters = api_parameters

    # Function to call api. This function takes api name as a parameter and activates the switch case to call an API
    def call_api(self, api_name):
        if api_name == "weatherapi":
            return weather.weather(self.api_parameters)
        elif api_name == "timezoneapi":
            return timezone.timezone(self.api_parameters)
        elif api_name == "translationapi":
            return translation.translation(self.api_parameters)
        elif api_name == 'pdfapi':
            return pdfapi.pdfapi(self.api_parameters)
            