# Author: Denis A. Engemann, email: denis.engemann@gmail.com
#
# License: BSD (3-clause)

__doc__ = """

Initialzie Query and Save Results
---------------------------------

This example deomstrates how to setup a query,
download PubMed records and save the results.
"""

print __doc__

import pymed as pm

# setup search
client = 'foo@bar.com'
term = 'diffusion kurtosis imaging'
pubmed_fields = 'all'
chunksize = 50

# get records
recs = pm.query_records(client=client, term=term, pubmed_fields=pubmed_fields,
                      chunksize=chunksize)

# look at result
print recs

# save records to disk
recs.save('my_records.json')
