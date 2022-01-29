import os
import random
import numpy as np


def get_random_name():
    first_letter = ["김", "이", "박", "최", "정", "사", "윤", "천", "부", "고"]
    middle_letter = ["민", "찬", "정", "영", "재", "준", "지", "태", "수", "원"]
    last_letter = ["영", "규", "현", "지", "국", "혁", "현", "정", "주", "웅", "아"]
    return (
        random.choice(first_letter) + 
        random.choice(middle_letter) + 
        random.choice(last_letter)
    )

def get_random_english_name():
    first_name = ["Jesse", "Jennifer", "James", "Bob", "Stuart", "Josh", "Werner"]
    last_name = ["Brown", "White", "Williams", "Davis", "Lopez", "Wilson", "Martin"]
    return (
        random.choice(first_name) +
        " " +
        random.choice(last_name)
    )

def get_random_gender():
    return int(random.random() > 0.5)

def get_random_height(gender, in_feet=False):
    if gender == 0:
        mean = 173
        std = 5
    else:
        mean = 160
        std = 3
    if in_feet:
        mean /= 30.48
        std /= 30.48
    return np.random.normal(mean, std)

def get_random_weight(gender):
    if gender == 0:
        mean = 70
        std = 10
    else:
        mean = 50
        std = 5
    return np.random.normal(mean, std)

def get_random_score():
    return min(max(int(np.random.normal(60, 10)), 0), 100)


if __name__ == "__main__":
    dir_name = "week6/data"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(os.path.join(dir_name, "kor_demographic.csv"), "w") as f:
        f.write("idx,name,gender,height,weight\n")
    with open(os.path.join(dir_name, "kor_score.csv"), "w") as f:
        f.write("idx,name,score\n")
    for i in range(1000):
        name = get_random_name()
        gender = get_random_gender()
        height = get_random_height(gender)
        weight = get_random_weight(gender)
        score = get_random_score()
        with open(os.path.join(dir_name, "kor_demographic.csv"), "a") as f:
            f.write(f"{i},{name},{gender},{height:.2f},{weight:.2f}\n")
        with open(os.path.join(dir_name, "kor_score.csv"), "a") as f:
            f.write(f"{i},{name},{score}\n")
    
    with open(os.path.join(dir_name, "us.csv"), "w") as f:
        f.write("idx,name,gender,height,weight,score\n")
    for i in range(1000):
        name = get_random_english_name()
        gender = get_random_gender()
        height = get_random_height(gender, in_feet=True)
        weight = get_random_weight(gender)
        score = get_random_score()
        with open(os.path.join(dir_name, "us.csv"), "a") as f:
            f.write(f"{i},{name},{gender},{height:.2f},{weight:.2f},{score}\n")
    pass