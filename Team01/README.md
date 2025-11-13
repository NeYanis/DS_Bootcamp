# Food and nutrition

Summary: This rush will help you to strengthen the skills acquired over the previous
days

## Task

In this rush, you are going to work on your own application that will help
people to eat healthier and tastier food. It is a good and valuable experience to
create a product prototype out of the different technologies that you have studied.
This will be a pretty result for just two weeks of diving in Python and data science!

Your work will have three stages: research (work in a Notebook), development
(organizing everything in a module with classes and methods), and the program
itself (python script). Each of the stages will produce corresponding files
as a result.

### Main program

Let us start from the end. The program is a Python script (```nutritionist.py```).

* It takes in a list of ingredients.
* It forecasts and returns the rating class (bad, so-so, great) of a potential dish with
the ingredients.
* It finds and returns all the nutrients (proteins, fats, sodium, etc.) in the ingredients
as well as their daily values in %.
* It finds 3 the most similar recipes to the list of ingredients, their ratings, and the
URLs where a user can find the full details.

Here is an example:

```
$ ./nutritionist.py milk, honey, jam
I. OUR FORECAST
You might find it tasty, but in our opinion, it is a bad idea to have a
dish with that list of ingredients.
II. NUTRITION FACTS
Milk
Protein - 6% of Daily Value
Total Carbohydrate - 1% of Daily Value
Total Fat - 1% of Daily Value
Calcium - 12% of Daily Value
...
Honey
...
Jam
...
III. TOP-3 SIMILAR RECIPES:
- Strawberry-Soy Milk Shake, rating: 3.0, URL:
https://www.epicurious.com/recipes/food/views/strawberry-soy-milk-
shake-239217
- ...
- ...
```

### Development

You need to create a Python module (```recipes.py```) with the classes and
methods that are used in the main script.

### Research

In this part of the rush, you need to prepare everything that is used
in the classes and methods above in a Jupyter Notebook (recipes.ipynb).

* Forecast
  * Data preparation 
    * Use [the dataset](https://drive.google.com/file/d/1hzmxNBrY7-9mv5EpqAvhVUiJahfrcYUN/view?usp=sharing) from Epicurious collected by HugoDarwood. 
    * Filter the columns: the less non-ingredient columns in your
dataset the
better. You will predict the rating or rating category using only the ingredients and nothing else. 
  * Regression 
    * Try different algorithms and their hyperparameters for rating
prediction.
Choose the best on cross-validation and find the score (RMSE) on the test
subsample. 
    * Try different ensembles and their hyperparameters. Choose the
best on
cross-validation and find the score on the test subsample. 
    * Calculate the RMSE for a naive regressor that predicts the
average rating. 
  * Classification 
    * Binarize the target column by rounding the ratings to the closest
integer.
This will be your classes. 
    * Try different algorithms and their hyperparameters for class
prediction.
Choose the best on cross-validation and find the score (accuracy) on the
test subsample. 
    * Compare the metrics using accuracy. Calculate the accuracy of a
naive
classificator that predicts the most common class.
    * Binarize the target column again by converting the integers to
classes ‘bad’
(0, 1), ‘so-so’ (2, 3), ‘great’ (4, 5). 
    * Try different algorithms and their hyperparameters for class
prediction.
Choose the best on cross-validation and find the score on the test subsample. 
    * Compare the metrics using accuracy. Calculate the accuracy of a
naive
classificator that predicts the most common class. 
    * What is worse: to predict a bad rating which is good in real life, or
to
predict a good rating which is bad in real life? Replace accuracy with the
appropriate metric. 
    * Try different algorithms and their hyperparameters for class
prediction
with the new metric. Choose the best and find the score on the test
subsample. 
    * Try different ensembles and their hyperparameters. Choose the
best and
find the score on the test subsample.
  * Decision
    * Decide what is better to use: the regression model or the
classification.
Save the best model. You will use it in the program.
* Nutrition Facts
  * Collect all the nutrition facts for the ingredients from your prepared and filtered dataset (only ingredient columns) into a dataframe. Use [the following API](https://fdc.nal.usda.gov/api-guide.html) for that. 
  * Transform all the values into % of the daily value. Keep only nutrients that
exist in [this](https://drive.google.com/file/d/1jn0t5tU_RgOpq4wcO-uS4D0_NAP6MwHz/view?usp=sharing) and [that](https://drive.google.com/file/d/1bmdZGB0QwND2BD3XlC1JswL7AdnTJHLT/view?usp=sharing) table. 
  * Save the transformed dataframe into a CSV file that you will use in your main
program 
* Similar Recipes 
  * For each recipe from the dataset, collect the URL from epicurious.com with
  its details (if there is no URL for that recipe, skip it).
  * Save the new dataframe to a CSV file that you will use in your main program.

### Bonus part

Add more methods to the classes that will help the script perform a new
function: generate a menu for a day.

The daily menu should randomly give a list of the three recipes that
cover most of the nutritional needs (% of the daily value) without
overtaking them and have the highest total rating.

You should offer only recipes appropriate for breakfast, lunch, and dinner,
respectively.

The result of the program should look like this:

```
BREAKFAST
---------------------
Feta, Spinach, and Basil Omelette Muffins (rating: 4.375)
Ingredients:
- arugula
- egg
- feta
- muffin
- omelet
- spinach
- tomato
Nutrients:
- protein: 16%
- fat: 10%
- sodium: 7 %
- ...
URL: https://www.epicurious.com/recipes/food/views/feta-spinach-and-basil-omelette-muffins
LUNCH
---------------------
...
```
