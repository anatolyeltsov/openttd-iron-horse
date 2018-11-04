from train import PassengerEngineMetroConsist, MetroUnit

consist = PassengerEngineMetroConsist(id='fleet',
                                      base_numeric_id=210,
                                      name='Fleet',
                                      role='pax_metro',
                                           power=1100,
                                      gen=3,
                                      sprites_complete=True)

# should be 4 short units, not 2 long but eh
consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=200,
                 chassis='railcar',
                 repeat=2)
