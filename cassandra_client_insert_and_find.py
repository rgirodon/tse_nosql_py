from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect('cycling')

rows = session.execute('SELECT lastname, nationality FROM cyclists')

for cyclist_row in rows:
    print(cyclist_row.lastname, cyclist_row.nationality)