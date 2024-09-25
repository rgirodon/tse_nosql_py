from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")

with GraphDatabase.driver(URI, auth=AUTH) as driver:

    records, summary, keys = driver.execute_query("MATCH (p:Person) RETURN p.name AS name")

    for record in records:
        print(record["name"])

