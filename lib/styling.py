
def filter_by_cuisine():
    page_number = 1
    cuisine = ''

    while True:

        click.clear()
        print('Choose a Cuisine Type')
        print('==================')
        print('\n')
        print('Chinese')
        print('---')
        print('French')
        print('---')
        print('Hispanic')
        print('---')
        print('Italian')
        print('---')
        print('Japanese')
        print('---')
        print('Sushi')
        print('---')
        print('Tempura')
        print('---')
        print('\n')

        choice = click.prompt('\nType your choice').lower()
        
        if choice == 'chinese':
            cuisine = 'Chinese'
            break
        elif choice == 'french':
            cuisine = 'French'
            break
        elif choice == 'hispanic':
            cuisine = 'Hispanic'
            break
        elif choice == 'italian':
            cuisine = 'Italian'
            break
        elif choice == 'japanese':
            cuisine = 'Japanese'
            break
        elif choice == 'sushi':
            cuisine = 'Sushi'
            break
        elif choice == 'tempura':
            cuisine = 'Tempura'
            break

        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            print('\nPlease input a valid cuisine\n')
            click.pause()
            

    while True:

        click.clear()
        display_restaurants_by_cuisine(cuisine, page_number)
        choice = click.prompt("\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Restaurants Menu)")

        if choice == 'p' and page_number > 1:
            page_number -= 1
        elif choice == 'n':
            page_number += 1
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            click.echo("Invalid choice. Please try again.")