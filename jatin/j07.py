class vehicle : 
    pass 
class land_vehicle (vehicle ) :
    pass    
class tracked_vehicle (land_vehicle) :
    pass

my_vehicle = vehicle()
my_land_vehicle = land_vehicle()
my_tracked_vehicle = tracked_vehicle()

for obj in (my_vehicle, my_land_vehicle, my_tracked_vehicle) :
    for cls in (vehicle, land_vehicle, tracked_vehicle) :
        print(isinstance(obj, cls), end = "\t")
    print()