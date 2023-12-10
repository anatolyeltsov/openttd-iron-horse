from train import MailHSTCarConsist, ExpressMailCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=16170,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=16180,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=16190,
        gen=6,
        subtype="U",
        intro_year_offset=-8,  # match to nimbus HST
        cab_id="nimbus",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
