import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

import warnings
warnings.filterwarnings("ignore", module='astropy.io.votable.tree')

mag_ub = 20.0                                       # magnitude upper bound for query

# how to import platesolved coords from another python file? Do everything in same script?
# degrees?
# TODO use SkyCoord
image_ctr_ra     = 200.0
image_ctr_dec    = -60.0

# image fov calculations - compare against platesolved data?
# image extents expressed as image size in a given axis in arcseconds
image_y_extent  = 100
image_x_extent  = 150

# query stringbuilding
query = (  
    f"SELECT TOP 100 ra, dec, phot_g_mean_mag, r_est, teff_val, designation "
    f"FROM external.gaiadr2_geometric_distance "
    f"JOIN gaiadr2.gaia_source USING (source_id) "
    f"WHERE CONTAINS(POINT('ICRS', ra, dec), BOX('ICRS', {image_ctr_ra}, {image_ctr_dec}, {image_x_extent * 3600}, {image_y_extent * 3600})) = 1 "
    f"AND phot_g_mean_mag < {mag_ub} "
    f"AND teff_val > 0"
)

test_query = (
    f"select top 100 * "
    f"from gaiadr1.gaia_source order by source_id"
)


# TODO order by mag

# Gaia final query - 
# SELECT ra, dec, phot_g_mean_mag, r_est, teff_val, designation \
# FROM external.gaiadr2_geometric_distance \
# JOIN gaiadr2.gaia_source USING (source_id) \
# WHERE CONTAINS (POINT('ICRS', ra, dec), BOX('ICRS', image_ctr_ra, image_ctr_dec, image_x_extent * 3600, image_y_extent * 3600)) = 1 \
# AND phot_g_mean_mag < mag_ub
# AND teff_val > 0

# Gaia test query - SELECT TOP 1000000000 (ra/360*24) AS RA, dec, r_est, teff_val, \
# phot_g_mean_mag, designation \
# FROM external.gaiadr2_geometric_distance \
# JOIN gaiadr2.gaia_source \
# USING (source_id) \
# WHERE phot_g_mean_mag > 16.95 AND phot_g_mean_mag < 17 AND teff_val > 0

# launch async job, file dump as .csv 
job = Gaia.launch_job_async(query, output_format="csv", dump_to_file=True)

print(job)

# ------------------------------------------------------------------------------------------

# Gaia table headings:
# solution_id     - record of subsystem version for data generation/input data
# designation     - source designation derived from source_id, unique across data releases
# source_id       - id encoding rough position and other info, unique in a particular DR
# ra              - right ascension, icrs, degrees
# dec             - declination, ircs, degrees
# phot_g_mean_mag - mean magnitude in G band, float
# teff_val        - stellar effective temperature, float, K
# r_est           - estimated distance, parsec, from extenral.gaiadr2_geometric_distance