import mysql.connector

#test

def home():
    print("\t\t\t\t\t\t****************************")
    print("\t\t\t\t\t\tElection Registration System")
    print("\t\t\t\t\t\t****************************")

    print("\n\t\t 1) Citizens \n\t\t 2) Parties \n\t\t 3) Candidates \n\t\t 4) exit \n")
    option = input("Enter your option : ")

    return option


def create_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS election")


def create_citizen_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS citizens 
                      (nic VARCHAR(255), 
                       name VARCHAR(255) PRIMARY KEY, 
                       age INT, 
                       state_province VARCHAR(255))''')


def create_candidates_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidates
                          (nic VARCHAR(255) PRIMARY KEY,
                           party VARCHAR(255),
                           education VARCHAR(255))''')


class Citizen:
    def __init__(self, nic, name, age, state_province):
        self.nic = nic
        self.name = name
        self.age = age
        self.state_province = state_province

    def __str__(self):
        return f"{self.nic} (NIC: {self.name}, Age: {self.age}, State/Province: {self.state_province})"

    def is_eligible_to_vote(self):
        return self.age > 18


class Candidate(Citizen):
    def __init__(self, nic, name, age, state_province, party, education):
        super().__init__(nic, name, age, state_province)
        self.party = party
        self.education = education


def get_citizen_details():
    nic = input("Enter NIC: ")
    name = input("Enter name: ")
    state_province = input("Enter state/province: ")
    age = int(input("Enter age: "))

    return nic, name, state_province, age


def get_candidate_details():

    party = input("enter party name: ")
    education = input("enter education qualifications: ")
    return party, education


def add_citizen_to_db(citizen, cursor):
    sql = '''INSERT INTO citizens (nic, name, age, state_province)
             VALUES (%s, %s, %s, %s)'''
    values = (citizen.nic, citizen.name, citizen.age, citizen.state_province)
    cursor.execute(sql, values)


def check_citizen_eligible(citizen, cursor, cnx):

    if citizen.is_eligible_to_vote():
        add_citizen_to_db(citizen, cursor)
        cnx.commit()
        print(f"citizen {citizen.name} added to the database.")
    else:
        print(f"Sorry, {citizen.name} is not eligible to vote.")


def create_party_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS parties
                       (name VARCHAR (255) PRIMARY KEY,
                        symbol_name VARCHAR(255))''')


def get_party_details():
    name = input("Enter name: ")
    symbol_name = input("Enter symbol: ")
    return name, symbol_name


class Party:
    def __init__(self, name, symbol_name):
        self.name = name
        self.symbol_name = symbol_name

def add_party_to_db(party, cursor):
    sql = '''INSERT INTO parties (name, symbol_name)
                 VALUES (%s, %s)'''
    values = (party.name, party.symbol_name)
    cursor.execute(sql, values)



def check_party_table(cursor):
    cursor.execute("SELECT COUNT(*) FROM parties")
    party_count = cursor.fetchone()[0]
    if party_count == 0:
        print("It's not parties registered in system.")
        home()


def show_party_details(cursor):
    cursor.execute("SELECT * FROM parties")
    parties = cursor.fetchall()

    if not parties:
        print("No party details found.")
    else:
        print("Party details:")
        for party in parties:
            name, symbol_name = party
            print(f"Name: {name}, Symbol: {symbol_name}")


def check_nic_in_citizens_table(nic, cursor):
    cursor.execute("SELECT COUNT(*) FROM citizens WHERE nic = %s", (nic,))
    count = cursor.fetchone()[0]
    return count > 0


def add_candidate_to_db(candidate, cursor):
    sql = '''INSERT INTO candidates (nic, party, education)
             VALUES (%s, %s, %s)'''
    values = (candidate.nic, candidate.party, candidate.education)
    cursor.execute(sql, values)


def show_citizen_details(cursor):
    cursor.execute("SELECT * FROM citizens")
    citizens = cursor.fetchall()

    if not citizens:
        print("No citizen details found.")
    else:
        print("Citizen details:")
        for citizen in citizens:
            nic, name, age, state_province = citizen
            print(f"NIC: {nic}, Name: {name}, Age: {age}, State/Province: {state_province}")

def get_citizen_option():

    print("\n\t\t\t\t\t\t____________________________________")
    print("\t\t\t\t\t\tYou are in the Citizens Manage System")
    print("\t\t\t\t\t\t____________________________________")
    print("\n\t\t 1) Add Citizen details \n\t\t 2) Show Citizens details\n")

    choose = input("Enter your option : ")
    print("\n")
    return choose

def get_candidate_option():
    print("\n\t\t\t\t\t\t______________________________________")
    print("\t\t\t\t\t\tYou are in the Candidates Manage System")
    print("\t\t\t\t\t\t______________________________________")
    print("\n\t\t 1) Add Candidate details \n\t\t 2) Show Candidates details\n")

    choose = input("Enter your option : ")
    print("\n")
    return choose


def get_party_option():
    print("\n\t\t\t\t\t\t____________________________________")
    print("\t\t\t\t\t\tYou are in the Parties Manage System")
    print("\t\t\t\t\t\t____________________________________")
    print("\n\t\t 1) Add Party details \n\t\t 2) Show Parties details\n")

    choose = input("Enter your option : ")
    print("\n")
    return choose


def show_party_details(cursor):
    cursor.execute("SELECT * FROM parties")
    parties = cursor.fetchall()

    if not parties:
        print("No party details found.")
    else:
        print("Party details:")
        for party in parties:
            name, symbol_name = party
            print(f"Name: {name}, Symbol: {symbol_name}")

def show_candidate_details(cursor):
    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    if not candidates:
        print("No candidate details found.")
    else:
        print("Candidate details:")
        for candidate in candidates:
            nic, name, age, state_province, party, education = candidate
            print(f"NIC: {nic}, Name: {name}, Age: {age}, State/Province: {state_province}, Party: {party}, Education: {education}")



def main():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
    )
    cursor = cnx.cursor()

    create_database(cursor)

    cnx.database = 'election'




    while True:

        option = home()


        if option == '4':
            break

        if option == '1':

            create_citizen_table(cursor)

            choose = get_citizen_option()

            if choose == '2':

                show_citizen_details(cursor)

            elif choose == '1':

                nic, name, state_province, age = get_citizen_details()

                citizen = Citizen(nic, name, age, state_province)

                check_citizen_eligible(citizen, cursor, cnx)

            else:
                print("\t\tInvalid input")
                home()


        if option == '2':
            create_party_table(cursor)

            choose = get_party_option()

            if choose == '2':
                show_party_details(cursor)

            if choose == '1':
                name, symbol_name = get_party_details()

                party = Party(name, symbol_name)

                add_party_to_db(party, cursor)

                cnx.commit()




        if option == '3':


            check_party_table(cursor)

            create_candidates_table(cursor)

            show_party_details(cursor)

            nic = input("insert nic: ")

            count = check_nic_in_citizens_table(nic, cursor)

            if count == 1:
                party, education = get_candidate_details()

                candidate = Candidate(nic, party, education)

                add_candidate_to_db(candidate, cursor)






            else:

                print("Candidate not registered as citizen \n registered as citizen")

                nic, name, state_province, age = get_citizen_details()
                party, education = get_candidate_details()

                citizen = Citizen(nic, name, age, state_province)
                candidate = Candidate(party, education)

                check_citizen_eligible(citizen, cursor, cnx)
                add_candidate_to_db(candidate, cursor)






            cnx.commit()

    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()
