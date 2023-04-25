names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
         ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
         ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
         ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
         ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
         ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
         ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
         ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
         ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
         ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
         ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
         ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
         ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
         ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
         ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]
def conc(*x):
    for i in x:
        return i[0] + ' ' + i[1]
    
res = list(map(conc, names))
print(res)