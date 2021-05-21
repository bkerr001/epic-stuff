import datetime
#<-------------------Suspected Infection Logic/Variables------------------------>#
    # If infection documented as present on admission, admission time will be used for infection.
    # BPA Options - Infection was suspected but has been ruled out (MUST BE WITIHIN 6 HOURS and by(MD), INFECTION IS VIRAL,
    # ABX_Administered= "if antibiotic administered within 6 hours"
ABX_Prompt = "if physician selected'YES' to suspected infection when ordering antibiotics "
Problem_List = "if any infectious etioilogy placed on problem list(See Appendix A)"
Nursing_Sepsis_Screen = "Sepsis screen in ED, ICU stating that infection is present"
ICD_Infection = "list of infection codes (See Appendex A)"
Admit_Diagnosis = "Admission Diagnosis, primary problem is of infectious etiology"
ED_Dianosis = "EDMD Diagnosis, primary problem is of infectious etiology"


def Infection_Present(ABX_Prompt, Nursing_Sepsis_Screen, ICD_Infection, Problem_List):
    if ABX_Prompt or Nursing_Sepsis_Screen or ICD_Infection or Problem_List:
        return True, datetime.datetime








"Look Further into abx administration vs the order for an antibiotic for the purpose of suspected infection"
# The following is a list of conditions commonly associated with severe sepsis that are considered infections.
# (This is not an all-inclusive list.)
# Abscess
# Acute abdomen
# Acute abdominal infection
# Blood stream catheter infection
# Bone/joint infection
# C. difficile (C-diff)
# Chronic obstructive pulmonary disease (COPD) acute exacerbation
# Endocarditis
# Gangrene
# Implantable device infection
# Infection
# Specifications Manual for National Hospital Inpatient Quality Measures
# Discharges 07-01-21 (3Q21) through 12-31-21 (4Q21) 1-133
# Infectious
# Meningitis
# Necrosis
# Necrotic/ischemic/infarcted bowel
# Pelvic Inflammatory Disease
# Perforated bowel
# Pneumonia, empyema
# Purulence/pus
# Sepsis
# Septic
# Skin/soft tissue infection
# Suspect infection, source unknown
# Urosepsis, urinary tract infection
# Wound infection