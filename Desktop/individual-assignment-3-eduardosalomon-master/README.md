# Individual assignment 3

Welcome to Individual Assignment 3.  The idea for this exercise is to use
classes to model different problems, if you have to decide between putting your
data into a simple dictionary or using classes, choose the later.

1. [Due date](#due-date)
2. [Exercises](#exercises)
   * [Exercise 1 - Classes](#exercise-1---classes)
   * [Exercise 2 - Price calculation](#exercise-2---price-calculation)
   * [Exercise 3 - Customer tier](#exercise-3---customer-tier)
3. [Grading](#grading)
4. [Submitting your assignment](#submitting-your-assignment)

## Due date

The assignment is due on December 23rd, at 22:00 Madrid time.

## Exercises

For these exercises we will imagine we work on an ecommerce website that sells
music related products.

Our shop will sell:

| **Product**    | **Price** |
|----------------|-----------|
| Guitar         | 1000      |
| Pick box       | 5         |
| Guitar strings | 10        |

### Exercise 1 - Classes

In this first exercise you'll need to create Python classes to support the
following actions:

- Each one of the products mentioned above will need to be represented as a
  `Product`.
- There must exist a `ShoppingCart`.
- There should be a way for adding products to the shopping cart.

### Exercise 2 - Price calculation

Create a method `calculate_price` to calculate the total price of the
`ShoppingCart`.  This method must not receive new parameters, and only
calculate the price of the elements already added to the `ShoppingCart`.

### Exercise 3 - Customer tier

The company decides to add a new customer tier feature to the shop.  Now
shopping carts can have an optional customer tier, that will provide some
discount:

- **Silver** tier: Provides a fixed 5$ discount in the total price of the
  `ShoppingCart`.
- **Gold** tier: Provides a 10% discount to the total price of the
  `ShoppingCart`.

Create the classes needed to add that functionality.

Create a new method on `ShoppingCart` called `calculate_price_with_discounts`
that calculates the total price with the discounts applied.

## Grading

| **Exercise** | **Max possible grade** |
|--------------|------------------------|
| Exercise 1   | 3                      |
| Exercise 2   | 3                      |
| Exercise 3   | 3                      |
| Coding style | 1                      |

Total possible points **10**.

## Submitting your assignment

In order to submit your assignment you will just need to push the latest
version of your code to github.
