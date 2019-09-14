import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

import warnings
warnings.filterwarnings("ignore", module='astropy.io.votable.tree')

job = Gaia.launch_job_async("select top 100 * from gaiadr1.gaia_source order by source_id", dump_to_file=True)

print(job)

r = job.get_results()
print(r['solution_id'])