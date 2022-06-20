from faker import Faker

fake = Faker()


def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "country": fake.country(),
        "credit_card_number": fake.credit_card_number(),
        "email": fake.email(),
        "i_bank": fake.iban(),
        "job": fake.job(),
        "phone_number": fake.phone_number(),
        "swift": fake.swift(),
        "year": fake.year()
    }
