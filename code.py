from experta import *
import random
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}
diseaseName=[]
priority_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map,priority_list

class generateFacts(KnowledgeEngine):
    """symptoms=""
    diseaseName=[]
    def __init__(self,symptoms,diseaseName):
        self.symptoms=symptoms
        self.diseaseName=diseaseName
        random.shuffle(priority_list)"""
    random.shuffle(priority_list)
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="diseaseNameKnown")

    @Rule(Fact(action="diseaseNameKnown"),NOT(Fact(headache=W())),salience=priority_list[0])
    def functName(self):
        # self.declare(Fact(headache=symptoms[diseaseName.index(strings)]))
        self.declare(Fact(headache=input("headache: ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(back_pain=W())), salience=priority_list[1])
    def funtName1(self):
        self.declare(Fact(back_pain=input("BackPain ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(chest_pain=W())), salience=priority_list[2])
    def funtName2(self):
        self.declare(Fact(chest_pain=input("ChestPain ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(cough=W())), salience=priority_list[3])
    def funtName3(self):
        self.declare(Fact(cough=input("Cough ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(fainting=W())), salience=priority_list[4])
    def funtName4(self):
        self.declare(Fact(fainting=input("Fainting ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(sore_throat=W())), salience=priority_list[5])
    def funtName5(self):
        self.declare(Fact(sore_throat=input("Sore Throat ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(fatigue=W())), salience=priority_list[6])
    def funtName6(self):
        self.declare(Fact(fatigue=input("Fatigue ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(restlessness=W())), salience=priority_list[7])
    def funtName7(self):
        self.declare(Fact(restlessness=input("Restlessness ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(low_body_temperature=W())), salience=priority_list[8])
    def funtName8(self):
        self.declare(Fact(low_body_temp=input("Low body temperature ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(fever=W())), salience=priority_list[9])
    def funtName9(self):
        self.declare(Fact(fever=input("Fever ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(sunken_eyes=W())), salience=priority_list[10])
    def funtName10(self):
        self.declare(Fact(sunken_eyes=input("Sunken Eyes ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(nausea=W())), salience=priority_list[11])
    def funtName11(self):
        self.declare(Fact(nausea=input("Nausea ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(blurred_vision=W())), salience=priority_list[12])
    def funtName12(self):
        self.declare(Fact(blurred_vision=input("Blurred vision ")));

    @Rule(Fact(action="diseaseNameKnown"), NOT(Fact(hallucination=W())), salience=priority_list[13])
    def funtName13(self):
        self.declare(Fact(hallucination=input("Hallucination ")));

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"),Fact(hallucination="no"))
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="yes"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="yes"))
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="yes"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_5(self):
        self.declare(Fact(disease="Sinusitus"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_6(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"), Fact(hallucination="no"))
    def disease_7(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_8(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_9(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="yes"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="yes"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(hallucination="no"))
    def disease_10(self):
        self.declare(Fact(disease="HypoThermia"))

    @Rule(Fact(action='diseaseNameKnown'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="yes"), Fact(hallucination="no"))
    def disease_11(self):
        self.declare(Fact(disease="HyperTension"))



    @Rule(Fact(action='diseaseNameKnown'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(hallucination=MATCH.hallucination),
          Fact(blurred_vision=MATCH.blurred_vision), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
                    low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
               fever, sunken_eyes, nausea, blurred_vision]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if (temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        print("Most probably it is: ",max_disease)
        print("Disease Description: ",d_desc_map[max_disease])
        print("Some Treatments: ",d_treatment_map[max_disease])



    @Rule(Fact(action='diseaseNameKnown'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("You are most probably suffering with %s\n" % (id_disease))
        print("Disease description :\n")
        print(disease_details + "\n")
        print("Medications: \n")
        print(treatments + "\n")


def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]
    
def editDistance(diseaseName,diseaseCause,symptoms):
    distanceFromSymptom=[]
    for string in diseaseCause:
        distanceFromSymptom.append(editDistDP(string,symptoms,len(string),len(symptoms)))
    minDistanceFromSymptoms=1000000000000000
    for individualDist in distanceFromSymptom:
        individualDist=int(individualDist)
        if(individualDist<minDistanceFromSymptoms):
            minDistanceFromSymptoms=individualDist
    ProbablyDisease=[]
    for distance in distanceFromSymptom:
        distance=int(distance)
        if(distance==minDistanceFromSymptoms):
            ProbablyDisease.append(diseaseName[diseaseCause.index(distance)])
    if(len(ProbablyDisease)==1):
        return ProbablyDisease[0]


def diseaseTest(symptoms):
    diseaseName=["Jaundice","Alzheimers","Arthritis","Tuberculosis","Asthma","Sinositis","Heart Disease","Diabetes","HyperThyroidism","Heat Stroke","Hypothermia","HyperTension"]
    diseaseCause=["00000010010100","00000001000001","01000010000000","00110000010000","00110001000000","10010100010000","00100000000100","00000010000110","00000010000100","10000000010100","00001000100000","10100011000010"]
    for string in diseaseCause:
        if(symptoms==string):
            print("You probably have :",diseaseName[diseaseCause.index(string)])
            break

def Questions():
    headache=input("headache: ")
    back_pain=input("Back Pain: ")
    chest_pain=input("Chest Pain: ")
    cough=input("cough: ")
    fainting=input("fainting: ")
    sore_throat=input("Sore throat: ")
    fatigue=input("fatigue: ")
    restlessness=input("restlessness: ")
    low_body_temprature=input("Low body temprature: ")
    fever=input("fever: ")
    sunken_eyes=input("Sunken Eyes: ")
    nausea=input("Nausea: ")
    blurred_vision=input("Blurred Vision: ")
    hallucination=input("Hallucination: ")
    symptoms=""


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        print(disease_s_data)
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]

def get_details(disease):
    return d_desc_map[disease]

def get_treatments(disease):
    return d_treatment_map[disease]

def openDiseaseList(diseaseName):
    for disease in diseaseName:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        #print(disease_s_data)
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

if __name__=="__main__":
    print("Welcome to your medical diagnosis:")
    print("Please enter your details below: ")
    print("Name:")
    Name=input()
    print("Age:")
    Age=input()
    while(True):
        try:
            Age=int(Age)
            break
        except:
            print("Age not an integer, please reenter")
            Age=input()
    print("Gender: M/F/O ")
    Gender=input()
    print("Please answer the following questions: yes/no")
    diseaseName = ["Jaundice", "Alzheimers", "Arthritis", "Tuberculosis", "Asthma", "Sinusitis", "Heart Disease",
                   "Diabetes", "Hyperthyroidism", "Heat Stroke", "Hypothermia", "Hypertension"]

    openDiseaseList(diseaseName)

    engine=generateFacts()
    while(True):
        engine.reset()
        engine.run()
        continueAsk=input("Want to diagnose another disease?")
        if(continueAsk=="no"):
            exit()
