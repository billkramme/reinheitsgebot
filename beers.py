def listbeers():
    return [
    ["Schlafly Oatmeal Stout", "Oatmeal Stout", "5.7% ABV", "40 IBU", "Missouri", 1],
    ["Shiner Bock", "Bock", "4.4% ABV", "13 IBU", "Texas", 2],
    ["Guinness Draught", "Irish Dry Stout", "4.2% ABV", "40 IBU", "Ireland", 3],
    ["Sierra Nevada Narwhal", "Russian Imperial Stout", "10.2% ABV", "60 IBU", "California", 4],
    ["Horny Goat Exposed", "Cream Ale", "4.9% ABV", "13 IBU", "Wisconsin", 5],
    ["West Sixth Pay-It-Forward Cocoa Porter", "Porter", "7% ABV", "N/A IBU", "Kentucky", 6],
    ["Great Flood Brown", "English Brown Ale", "6.8% ABV", "26 IBU", "Kentucky", 7],
    ["Schlafly Pumpkin Ale", "Pumpkin Beer", "8% ABV", "16 IBU", "Missouri", 8],
    ["Great Flood Kelvin's Kilt Barrel Aged Scotch", "Scotch Ale", "8.6% ABV", "N/A IBU", "Kentucky", 9],
    ["Great Flood Banjo Steve's Stout", "Stout", "5.2% ABV", "24 IBU", "Kentucky", 10],
    ["Goose Island Lolita", "American Wild Ale", "8.7% ABV", "32 IBU", "Illinois", 11],
    ["Perennial La Boheme", "Flanders Red Ale", "5.5% ABV", "N/A IBU", "Missouri", 12],
    ["Bell's Oarsman Ale", "Berliner Weisse", "4% ABV", "N/A IBU", "Michigan", 13],
    ["Schlafly Pale Ale", "English Pale Ale", "4.4% ABV", "25 IBU", "Missouri", 14],
    ["Schlafly Coffee Stout", "Stout", "5.7% ABV", "30 IBU", "Missouri", 15],
    ["Schlafly Irish-Style Extra Stout", "Foreign/Export Stout", "8% ABV", "45 IBU", "Missouri", 16],
    ["Shiner Bohemian Black Lager", "Black Lager", "4.9% ABV", "N/A IBU", "Texas", 17],
    ["North Coast Old Rasputin", "Russian Imperial Stout", "9% ABV", "75 IBU", "California", 18],
    ["Resignation KCCO Black Lager", "Black Lager", "5.1% ABV", "22 IBU", "Texas", 19],
    ["O'Fallon Smoke", "Smoked Beer", "6% ABV", "N/A IBU", "Missouri", 20],
    ["Left Hand Milk Stout", "Milk Stout", "6% ABV", "N/A IBU", "Colorado", 21],
    ["Schlafly Oktoberfest", "Oktoberfest", "5.5% ABV", "25 IBU", "Missouri", 22],
    ["Schlafly Hefeweizen", "Hefeweizen", "4.4% ABV", "16 IBU", "Missouri", 23],
    ["Young's Double Chocolate Stout", "Milk Stout", "5.2% ABV", "25 IBU", "England", 24],
    ["Exit 6 The Wicked", "Pumpkin Beer", "9% ABV", "20 IBU", "Missouri", 25],
    ["New Belgium Lips of Faith La Folie", "Flanders Oud Bruin", "7% ABV", "18 IBU", "Colorado", 26],
    ["Hofbrau Oktoberfestbier", "Oktoberfest", "6.3% ABV", "N/A IBU", "Germany", 27],
    ["Sam Adams Oktoberfest", "Oktoberfest", "5.3% ABV", "16 IBU", "Massachusetts", 28],
    ["Kirkwood Station Blackberry Wheat", "Fruit Beer", "4.8% ABV", "11 IBU", "Missouri", 29],
    ["Mikkeller It's Alive Barrel Aged White Wine", "Sour Ale", "8% ABV", "N/A IBU", "Denmark", 30],
    ["Santa Fe State Pen Porter", "American Porter", "6.4% ABV", "N/A IBU", "New Mexico", 31],
    ["Left Hand Good Juju", "Spiced Beer", "4.5% ABV", "20 IBU", "Colorado", 32],
    ["Stiegl-Radler Grapefruit Naturtrub", "Radler", "2% ABV", "N/A IBU", "Austria", 33],
    ["Angry Orchard Apple Ginger", "Cider", "5% AVB", "N/A IBU", "Ohio", 34],
    ["Arcadia Whitsun Ale", "American Pale Wheat Ale", "6.2% ABV", "N/A IBU", "Michigan", 35],
    ["Sam Adams Boston Lager", "Vienna Lager", "4.9% ABV", "30 IBU", "Massachusetts", 36],
    ["Deschutes Black Butte Porter", "American Porter", "5.2% ABV", "30 IBU", "Oregon", 37],
    ["O'Fallon Pumpkin Beer", "Pumpkin Beer", "5.5% ABV", "N/A IBU", "Missouri", 38],
    ["Charleville Strawberry Blonde Ale", "Fruit Beer", "4.5% ABV", "N/A IBU", "Missouri", 39],
    ["Breckenridge Vanilla Porter", "American Porter", "4.7% ABV", "16 IBU", "Colorado", 40],
    ["Exit 6 Pineapple Saison", "Saison", "2.8% ABV", "N/A IBU", "Missouri", 41],
    ["Schmaltz He'Brew Funky Jewbelation", "American Strong Ale", "9.4% ABV", "N/A IBU", "New York", 42],
    ["Southern Tier Warlock", "Pumpkin Beer", "8.6% ABV", "N/A IBU", "New York", 43],
    ["Yazoo Gerst Amber", "American Amber Ale", "5% ABV", "N/A IBU", "Tennessee", 44],
    ["Yuengling Traditional Lager", "American Amber Lager", "4.4% ABV", "N/A IBU", "Pennsylvania", 45],
    ["Blackstone St. Charles Porter", "American Porter", "5.8% ABV", "N/A IBU", "Tennessee", 46],
    ["Schlafly Helles Style Summer Lager", "Helles Lager", "4.5% ABV", "17 IBU", "Missouri", 47],
    ["Liefmans Cuvee Brut", "Sour Ale", "6% ABV", "N/A IBU", "Belgium", 48],
    ["Boulevard Terra Incognita", "American Wild Ale", "8.5% ABV", "39 IBU", "Missouri", 49],
    ["Urban Chestnut Cuvee De Peche", "Lambic", "6.5% ABV", "10 IBU", "Missouri", 50],
    ["Brasserie Cantillon Iris", "Lambic", "5% ABV", "N/A IBU", "Belgium", 51],
    ["Evil Twin Justin Blabaer", "Berliner Weisse", "4.5% ABV", "N/A IBU", "Denmark", 52],
    ["Goose Island Madame Rose", "American Wild Ale", "6.5% ABV", "40 IBU", "Illinois", 53],
    ["Schlafly Milk Chocolate Stout", "Milk Stout", "6.6% ABV", "29 IBU", "Missouri", 54],
    ["Six Row Whale Ale", "American Pale Wheat Ale", "5.5% ABV", "N/A IBU", "Missouri", 55],
    ["Civil Life Ruby Mild", "English Mild Ale", "4% ABV", "N/A IBU", "Missouri", 56],
    ["Civil Life Eric's Peat Smoked Special Beer", "ESB", "5.1% ABV", "N/A IBU", "Missouri", 57],
    ["Leinenkugel Summer Shandy", "Radler", "4.2% ABV", "14 IBU", "Wisconsin", 58],
    ["Brabandere Petrus Aged Pale", "Sour Ale", "7.3% ABV", "N/A IBU", "Belgium", 59],
    ["New Belgium Lips of Faith Le Terroir", "American Wild Ale", "7.5% ABV", "N/A IBU", "Colorado", 60],
]
