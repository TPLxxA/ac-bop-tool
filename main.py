import json

def calculate_bop_factor(cars_data):
    # Sort the cars based on lap time in ascending order
    sorted_cars = sorted(cars_data, key=lambda car: car['laps'])

    # Calculate the average lap time of all cars
    total_cars = len(sorted_cars)
    total_lap_time = sum(car['laps'] for car in sorted_cars)
    average_lap_time = total_lap_time / total_cars

    # Calculate the BoP factor for each car based on lap time
    bop_factors = {}
    for index, car in enumerate(sorted_cars):
        factor = car['laps'] / average_lap_time
        bop_factors[car['model']] = factor

    return bop_factors

def suggest_restrictor_and_ballast(bop_factors):
    suggestions = {}
    for car, factor in bop_factors.items():
        # restrictor = 100 - max(min(int(factor * 100), 100), 0)
        restrictor = max(min(int((1 - factor) * 1500), 100), 0)
        ballast = max(min(int((1 - factor) * 2000), 1000), 0)
        suggestions[car] = {'restrictor': restrictor, 'ballast': ballast}
    return suggestions

# Open json file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Transform results.json data so that it can be used for BoP
def transform_results(json_data):
    # Remove unneeded data
    for item in json_data["players"]:
        item.pop('name', None)
        item.pop('skin', None)

    # Index cars so that we can map them to lap times
    for index, item in enumerate(json_data["players"]):
        item['index'] = index
        item['laps'] = []

    # Map lap times to car model
    for lap in json_data["sessions"][0]["laps"]:
        for car in json_data["players"]:
            if car['index'] == lap['car']:
                car['laps'].append(lap['time'])

    # Merge laptimes for identical models
    merged_data = []

    for car in json_data["players"]:
        # Check if model in list
        model_exists = False
        for item in merged_data:
            if item['model'] == car['car']:
                model_exists = True
                # If exists, add laptime to existing model
                item['laps'][0].extend(car['laps'])
                break

        if model_exists:
            pass
        # Else, create new model and add laptime
        else:
            merged_data.append({'model': car['car'], 'laps': [car['laps']]})
    
    # Get the 5 fastest times for each model
    for item in merged_data:
        item['laps'] = item['laps'][0]
        top_5 = sorted(item['laps'])[:5]
        # Average top 5 lap times
        avg_laptime = sum(top_5) / len(top_5)
        item['laps'] = avg_laptime

    return merged_data

# Load data
file_path = 'results.json'  # Replace with the path to your JSON file
json_data = load_json_file(file_path)
cars_data = transform_results(json_data)

# print results
bop_factors = calculate_bop_factor(cars_data)
print(bop_factors)
suggestons = suggest_restrictor_and_ballast(bop_factors)
print(suggestons)