import pandas as pd
import random

genders=["Male", "Female", "Other", "Non-binary", "Prefer not to say"]

occasion=["Birthday", "Wedding", "Anniversary", "Retirement", "Bachelorette", "Success", 
          "Graduation", "Farewell", "Milestone Hitting", "Acheivement", "Festival", "Appreciation",
          "Housewarming", "Baby Shower", "Corporate"]

preferences=["Tech", "Fashion", "Books", "Fitness", "Gaming", "Art", "Music", "Travel", 
    "Home Decor", "Gourmet", "DIY", "Luxury", "Eco-friendly", "Collectibles", "Adventure",
    "Science & Space", "Pets", "Anime & Comics", "Self-care", "Productivity", "Spirituality"]

hobbies=["Sports", "Reading", "Cooking", "Photography", "Gardening", "Painting", "Writing", 
    "Dancing", "Hiking", "Gaming", "Cycling", "Fishing", "Knitting", "Yoga", "Woodworking",
    "Singing", "Astrophotography", "Meditation", "Calligraphy", "Podcasting", "Robotics",
    "Baking", "Travel Blogging", "Archery", "Martial Arts", "Car Collecting"]

jobs=["Student", "Engineer", "Doctor", "Artist", "Teacher", "Business Owner", "Freelancer", 
    "Scientist", "Musician", "Designer", "Writer", "Lawyer", "Chef", "Athlete", "Researcher",
    "Actor", "Politician", "Psychologist", "Fashion Designer", "Pilot", "Entrepreneur",
    "Veterinarian", "Astronomer", "Therapist", "Stock Trader", "Biotechnologist"]

past_gifts=["Smartwatch", "Book", "Perfume", "Headphones", "Gift Card", "Backpack", "Shoes", 
    "Jewelry", "Gaming Console", "Fitness Tracker", "Sunglasses", "Handbag", "Skincare Set",
    "Subscription Box", "Board Game", "Personalized Mug", "Customized Notebook", "Concert Tickets",
    "Drone", "VR Headset", "Limited Edition Sneakers", "Luxury Pen", "Candle Set", 
    "Coffee Maker", "Wireless Charger", "Portable Speaker", "Pet Accessories", "Sports Jersey"]

price_ranges = ["₹100-₹500", "₹500-₹2000", "₹2000-₹5000", "₹5000-₹10,000", "₹10,000-₹20,000", "₹20,000+"]

suggested_gifts=["Smartwatch", "Book", "Perfume", "Headphones", "Gift Card", "Backpack", "Shoes", 
    "Jewelry", "Gaming Console", "Fitness Tracker", "Sunglasses", "Handbag", "Skincare Set",
    "Subscription Box", "Board Game", "Personalized Mug", "Customized Notebook", "Concert Tickets",
    "Drone", "VR Headset", "Limited Edition Sneakers", "Luxury Pen", "Candle Set", 
    "Coffee Maker", "Wireless Charger", "Portable Speaker", "Pet Accessories", "Sports Jersey",
    "Smart Speaker", "Laptop Stand", "Bluetooth Earbuds", "Vinyl Records", "Comic Books", 
    "Handmade Soap Set", "Painting Kit", "Digital Drawing Tablet", "Cooking Kit", 
    "Leather Wallet", "Mini Projector", "Noise-Canceling Headphones", "Camping Gear", 
    "E-Reader", "Personalized Keychain", "Massage Gun", "DIY Craft Kit", "Tea Collection Set", 
    "Puzzle Set", "Action Figures", "Running Shoes", "Smart Home Device", "Succulent Plant Set"]

data={"Age":[random.randint(5, 80) for _ in range(1000)],
    "Gender":[random.choice(genders) for _ in range(1000)],
    "Occasion":[random.choice(occasion) for _ in range(1000)],
    "Preferences":[random.choice(preferences) for _ in range(1000)],
    "Hobbies":[random.choice(hobbies) for _ in range(1000)],
    "Job":[random.choice(jobs) for _ in range(1000)],
    "Past Gifts":[random.choice(past_gifts) for _ in range(1000)],
    "Price Range":[random.choice(price_ranges) for _ in range(1000)],
    "Suggested Gifts":[random.choice(suggested_gifts) for _ in range(1000)]}

df=pd.DataFrame(data)
df.to_csv("gift_dataset.csv", index=False)
print("Dataset saved as gift_dataset.csv")