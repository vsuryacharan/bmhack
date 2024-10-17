from django.shortcuts import render
from .forms import SymptomForm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and prepare the data, then train the model
def train_model():
    # Load the dataset
    data = pd.read_csv('symptoms_data.csv')

    # Fill missing values
    data.fillna('No Symptom', inplace=True)

    # One-hot encode the data
    data_encoded = pd.get_dummies(data, columns=data.columns[1:], drop_first=True)

    # Split data into features (X) and target (y)
    X = data_encoded.drop('Disease', axis=1)
    y = data_encoded['Disease']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

# Initialize the model at startup
rf_model = train_model()

# List of all symptoms used for encoding
ALL_SYMPTOMS = [
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

def predict_disease(symptoms_selected):
    # Map selected symptoms to their encoded format (e.g., 'Symptom_1_Fever')
    example_symptoms = {}
    for i, symptom in enumerate(symptoms_selected, start=1):
        if i <= 7:  # We assume max 7 symptoms in dataset; adjust if different
            example_symptoms[f'Symptom_{i}_{symptom}'] = 1

    # Convert to DataFrame and reindex to match training features
    example_df = pd.DataFrame([example_symptoms])
    training_features = rf_model.feature_names_in_  # Features used in model training
    example_df = example_df.reindex(columns=training_features, fill_value=0)

    # Predict using the model
    prediction = rf_model.predict(example_df)
    
    return prediction[0]


def symptom_check(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms_selected = form.cleaned_data['symptoms']
            predicted_disease = predict_disease(symptoms_selected)
            return render(request, 'app/result.html', {'disease': predicted_disease})
    else:
        form = SymptomForm()

    return render(request, 'app/form.html', {'form': form}) 
