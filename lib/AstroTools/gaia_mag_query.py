# module to query the ESA Gaia dataset 
# based on a certain image location
# with an image of certain size
# returning data with magnitude under a given limit
# ordered by magnitude in desc. order

from astroquery.gaia import Gaia


def launch_query(image_ctr_ra, image_ctr_dec, image_x_extent, image_y_extent, mag_ub):
    query = (  
        f"SELECT ra, dec, phot_g_mean_mag, r_est, teff_val, designation "
        f"FROM external.gaiadr2_geometric_distance "
        f"JOIN gaiadr2.gaia_source USING (source_id) "
        f"WHERE CONTAINS(POINT('ICRS', ra, dec), BOX('ICRS', {image_ctr_ra}, {image_ctr_dec}, {image_x_extent / 3600}, {image_y_extent / 3600})) = 1 "
        f"AND phot_g_mean_mag < {mag_ub} "
        f"ORDER BY phot_g_mean_mag DESC"
    )

    job = Gaia.launch_job_async(query, output_format="csv", dump_to_file=True)


# ------------------------------------------------------------------------------------------

# Gaia table headings:
# solution_id     - record of subsystem version for data generation/input data
# designation     - source designation derived from source_id, unique across data releases
# source_id       - id encoding rough position and other info, unique in a particular DR
# ra              - right ascension, icrs, degrees
# dec             - declination, ircs, degrees
# phot_g_mean_mag - mean magnitude in G band, float
# r_est           - estimated distance, parsec, from external.gaiadr2_geometric_distance