import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

# Blood Group
dat = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "AB+": 0,
    "AB-": 0,
    "O+": 0,
    "O-": 0,
    "rh-null": 0,
    "others": 0,
}

# number of diseases
disDat = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# diabetes
diabetes = {"1-15": 0, "16-30": 0, "31-45": 0, "46-60": 0, "60+": 0}

# body mass index
bmi_male = {}
bmi_female = {}

chronic = [
    "heart disease",
    "stroke",
    "lung cancer",
    "colorectal cancer",
    "depression",
    "type 2 diabetes",
    "arthritis",
    "osteoporosis",
    "asthma",
    "chronic obstructive pulmonary disease",
    "copd",
    "chronic kidney disease",
    "ckd",
    "oral disease"
]

df = pd.read_csv("event.csv")
for index, row in df.iterrows():
    disease_count = 0
    if row[5].lower() == "male":   
        bmi_male[row[7] / 100] = row[8]
    else:
        bmi_female[row[7] / 100] = row[8]
    for i in range(6):
        if str(row[13 + i]) != "-":
            if str(row[13 + i]).lower() in chronic:
                pass
            if str(row[13 + i]).lower() == "diabetes":
                for i in range(5):
                    if (15 * (i + 1) - row[4] < 15) and (row[4] - (15 * i) < 15):
                        if i == 0:
                            diabetes["1-15"] += 1
                        elif i == 1:
                            diabetes["16-30"] += 1
                        elif i == 2:
                            diabetes["31-45"] += 1
                        elif i == 3:
                            diabetes["46-60"] += 1
                        else:
                            diabetes["60+"] += 1
            disease_count += 1
    disDat[disease_count] += 1
    dat[row[6]] += 1

ax = plt.subplot()
plt.bar(diabetes.keys(), diabetes.values(), width=0.8)
sns.despine(left=True)
sns.set(style="whitegrid")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.grid(True, linestyle='-', which='major', color='grey', alpha=0.5)
plt.rcParams['figure.dpi'] = 240
save_path = "D:\Study\Healthcare record management\public\images\plot0.png"
plt.savefig(save_path)
plt.close()

ax = plt.subplot()
plt.bar(dat.keys(), dat.values(), width=0.8)
plt.grid(False)
sns.despine(left=True)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.grid(True, linestyle='-', which='major', color='grey', alpha=0.5)
# plt.rcParams['figure.dpi'] = 360
save_path = "D:\Study\Healthcare record management\public\images\plot1.png"
plt.savefig(save_path)
plt.close()

ax = plt.subplot()
plt.bar(disDat.keys(), disDat.values(), width=0.8)
plt.grid(False)
sns.despine(left=True)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.grid(True, linestyle='-', which='major', color='grey', alpha=0.5)
# plt.rcParams['figure.dpi'] = 360
save_path = "D:\Study\Healthcare record management\public\images\plot2.png"
plt.savefig(save_path)
plt.close()

explodeTuple = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02)
lab = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "rh-null", "others"]
# plt.rcParams['figure.dpi'] = 360
plt.pie(dat.values(), labels=lab, shadow=False, explode=explodeTuple, autopct="%1.2f%%")
save_path = "D:\Study\Healthcare record management\public\images\plot3.png"
plt.savefig(save_path)
plt.close()

img = plt.imread("public/images/BMI_chart1.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[36, 124, 1.4314, 2.009])
ax.set_aspect("auto")
plt.xlim([36, 124])
plt.ylim([1.4314, 2.009])
plt.grid(False)
sns.despine(left=True)
# plt.rcParams['figure.dpi'] = 360
plt.scatter(bmi_male.values(), bmi_male.keys(), s=2.5, color="blue")
plt.scatter(bmi_female.values(), bmi_female.keys(), s=2.5, color="crimson")
save_path = "D:\Study\Healthcare record management\public\images\plot4.png"
plt.savefig(save_path)
plt.close()
