import sqlite3
conn = sqlite3.connect("extreme_sports4.db")
#table_name = ('sportlist')
c = conn.cursor()
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='sportlist'""")
try:
    if c.fetchone()[0] == 1:
        pass
except:
    c.execute("""CREATE TABLE sportlist (
            sportname text,
            numberofplayers int,
            coolness real)""")
    print("created table")

c.execute("""INSERT INTO sportlist VALUES ("Extreme Balancing", 40, 100000000)""")
c.execute("""INSERT INTO sportlist VALUES ("Rugby", 250000, 5)""")
c.execute("""INSERT INTO sportlist VALUES ("Extreme Building", 50, 25)""")


c.execute("SELECT sportname FROM sportlist WHERE coolness > 0")
print(c.fetchone())

for row in c.execute("SELECT * FROM sportlist WHERE numberofplayers*coolness > 100000"):
    print(row)
