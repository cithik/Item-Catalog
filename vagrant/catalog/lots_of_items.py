from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///categoryitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com")
session.add(user1)
session.commit()

user2 = User(name="Kriti Vyaas", email="kriti.vyaas@udacity.com")
session.add(user2)
session.commit()

# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=2, name="Veggie Burger", description="Juicy grilled veggie patty with tomato and lettuce",
             price="$7.50", category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="French Fries", description="with garlic and parmesan",
             price="$2.99", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
             price="$5.50", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
             price="$3.99", category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
             price="$7.99", category=category1)

session.add(item5)
session.commit()


# Items for Basketball
category2 = Category(user_id=2, name="Basketball")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
             price="$7.99", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Peking Duck", description=" A famous duck dish from Beijing[1]",
             price="$25", category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber ",
             price="15",  category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
             price="12",  category=category2)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef",
             price="14",  category=category2)

session.add(item5)
session.commit()

#
# # Items for Baseball
# category3 = Category(user_id=1, name="Baseball")
#
# session.add(category3)
# session.commit()
#
#
# item1 = Item(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth",
#              price="$8.99", category=category3)
#
# session.add(item1)
# session.commit()
#
# item2 = Item(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling",
#              price="$6.99", category=category3)
#
# session.add(item2)
# session.commit()
#
# item3 = Item(user_id=1, name="Gyoza", description="The most prominent Japanese-style",
#              price="$9.95", category=category3)
#
# session.add(item3)
# session.commit()
#
# item4 = Item(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu",
#              price="$6.99", category=category3)
#
# session.add(item4)
# session.commit()
#
# item5 = Item(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
#              price="$9.50", category=category3)
#
# session.add(item5)
# session.commit()
#
#
# # Items for Frisbee
# category4 = Category(user_id=1, name="Frisbee ")
#
# session.add(category4)
# session.commit()
#
#
# item1 = Item(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk ",
#              price="$2.99", category=category4)
#
# session.add(item1)
# session.commit()
#
# item2 = Item(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
#              price="$5.99",  category=category4)
#
# session.add(item2)
# session.commit()
#
# item3 = Item(user_id=1, name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea ",
#              price="$4.50", category=category4)
#
# session.add(item3)
# session.commit()
#
# item4 = Item(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced",
#              price="$6.95", category=category4)
#
# session.add(item4)
# session.commit()
#
# item5 = Item(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo",
#              price="$7.95", category=category4)
#
# session.add(item5)
# session.commit()
#
#
# # Items for Snowboarding
# category5 = Category(user_id=1, name="Snowboarding ")
#
# session.add(category5)
# session.commit()
#
#
# item1 = Item(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish",
#              price="$13.95", category=category5)
#
# session.add(item1)
# session.commit()
#
# item2 = Item(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
#              price="$4.95", category=category5)
#
# session.add(item2)
# session.commit()
#
# item3 = Item(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
#              price="$6.95", category=category5)
#
# session.add(item3)
# session.commit()
#
# item4 = Item(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
#              description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", category=category5)
#
# session.add(item4)
# session.commit()
#
# item5 = Item(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth",
#              price="$7.95", category=category5)
#
# session.add(item5)
# session.commit()
#
#
# # Items for Rock Climbing
# category6 = Category(user_id=1, name="Rock Climbing")
#
# session.add(category6)
# session.commit()
#
#
# item1 = Item(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes",
#              price="$9.95", category=category6)
#
# session.add(item1)
# session.commit()
#
# item2 = Item(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
#              price="$7.95", category=category6)
#
# session.add(item2)
# session.commit()
#
# item3 = Item(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
#              price="$6.50", category=category6)
#
# session.add(item3)
# session.commit()
#
# item4 = Item(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
#              price="$6.75", category=category6)
#
# session.add(item4)
# session.commit()
#
#
# # Items for Foosball
# category7 = Category(user_id=1, name="Foosball ")
#
# session.add(category7)
# session.commit()
#
# item1 = Item(user_id=1, name="Chicken Fried Steak", description="Fresh battered sirloin steak fried",
#              price="$8.99", category=category7)
#
# session.add(item1)
# session.commit()
#
#
# item2 = Item(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries ",
#              price="$2.99", category=category7)
#
# session.add(item2)
# session.commit()
#
# item3 = Item(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs",
#              price="$10.95", category=category7)
#
# session.add(item3)
# session.commit()
#
# item4 = Item(user_id=1, name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter",
#              price="$7.50", category=category7)
#
# session.add(item4)
# session.commit()
#
# item5 = Item(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy ",
#              price="$8.95", category=category7)
#
# session.add(item5)
# session.commit()
#
#
# # Items for Skating
# category8 = Category(user_id=1, name="Skating ")
#
# session.add(category8)
# session.commit()
#
#
# item1 = Item(user_id=1, name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans",
#              price="$5.95", category=category8)
#
# session.add(item1)
# session.commit()
#
# item2 = Item(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake",
#              price="$7.99", category=category8)
#
# session.add(item2)
# session.commit()
#

print "added menu items!"
