from faker import Faker
fake = Faker()

if __name__ == "__main__":
    for i in range(3):
        i = fake.iban()
        print(i)