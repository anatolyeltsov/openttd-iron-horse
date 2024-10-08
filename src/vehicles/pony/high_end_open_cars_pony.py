from train import OpenCarHighEndConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23590,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23600,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23610,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23620,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23640,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_16px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23650,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarHighEndConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
