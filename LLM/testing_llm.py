import os
import pandas as pd
from openai import OpenAI


# Set up your OpenAI API credentials
client = OpenAI()

df = pd.read_csv("CA_data.csv")

data = df[["Description", "Vehicle Damage"]]
# remove the rows with missing values
print(data.shape)
data = data.dropna()

# drop the rows with "Not Available" in the Vehicle Damage column
data = data[data["Vehicle Damage"] != "Not Available"]
print(data.shape)




def model(description):

    prompt =f"""
            Given the description of a car accident, predict if the damage 
            the vehicle sustained by only returning ONLY the word None, Minor, or Moderate.
            Lean towards Minor if the damage is not severe, Moderate if the damage is severe.
            {description}
            """

    # Use the prompt in your OpenAI API calls
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a car accident damage predictor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2,
        temperature=0.8
    )
    return response.choices[0].message.content

# Test the model
# get the first 5 descriptions and their corresponding vehicle damage
descriptions = data["Description"]
vehicle_damage = data["Vehicle Damage"]
d = {}

correct, total = 0, 0
for description, damage in zip(descriptions, vehicle_damage):
    prediction = model(description)
    # print(f"Actual Vehicle Damage: {damage}")
    # print(f"Predicted Vehicle Damage: {prediction}")
    total += 1
    if prediction == damage:
        correct += 1
    else:
        d[(prediction, damage)] = d.get((prediction, damage), 0) + 1
    
    
print(d)
print(f"Accuracy: {correct/total}, Total: {total}, Correct: {correct}")

