import sqlite3
conn = sqlite3.connect("extreme_sports.db")

#cursor objects allow you to execute commands
c = conn.cursor()
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='sportlist'""")

#if the table doesn't exist create a new one
try:
    #tests to see if any tables exist
    if c.fetchone()[0] == 1:
        pass
    #if none exist, create one
except:
    c.execute("""CREATE TABLE sportlist (
            sportname text,
            numberofplayers int,
            coolness real)""")
    print("created table")

#insert 3 different items into the table
c.execute("""INSERT INTO sportlist VALUES ("Extreme Balancing", 40, 100000000)""")
c.execute("""INSERT INTO sportlist VALUES ("Rugby", 250000, 5)""")
c.execute("""INSERT INTO sportlist VALUES ("Extreme Building", 50, 25)""")

#return the first sport name with positive coolness
c.execute("SELECT sportname FROM sportlist WHERE coolness > 0")
print(c.fetchone())

#print all rows where the product of numplayers and coolness is over 10^5
for row in c.execute("SELECT * FROM sportlist WHERE numberofplayers*coolness > 100000"):
    print(row)
