//Pizza Oven
function pizzaOven(crust, sauce, cheese, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;
}
//pizza1
var pizza1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"]);
    console.log(pizza1);

//pizza2
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"])
    console.log(pizza2);

//pizza3
var pizza3 = pizzaOven("stuffed crusted", "tomato", ["mozzarella", "parmesan"], ["jalapeno", "olives", "onions"])
    console.log(pizza3);

//pizza4
var pizza4 = pizzaOven("hand tossed", "pesto", ["mozzarella", "feta"], ["pineapple", "olives", "onions", "jalapeno", "pepper"])
    console.log(pizza4);

