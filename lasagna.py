"""class Lasa:
    EXPECTED_BAKE_TIME = 40
    print(EXPECTED_BAKE_TIME)
    def bake_time_remaining(elapsed_baked_time):
        return EXPECTED_BAKE_TIME - elapsed_baked_time

    def preparation_time_in_minutes(number_of_layers):
        each_layer_time_in_minutes=2
        return each_layer_time_in_minutes*number_of_layers
    bake_time_remaining(int(input("Enter how long dish been cookin")))
    preparation_time_in_minutes(int(input("Enter Number of layers you want in your Lasanga")))

class Lasa2(Lasa):
    def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
        return preparation_time_in_minutes(number_of_layers)+ elapsed_baked_time

    
    elapsed_time_in_minutes()"""


EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)
def bake_time_remaining(elapsed_baked_time):
    print("EXPECTED_BAKE_TIME - elapsed_baked_time")
    return EXPECTED_BAKE_TIME - elapsed_baked_time
    

def preparation_time_in_minutes(number_of_layers):
    each_layer_time_in_minutes=2
    print(each_layer_time_in_minutes*number_of_layers)
    return each_layer_time_in_minutes*number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    print(preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time)
    return preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time

bake_time_remaining(int(input("Enter how long dish been cookin")))
preparation_time_in_minutes(int(input("Enter Number of layers you want in your Lasanga")))
elapsed_time_in_minutes(3,12)