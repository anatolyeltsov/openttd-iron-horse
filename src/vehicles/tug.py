from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='tug',
                        base_numeric_id=220,
                        name='Tug',
                        power=3600,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        speed=90,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        gen=5)

consist.add_unit(type=DieselEngineUnit,
                 weight=125,
                 vehicle_length=8,
                 spriterow_num=0)

