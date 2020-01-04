from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='relentless',
                            base_numeric_id=4400,
                            name='Relentless',
                            role='heavy_express_3',
                            power=3850,
                            random_reverse=True,
                            gen=6,
                            intro_date_offset=-7, # let's be earlier on this to keep the mail up with the HSTs etc
                            fixed_run_cost_points=600, # give a serious malus to this one (balancing eh?)
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=95,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist