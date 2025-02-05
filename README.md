## Diabetes Prediction

# Uvod

Ova aplikacije je nastala idejom, poznavajući osobe koje imaju dijabetes, te mi je izgledalo veoma idealno da razvijem ovog agenta za predikciju. 
Sama aplikacija neće vršiti dijagnozu, već se samo vršiti predikciju, da li osoba koja unosi svoje podatke ima predispozicije za dijabetes, ili ne.

# Korištene tehnologije

Korištene tehnologije koje su korištene u ovoj aplikaciji se sastoje od:
- HTML/CSS
- JavaScript
- Python
- FastAPI

# Struktura aplikacije

- Frontend dio aplikacije → index.html
- Backend dio aplikacije → app.py
- Dataset → diabetes_dataset.csv

# Ključni parametri

- Broj trudnoća
- Glukoza
- Krvni pritisak
- Debljina kože
- Inzulin
- BMI
- Genetska predispozicija
- Godine

Ovi parametri se koriste na osnovu medicinske literature, kao parametri koji se mogu koristiti pri predikciji same bolesti.

# Algoritam

Algoritam koji se koristi za ovaj projekat je Random Forest Classifier. Random Forest Classifier stvara skup stabala odlučivanja iz nasumično odabranog podskupa skupa za obuku. To je skup stabala odlučivanja iz nasumično odabranog podskupa skupa za obuku, a zatim prikuplja glasove iz različitih stabala odlučivanja kako bi se odlučilo o konačnom predviđanju. 
Dodatno, Random Forest Classifier može se nositi s zadacima klasifikacije i regresije, a njegova sposobnost pružanja rezultata važnosti značajki čini ga vrijednim alatom za razumijevanje značaja različitih varijabli u skupu podataka.
Rezultati su pokazali da je model ranog otkrivanja dijabetesa koji koristi algoritam Random Forest dao točnost od 87%.

# Python biblioteke

- os
- Pandas
- Numpy
- FastAPI
- Pydantic
- Sklearn 

# Reference 

- https://archive.ics.uci.edu/dataset/34/diabetes 
- https://www.sciencedirect.com/science/article/pii/S1877050920300557 

