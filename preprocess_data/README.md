#### Columns removed and why

Columns that arent that useful: 'Lat1', 'Lat2', 'Lat3', 'Lng1', 'Lng2', 'Lng3', 
Columns that are redundant: Vehicle 1 Business Name, 
Too much missing data: 'Property Damage', 'Property Owner's Details
Mixed feelings: 'ZIPCODE of Accident', 'State of Accident', 'County of Accident', 'Location of Accident',

## Column Descriptions

### Vehicle 1 Year of Manufacturing
Indicates the year that Vehicle 1 was manufactured(normalized)

### Vehicle 1 was Moving
Indicates if the vehicle was moving

### Vehicle 1 was Stopped in Traffic
Indicates if the vehicle was stopped

### Number of Vehicles involved in Accident (w V1)
Indicates the number of vehicles in accident

### Vehicle Damage
Indicates the vehicle damage.\
{1: minor, 2: moderate, 3: None, 0: major}

### Roadway Conditions Vehicle 1
Indicating if there was a roadway condition. \
{0: no condition, 1: there was condition}

## One hot encoded columns: {1: yes, 0: no}

### Clear
Clear weather

### Cloudy
Cloudy weather

### Fog/Visibility/Dark
fog or visibility weather

### Raining
rain

### Lighting Vehicle 1_Dark
Dark outside

### Lighting Vehicle 1_Daylight
Light outside

### Road_Dry
Road was dry

### Road_Wet
Road was wet.

### Movement Preceding Collision Vehicle 1_Backing
Backing before crash

### Movement Preceding Collision Vehicle 1_Moving on Highway
moving on highway before crash

### Movement Preceding Collision Vehicle 1_Parking
Parking before crash

### Movement Preceding Collision Vehicle 1_Proceeding Straight
Going straight before crash

### Movement Preceding Collision Vehicle 1_Stopped
Stopped before getting crash

### Movement Preceding Collision Vehicle 1_Turning
Turning before crash

### External_factors
Indicating if there were external factors(bikers, pedestrian, scooters, etc)

### Manufacturer_apple
apple made this car

### Manufacturer_cruise
cruise made this car

### Manufacturer_google
google made this car

### Manufacturer_other
other? made this car(grouped values since they were too little)

### Manufacturer_waymo
waymo made this car

### Manufacturer_zoox
zoox made this car

### Rear Damage
Damage on the rear 

### Front Damage
Damage on the Front

### Right Side Damage
Damage on the Right Side

### Left Side Damage
Damage on the Left Side

### Inside Damage
Damage on the Inside??

### accident_Year
Year of the accident(normalized)

### accident_Month
Month of the accident(normalized)

### accident_Day
Day of the accident(normalized)

### accident_Day_of_week
day of the week(monday, tuesday etc) of the accident(normalized)

### accident_Hour
Hour of the accident(normalized)

### Chevrolet Bolt
Make + model

### Chrysler Pacifica
Make + model

### Cruise AV
Make + model

### Jaguar I-Pace
Make + model

### Lexus RX 450h
Make + model

### Toyota Highlander
Make + model

### other_makeModel
Make + model

### Vehicle1_is_Other
no clue what kind of car it is

### Vehicle1_is_SUV
SUV

### Vehicle1_is_Sedan
Sedan

### Vehicle1_is_Van
Van

### area_of_accident_SF Bay Area
Accident happened in SF bay area

### area_of_accident_SoCal
Accident happened in Socal

### area_of_accident_South Bay
Accident happened in South bay

### Car Mode_Autonomous Mode
Autonomous mode

### Car Mode_Conventional Mode
Convention Mode

### Car Mode_autonomous Mode
huh(FIX THIS LATER)

### Collision_Broadside
Type of collision

### Collision_Head-On
Type of collision

### Collision_Hit Object
Type of collision

### Collision_Other
Type of collision

### Collision_Rear End
Type of collision

### Collision_Side Swipe
Type of collision