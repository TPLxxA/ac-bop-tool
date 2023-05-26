# ac-bop-tool
A tool to calculate BoP for any GT3 grid on any track. It's about 95% ChatGPT-generated but it works

# Usage
- Start a race weekend with the grid you want to BoP. Make sure that the strength of each AI driver is at 100%, and that there's no variation in aggression.
- Simulate a 20-30 minute qualifying session (longer is more accurate, but obviously takes longer). Do not drive yourself
- Quit the weekend
- Find the results file that CM has generated (In CM go to Results, find your session and click on View in Exlporer. It should be in: ...\AppData\Local\AcTools Content Manager\Progress\Sessions)
- Create a new file called results.json and put it in the same folder as this script
- Run the script
- Apply the suggested restrictor and ballast settings to each car
- Repeat from step 1 until you're happy. After the second qualifying simulation, ADD the suggested ballast and restrictor to the restricted values, do not replace with the new suggested values.
- It should take around 3 sessions to get a fairly balanced grid

# How it works
The script takes data from a qualifying session. It grabs the top 5 fastest laps by any model (these can be 5 laps by the same driver, or 5 laps by different drivers in the same car), then takes the average of those 5 laps.
A BoP factor is calculated so that the length of the track does not matter. Based on this BoP factor, a suggested restrictor and ballast is calculated with a formula that I don't understand.

# Limitations
- UX is terrible, takes a developer to understand
- Still takes forever
- Only tested for GT3 cars, but should theoratically work for any class
- Only suggests additions to restrictor and ballast, so if a car is too slow because if its suggestions, you have to manually take some off
- Only takes into account lap times, so a disbalance may still exist with different tyres, fuel capacity etc.
