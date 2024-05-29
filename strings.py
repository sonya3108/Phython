def main():
    header_footer = "~" * 50
    print(header_footer)

    dish_name = input("Введіть назву страви, рецепт якої вам подобається: ").strip()

    recipe = input("Введіть рецепт зазначеної страви: ").strip()

    formatted_dish_name = f"{'*' * 10} {dish_name.upper()} {'*' * 10}"

    formatted_recipe = recipe.lower().strip() + " 😊"

    print(formatted_dish_name)

    print(formatted_recipe)

    meat_count = formatted_recipe.count("мясо")

    print(f"Кількість слів 'мясо' в рецепті: {meat_count}")

    print(header_footer)


if __name__ == "__main__":
    main()