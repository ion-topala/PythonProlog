% Facts about medications
medication(ibuprofen, painRelief).
medication(acetaminophen, painRelief).
medication(aspirin, painRelief).
medication(lisinopril, bloodPressureRegulation).
medication(metoprolol, bloodPressureRegulation).
medication(atorvastatin, cholesterolRegulation).
medication(simvastatin, cholesterolRegulation).
medication(loratadine, allergyRelief).
medication(diphenhydramine, allergyRelief).

% Define the medication class for each medication
medication_class(aspirin, analgesics).
medication_class(ibuprofen, analgesics).
medication_class(ibuprofen, betaBlocker).
medication_class(acetaminophen, analgesics).
medication_class(lisinopril, antihypertensives).
medication_class(amlodipine, antihypertensives).
medication_class(fexofenadine, antihistamines).
medication_class(metoprolol, betaBlocker).
medication_class(atorvastatin, hmgCOA).
medication_class(simvastatin, hmgCOA).
medication_class(loratadine, antihistamines).
medication_class(diphenhydramine, antihistamines).


% Facts about medication side effects
side_effect(ibuprofen, stomachUpset).
side_effect(ibuprofen, nausea).
side_effect(ibuprofen, headache).
side_effect(acetaminophen, liverDamage).
side_effect(aspirin, stomachBleeding).
side_effect(aspirin, reducedBloodClotting).
side_effect(lisinopril, cough).
side_effect(metoprolol, fatigue).
side_effect(metoprolol, dizziness).
side_effect(atorvastatin, musclePain).
side_effect(simvastatin, musclePain).
side_effect(loratadine, dryMouth).
side_effect(loratadine, drowsiness).
side_effect(diphenhydramine, drowsiness).
side_effect(diphenhydramine, dryMouth).
side_effect(amlodipine, headache).
side_effect(amlodipine, nausea).
side_effect(amlodipine, stomachPain).
side_effect(fexofenadine, headachesPain).
side_effect(fexofenadine, dryMouth).
side_effect(fexofenadine, dizziness).



%interacts
interacts(ibuprofen, aspirin).
interacts(ibuprofen, lithium).
interacts(ibuprofen, methotrexate).
interacts(terbinafine, tramadol).
interacts(terbinafine, triazolam).
interacts(terbinafine, tarfarin).
interacts(terbinafine, tosiglitazone).
interacts(terbinafine, tllopurinol).
interacts(acetaminophen, warfarin).
interacts(acetaminophen, isoniazid).
interacts(acetaminophen, carbamazepine).
interacts(acetaminophen, rifampin).
interacts(aspirin, warfarin).
interacts(aspirin, heparin).
interacts(aspirin, clopidogrel).
interacts(lisinopril, diuretics).
interacts(metoprolol, digoxin).
interacts(metoprolol, clonidine).
interacts(atorvastatin, gemfibrozil).
interacts(atorvastatin, erythromycin).
interacts(simvastatin, erythromycin).
interacts(simvastatin, clarithromycin).
interacts(simvastatin, itraconazole).
interacts(loratadine, erythromycin).
interacts(loratadine, ketoconazole).
interacts(diphenhydramine, maois).


pregnancy_category(aspirin, d).
pregnancy_category(ibuprofen, c).
pregnancy_category(acetaminophen, c).
pregnancy_category(penicillin, b).
pregnancy_category(azithromycin, b).
pregnancy_category(metformin, b).
pregnancy_category(levothyroxine, a).
pregnancy_category(fluoxetine, c).
pregnancy_category(advil, c).
pregnancy_category(tylenol, b).
pregnancy_category(aleve, c).
pregnancy_category(claritin, b).
pregnancy_category(zantac, b).
pregnancy_category(ambien, c).
pregnancy_category(lipitor, x).


medication_for_symptom(fever, [acetaminophen, ibuprofen, aspirin]).
medication_for_symptom(headache, [acetaminophen, ibuprofen, aspirin]).
medication_for_symptom(pain, [acetaminophen, ibuprofen, aspirin]).
medication_for_symptom(hypertension, [lisinopril, metoprolol]).
medication_for_symptom(heartFailure, [lisinopril, metoprolol]).
medication_for_symptom(highCholesterol, [atorvastatin, simvastatin]).
medication_for_symptom(allergies, [loratadine, diphenhydramine]).
medication_for_symptom(insomnia, [diphenhydramine]).


% Base case: empty list of symptoms returns empty list of medications
medications_for_symptoms([], []).

% Recursive rule: return list of medications for each symptom in the list
medications_for_symptoms([Symptom|RestSymptoms], [Medication|RestMedications]) :-
    medication_for_symptom(Symptom, Medication),
    medications_for_symptoms(RestSymptoms, RestMedications).

%medicine which help to prevent a second heart-attack
is_beta_blocker(Medication) :-
    atom_concat(_, 'olol', Medication).


% Get the medication class for a medication
get_medication_class(Medication, MedicationClass) :-
    % Get the medication class for the medication
    medication_class(Medication, MedicationClass).


% Predicate that determines if a medication is safe for pregnancy
safe_for_pregnancy(Medication) :-
    pregnancy_category(Medication, Category),
    (Category = a; Category = b; Category = c),
    !.

is_pain_reliever(Medication) :- medication(Medication, painRelief).

can_cause_drowsiness(Medication) :- side_effect(Medication, drowsiness).

medication_for_condition(painRelief, [ibuprofen, acetaminophen, aspirin]).
medication_for_condition(bloodPressureRegulation, [lisinopril, metoprolol]).
medication_for_condition(cholesterolRegulation, [atorvastatin, simvastatin]).
medication_for_condition(allergyRelief, [loratadine, diphenhydramine]).

potential_side_effects(Medication, SideEffects) :- findall(SE, side_effect(Medication, SE), SideEffects).

interacts_with(D1, D2) :-
  interacts(D1, D2) ; interacts(D2, D1).


% Medication dosage recommendations
dosage_recommendation(ibuprofen, Age, Weight, Dosage) :-
    Age < 12,
    Dosage is Weight * 10.
dosage_recommendation(ibuprofen, Age, Weight, Dosage) :-
    Age >= 12,
    Dosage is Weight * 15.

dosage_recommendation(acetaminophen, Age, Weight, Dosage) :-
    Age < 6,
    Dosage is Weight * 10.
dosage_recommendation(acetaminophen, Age, Weight, Dosage) :-
    Age >= 6,
    Dosage is Weight * 15.

dosage_recommendation(amoxicillin, Weight, Dosage) :-
    Weight < 15,
    Dosage is 50.

dosage_recommendation(amoxicillin, Weight, Dosage) :-
    Weight > 15, Weight < 29,
    Dosage is 750.

dosage_recommendation(amoxicillin, Weight, Dosage) :-
    Weight < 30,
    Dosage is 1000.
