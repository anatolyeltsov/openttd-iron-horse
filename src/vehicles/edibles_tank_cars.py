from train import EdiblesTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 or 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3030,
                                    gen=2,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1190,
                                    gen=3,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2990,
                                    gen=4,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3050,
                                    gen=5,
                                    subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2090,
                                    gen=6,
                                    subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

