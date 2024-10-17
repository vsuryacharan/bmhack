from django import forms

# List of unique symptoms
SYMPTOMS = [
    'Fever', 'Nasal Discharge', 'Loss of appetite', 'Weight Loss', 'Lameness', 
    'Breathing Difficulty', 'Swollen Lymph nodes', 'Lethargy', 'Depression', 
    'Coughing', 'Diarrhea', 'Seizures', 'Vomiting', 'Eating less than usual', 
    'Excessive Salivation', 'Redness around Eye area', 'Severe Dehydration', 
    'Pain', 'Discomfort', 'Sepsis', 'WeightLoss', 'Tender abdomen', 
    'Increased drinking and urination', 'Bloated Stomach', 'Yellow gums', 
    'Constipation', 'Paralysis', 'Wrinkled forehead', 'Continuously erect and stiff ears', 
    'Grinning appearance', 'Stiff and hard tail', 'Stiffness of muscles', 'Acute blindness', 
    'Blood in urine', 'Hunger', 'Cataracts', 'Losing sight', 'Glucose in urine', 
    'Burping', 'Blood in stools', 'Passing gases', 'Eating grass', 'Scratching', 
    'Licking', 'Itchy skin', 'Redness of skin', 'Face rubbing', 'Loss of Fur', 
    'Swelling of gum', 'Redness of gum', 'Receding gum', 'Bleeding of gum', 
    'Plaque', 'Bad breath', 'Tartar', 'Lumps', 'Swelling', 'Red bumps', 
    'Scabs', 'Irritation', 'Dry Skin', 'Fur loss', 'Red patches', 
    'Heart Complication', 'Weakness', 'Aggression', 'Pale gums', 
    'Coma', 'Collapse', 'Abdominal pain', 'Difficulty Urinating', 'Dandruff', 
    'Anorexia', 'Blindness', 'Excess jaw tone', 'Urine infection', 
    'Lack of energy', 'Smelly', 'Neurological Disorders', 'Eye Discharge', 
    'Loss of Consciousness', 'Enlarged Liver', 'Lethargy', 'Purging', 
    'Bloody discharge', 'Wounds'
]

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=[(symptom, symptom) for symptom in SYMPTOMS],
        widget=forms.CheckboxSelectMultiple,
        label="Select Symptoms"
    )
