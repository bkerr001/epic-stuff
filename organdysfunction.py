
# Output Variables


Severe_Sepsis_Present_Time = "as defined by cms, see function below, all three items must be met within 6 hours of eachother"
Septic_Shock_Present_Time = "as defined by cms, see function below"
Infection_Present = "See Infection_Present below"
Organ_Dysfunction = "See organ_dysfunction below"
SIRS_Criteria = "As defined by CMS, two must be present, data from cognitive computing model"
Now = "Now DateTime"
BPA_Exclusion_All = "Normal for that patient | Due to a chronic condition | Due to a medication | Other: must comment"

## If any of the functions below return True, Organ Dysfunction returns True
def Organ_Dysfunction():    
    if Hypotension or Acute_Respiratory_Failure or Creatinine_Elevated or Bilirubin or Platelet or Lactate or INR_PTT :
        return True 
    else: 
        return False


##<-------------------------------Hypotension----------------------------------->#
# Vital signs filed from the current time, minus 6 hours"
## Hypotension Variables
Vitals = (MAP, SBP, Time)  # last 6 hours of vital signs
MAP = "Mean Arterial Pressure"
SBP = "Systolic Blood Pressure"
Time = "Time Vitals were taken"
Vitals_Location = "Department patient in when vitals were taken"
Vitals_Position = "Patient position while blood pressure taken, often null unless specified"
Hypotension_BPA_Exclusion = '"Orthostatic Vital Signs" | MD to document drop in blood pressure by 40mm/hg not due to sepsis" '
## Hypotension Function: 
    ##Evaluate all documented vital signs in the past 6 hours
        ## Exclude: 
        ## orthostatic vitals (vitals position = standing)
        ##Vitals if they were part of code documentation, sedation documentation (from narrator) but include Rapid Response Vitals
        ## the patients department at the time of obtaining was:
            ## Dialysis, Interventional Radiology, Operating Room, during any procedure requiring sedation.
            
    ##1)Any single blood pressure where SBP < 90 or MAP < 65 within the past 6 hours
    ##2)A drop in systolic blood pressure by 40mmhg within the last 6 hours 
        ##Logically : a pair of systolic blood pressures that are > 40mmhg apart where the difference in time between the pressures is less than 3 hours
        ##  and the first blood pressure is higher than the second.  
        
    ## Acceptable inclusion criteria (if docmented properly and in a timely manner are )
def Hypotension(Vitals):
    
    if Time_diff(SBP_Diff(Vitals)):
            return True
    for vitals in Vitals:
        if MAP < 60 or SBP < 90:
            if Vitals_Location != "Dialysis" or Vitals_Location != "Operating Room":
                if Vitals_Position != "Standing":
                    return True
    else:
        return False, Vitals

diff=40
def SBP_Diff(Vitals, diff):## create pairs of vitals where the sbp difference > 40
    return [(e1, e2) for e1 in Vitals for e2 in Vitals if (e1[0]-e2[0]>diff)]

def Time_diff(pairs):
    if pairs:    
        for pair in pairs:
            if pair[1][3]-pair[0][3]<10800 :
                 return True ## exit with True if one of the pairs meets criteria of SBP1>SBP2 and time differnce between the two is <3 hours.
    else: return False  
                

##<-----------------------Acute Respiratory Failure---------------------------->#
# This is going to fire alot, optional= all indication to CAPAP/BIPAP Order. This could get messy as RT often places the orders.
Respiratory_BPA_Exclusion = "NIPPV for Obstructive Sleep Apnea | Other Reason for new Mechnical Ventilation/NIPPV"
# Order vs Documented vs both.
Mechanical_Ventilation = " New indication for mechanical ventilation, infection related"
#  Order vs Documented vs both.
Non_Invasive_Ventilation = "New indication for NIPPV, infectious related"

def Acute_Respiratory_Failure(Mechanical_Ventilation, Non_Invasive_Ventilation):
    if Mechanical_Ventilation or Non_Invasive_Ventilation:
        return True
    return False

##<-----------------------Creatinine >2.0---------------------------->#
Creatinine_Elevated_BPA_Eclusion = "ESRD on Hemodialysis or Peritoneal Dialysis | CKD with <0.5mg/dl rise in Creatinine from baseline "
ESRD_on_Dialysis = "ESRD on dialysis in problem list, coded dianoses"
Creatinine_Level = "Creatinine level that resulted in the last 6 hours"

def Creatinine_Elevated(ESRD_on_Dialysis, Creatinine_Level):
    if Creatinine_Elevated and not ESRD_on_Dialysis:
        return True
    else:
        return False

##<---------------------------Bilirubin > 2, ---------------------------->#
Bilirubin_Level = "Bilirubin Level that resulted in the last 6 hours"

def Bilirubin(Bilirubin_Level):
    if Bilirubin_Level > 2:
        return True
    else: 
        return False
##<-----------------------------PLT <100,000-------------------------------->#
Platelet_Level = "Platelet Level that resulted in the last 6 hours"

def Platelet(Platelet_Level):
    if Platelet_Level > 2:
        return True
    else: 
        return False
##<-----------------------------Lactate >2-------------------------------->#
Lactate_Level = "Lactate Level that resulted in the last 6 hours"
Lactate_BPA_Exclusion_Critera = "Recent Seizure | Recent Cardiac Arrest"

def Lactate(Lactate_Level):
    if Lactate_Level > 2:
        return True
    else:
        return False
##<-----------------------------INR/aPTT-------------------------------->#
INR_Level = "INR Level that resulted in the last 6 hours"
aPTT_Level = "aPTT Level that resulted in the last 6 hours"
Anticoagulation_Meds = "Medical record documentation of medication administered from the list below"
INR_PTT_BPA_Exclusion = ""

def INR_PTT(INR_Level, aPTT_Level):
    if INR_Level > 1.5 or aPTT_Level > 60:
        if not Anticoagulation_Meds:
            return True
    return False
##<-----------------------------Urine Output-------------------------------->#
    #!flowsheet data revealing urine ouput < 0.5ml./kg/hr
    #!hours must be consecutive, order must be in place for hourly intake and output
    #! ICU ONLY      

## Anticoagulation Medicaltions:
## Heparin
## Heparin
## Edoxaban
## Savaysa
## Desirudin
## Iprivask
## Dabigatran etexilate
## Pradaxa
## Rivaroxaban
## Xarelto
## Apixaban
## Eliquis
## Argatroban
## Argatroban
## Bivalirudin
## Angiomax
## Fondaparinux
## Arixtra
## Warfarin
## Coumadin
