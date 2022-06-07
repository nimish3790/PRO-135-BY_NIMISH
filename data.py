goldilock_planet_count = 0
for key, value in final_dict.items():
    if 'goldilock' in value:
        goldilock_planet_count += 1
print(goldilock_planet_count)

goldilock_gravity_type_count = 0
for key,value in final_dict.items():
    if 'goldilock' in value and 'planet_type' in value and 'gravity' in value:
        goldilock_gravity_type_count += 1
print(goldilock_gravity_type_count)

speed_planet_count = 0
for key, value in final_dict.items():
    if 'speed' in value:
        speed_planet_count += 1
print(speed_planet_count)

speed_goldilock_gravity_type_count = 0
for key,value in final_dict.items():
    if 'goldilock' in value and 'planet_type' in value and 'gravity' in value and 'speed' in value:
        speed_goldilock_gravity_type_count += 1
print(speed_goldilock_gravity_type_count)
