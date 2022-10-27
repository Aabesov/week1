QUESTIONS = {
    "expel air from the lungs with a sudden sharp sound.": [
        "a cough"
    ],
    "a pain in your head or face that's often described as a pressure that's throbbing, constant, sharp or dull. ": [
        "a headache"
    ],
    "an area of redness and spots on a person's skin, appearing especially as a result of allergy or illness.": [
        "a rash"
    ],
    "reddening, inflammation, and, in severe cases, blistering and peeling of the skin caused by overexposure to the ultraviolet rays of the sun.": [
        "sunborn"
    ],
    "make a sudden involuntary expulsion of air from the nose and mouth due to irritation of one's nostrils.": [
        "sneezing"
    ]
}

for question, alternative in QUESTIONS.items():
    correct_answer = alternative
    for alternative in sorted(alternative):
         print("Quiz")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print("The answer is", alternative, "not", answer)