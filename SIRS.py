import datetime
from organdysfunction import Mechanical_Ventilation, Vitals_Flowsheet_Six_HR
#<-------------------------SIRS Logic/Variables--------------------------------->#
# BPA Options = MD/APN/PA Documentation within 24 hours
SIRS_Temperature = "Cognitive Computing model "#!Ensure this only takes into acouunt the past 6 hours
SIRS_Heart_Rate = "Cognitive Computing model "#!Ensure this only takes into acouunt the past 6 hours
SIRS_Respiration = "Cognitive Computing model "#!Ensure this only takes into acouunt the past 6 hours
SIRS_WBC = "Cognitive Computing model"#!Ensure this only takes into acouunt the past 6 hours
department_obtained= "department patient was in when qualifying vital signs taken"
excluded_departments= ("Operating Room", "Interventional Radiology", "Cath Lab")#!Exclude code charting.
Ventilator_Flowsheet_Set_rate = "Ventilator set rate flowsheet row filed at the same time as the Respirations were >20"
Vitals_Flowsheet_RR= "If patient on ventilator needed to validate that patient RR> set RR"


def SIRS():
    SIRS_Score = 0
    if SIRS_Temperature and department_obtained != excluded_departments:
        SIRS_Score = SIRS_Score+1
    if SIRS_Heart_Rate and department_obtained != excluded_departments:
        SIRS_Score = SIRS_Score+1
    if SIRS_Respiration and department_obtained != excluded_departments:
        if Ventilator_Flowsheet_Set_rate and Ventilator_Flowsheet_Set_rate<Vitals_Flowsheet_RR:
            SIRS_Score = SIRS_Score+1
    if SIRS_WBC:
        SIRS_Score = SIRS_Score+1
    if SIRS_Score >= 2:
        return True, datetime.datetime
