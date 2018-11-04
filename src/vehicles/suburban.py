from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='suburban',
                        base_numeric_id=500,
                        name='2-6-2 Suburban',
                        role='branch_express',
                        power=650,
                        tractive_effort_coefficient=0.2,
                        random_reverse=True,
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=57,
                 vehicle_length=6,
                 spriterow_num=0)
