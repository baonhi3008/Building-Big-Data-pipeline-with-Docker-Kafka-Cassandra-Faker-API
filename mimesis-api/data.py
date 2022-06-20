from mimesis import Food
from mimesis import Text
from mimesis import Person
person = Person()
food = Food()
text = Text()


def get_food_data():
    return {
        "chef": person.first_name(),
        "chef_nationality": person.nationality(),
        "dish": food.dish(),
        "drink": food.drink(),
        "fruit": food.fruit(),
        "level": text.level(),
        "quote": text.quote(),
        "spices": food.spices(),
        "vegetable": food.vegetable(),

    }