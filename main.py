"""This app produces a command line menu-driven application providing users with the
ability to search states for state capital, flower, population."""
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Start of application
print("*********************************************************")
print("Welcome to the Python State's Capital and Flower List Application\n")

# dictionary of state capital values
capital_list = {'AL': 'Montgomery',
                'AK': 'Juneau',
                'AZ': 'Phoenix',
                'AR': 'Little Rock',
                'CA': 'Sacramento',
                'CO': 'Denver',
                'CT': 'Hartford',
                'DE': 'Dover',
                'FL': 'Tallahassee',
                'GA': 'Atlanta',
                'HI': 'Honolulu',
                'ID': 'Boise',
                'IL': 'Springfield',
                'IN': 'Indianapolis',
                'IA': 'Des Moines',
                'KS': 'Topeka',
                'KY': 'Frankfort',
                'LA': 'Baton Rouge',
                'ME': 'Augusta',
                'MD': 'Annapolis',
                'MA': 'Boston',
                'MI': 'Lansing',
                'MN': 'St. Paul',
                'MS': 'Jackson',
                'MO': 'Jefferson City',
                'MT': 'Helena',
                'NE': 'Lincoln',
                'NV': 'Carson City',
                'NH': 'Concord',
                'NJ': 'Trenton',
                'NM': 'Santa Fe',
                'NY': 'Albany',
                'NC': 'Raleigh',
                'ND': 'Bismarck',
                'OH': 'Columbus',
                'OK': 'Oklahoma City',
                'OR': 'Salem',
                'PA': 'Harrisburg',
                'RI': 'Providence',
                'SC': 'Columbia',
                'SD': 'Pierre',
                'TN': 'Nashville',
                'TX': 'Austin',
                'UT': 'Salt Lake City',
                'VT': 'Montpelier',
                'VA': 'Richmond',
                'WA': 'Olympia',
                'WV': 'Charleston',
                'WI': 'Madison',
                'WY': 'Cheyenne'
                }

# dictionary of state population values
population_list = {'AL': 4887870,
                   'AK': 737438,
                   'AZ': 7171650,
                   'AR': 3013820,
                   'CA': 39557000,
                   'CO': 5695560,
                   'CT': 3572660,
                   'DE': 967171,
                   'FL': 21299300,
                   'GA': 10519500,
                   'HI': 1420490,
                   'ID': 1754210,
                   'IL': 12741100,
                   'IN': 6691880,
                   'IA': 3156140,
                   'KS': 2911500,
                   'KY': 4684000,
                   'LA': 4659980,
                   'ME': 1338400,
                   'MD': 6042720,
                   'MA': 6902150,
                   'MI': 9995920,
                   'MN': 5611180,
                   'MS': 2986530,
                   'MO': 6126450,
                   'MT': 1062300,
                   'NE': 1929270,
                   'NV': 3034390,
                   'NH': 1356460,
                   'NJ': 8908520,
                   'NM': 2095430,
                   'NY': 19542200,
                   'NC': 10383600,
                   'ND': 760077,
                   'OH': 11689400,
                   'OK': 3943080,
                   'OR': 4190710,
                   'PA': 12807100,
                   'RI': 1057320,
                   'SC': 5084130,
                   'SD': 882235,
                   'TN': 6770010,
                   'TX': 28701800,
                   'UT': 3161100,
                   'VT': 626299,
                   'VA': 8517680,
                   'WA': 7535590,
                   'WV': 1805830,
                   'WI': 5813570,
                   'WY': 577737
                   }

# dictionary of state flower values
flower_list = {'AL': 'Camellia',
               'AK': 'Forget_Me_Not',
               'AZ': 'Saguaro_Cactus_Blossom',
               'AR': 'Apple_Blossom',
               'CA': 'California_Poppy',
               'CO': 'Rocky_Mountain_Columbine',
               'CT': 'C_Mountain_laurel',
               'DE': 'Peach_Blossom',
               'FL': 'Orange_Blossom',
               'GA': 'Cherokee_Rose',
               'HI': 'Pua_Aloalo',
               'ID': 'Syringa',
               'IL': 'I_Violet',
               'IN': 'Peony',
               'IA': 'Wild_Rose',
               'KS': 'Sunflower',
               'KY': 'Goldenrod',
               'LA': 'Louisiana_Iris',
               'ME': 'White_Pine_Cone_and_Tasse',
               'MD': 'Black_Eyed_Susan',
               'MA': 'Mayflower',
               'MI': 'Dwarf_Lake_Iris',
               'MN': 'Pink_and_White_Ladys_Slipper',
               'MS': 'Magnolia',
               'MO': 'White_Hawthorn_Blossom',
               'MT': 'Bitterroot',
               'NE': 'Goldenrod',
               'NV': 'Sagebrush',
               'NH': 'Purple_lilac',
               'NJ': 'Violet',
               'NM': 'Yucca',
               'NY': 'Rose',
               'NC': 'Dogwood',
               'ND': 'Wild_Prairie_Rose',
               'OH': 'Red_Carnation',
               'OK': 'Mistletoe',
               'OR': 'Oregon_Grape',
               'PA': 'Mountain_Laurel',
               'RI': 'R_Violet',
               'SC': 'Yellow_Jessamine',
               'SD': 'American_Pasque',
               'TN': 'Iris',
               'TX': 'Bluebonnet',
               'UT': 'Sego_lily',
               'VT': 'Red_Carnation',
               'VA': 'American_Dogwood',
               'WA': 'Coast_Rhododendron',
               'WV': 'Rhododendron',
               'WI': 'Wood_Violet',
               'WY': 'Indian_Paintbrush'
               }

# images of state flowers
Camellia = Image.open(os.path.join(sys.path[0] + "\\" + '1.jpg'))
Forget_Me_Not = Image.open(os.path.join(sys.path[0] + "\\" + '2.jpg'))
Saguaro_Cactus_Blossom = Image.open(os.path.join(sys.path[0] + "\\" + '3.jpg'))
Apple_Blossom = Image.open(os.path.join(sys.path[0] + "\\" + '4.jpg'))
California_Poppy = Image.open(os.path.join(sys.path[0] + "\\" + '5.jpg'))
Rocky_Mountain_Columbine = Image.open(os.path.join(sys.path[0] + "\\" + '6.jpg'))
C_Mountain_laurel = Image.open(os.path.join(sys.path[0] + "\\" + '7.jpg'))
Peach_Blossom = Image.open(os.path.join(sys.path[0] + "\\" + '8.jpg'))
Orange_Blossom = Image.open(os.path.join(sys.path[0] + "\\" + '9.jpg'))
Cherokee_Rose = Image.open(os.path.join(sys.path[0] + "\\" + '10.jpg'))
Pua_Aloalo = Image.open(os.path.join(sys.path[0] + "\\" + '11.jpg'))
Syringa = Image.open(os.path.join(sys.path[0] + "\\" + '12.jpg'))
I_Violet = Image.open(os.path.join(sys.path[0] + "\\" + '13.jpg'))
Peony = Image.open(os.path.join(sys.path[0] + "\\" + '14.jpg'))
Wild_Rose = Image.open(os.path.join(sys.path[0] + "\\" + '15.jpg'))
Sunflower = Image.open(os.path.join(sys.path[0] + "\\" + '16.jpg'))
K_Goldenrod = Image.open(os.path.join(sys.path[0] + "\\" + '17.jpg'))
Louisiana_Iris = Image.open(os.path.join(sys.path[0] + "\\" + '18.jpg'))
White_Pine_Cone_and_Tasse = Image.open(os.path.join(sys.path[0] + "\\" + '19.jpg'))
Black_Eyed_Susan = Image.open(os.path.join(sys.path[0] + "\\" + '20.jpg'))
Mayflower = Image.open(os.path.join(sys.path[0] + "\\" + '21.jpg'))
Dwarf_Lake_Iris = Image.open(os.path.join(sys.path[0] + "\\" + '22.jpg'))
Pink_and_White_Ladys_Slipper = Image.open(os.path.join(sys.path[0] + "\\" + '23.jpg'))
Magnolia = Image.open(os.path.join(sys.path[0] + "\\" + '24.jpg'))
White_Hawthorn_Blossom = Image.open(os.path.join(sys.path[0] + "\\" + '25.jpg'))
Bitterroot = Image.open(os.path.join(sys.path[0] + "\\" + '26.jpg'))
Goldenrod = Image.open(os.path.join(sys.path[0] + "\\" + '27.jpg'))
Sagebrush = Image.open(os.path.join(sys.path[0] + "\\" + '28.jpg'))
Purple_lilac = Image.open(os.path.join(sys.path[0] + "\\" + '29.jpg'))
Violet = Image.open(os.path.join(sys.path[0] + "\\" + '30.jpg'))
Yucca = Image.open(os.path.join(sys.path[0] + "\\" + '31.jpg'))
Rose = Image.open(os.path.join(sys.path[0] + "\\" + '32.jpg'))
Dogwood = Image.open(os.path.join(sys.path[0] + "\\" + '33.jpg'))
Wild_Prairie_Rose = Image.open(os.path.join(sys.path[0] + "\\" + '34.jpg'))
Red_Carnation = Image.open(os.path.join(sys.path[0] + "\\" + '35.jpg'))
Mistletoe = Image.open(os.path.join(sys.path[0] + "\\" + '36.jpg'))
Oregon_Grape = Image.open(os.path.join(sys.path[0] + "\\" + '37.jpg'))
Mountain_Laurel = Image.open(os.path.join(sys.path[0] + "\\" + '38.jpg'))
R_Violet = Image.open(os.path.join(sys.path[0] + "\\" + '39.jpg'))
Yellow_Jessamine = Image.open(os.path.join(sys.path[0] + "\\" + '40.jpg'))
American_Pasque = Image.open(os.path.join(sys.path[0] + "\\" + '41.jpg'))
Iris = Image.open(os.path.join(sys.path[0] + "\\" + '42.jpg'))
Bluebonnet = Image.open(os.path.join(sys.path[0] + "\\" + '43.jpg'))
Sego_lily = Image.open(os.path.join(sys.path[0] + "\\" + '44.jpg'))
Red_Clover = Image.open(os.path.join(sys.path[0] + "\\" + '45.jpg'))
American_Dogwood = Image.open(os.path.join(sys.path[0] + "\\" + '46.jpg'))
Coast_Rhododendron = Image.open(os.path.join(sys.path[0] + "\\" + '47.jpg'))
Rhododendron = Image.open(os.path.join(sys.path[0] + "\\" + '48.jpg'))
Wood_Violet = Image.open(os.path.join(sys.path[0] + "\\" + '49.jpg'))
Indian_Paintbrush = Image.open(os.path.join(sys.path[0] + "\\" + '50.jpg'))

confirm = input("Would you like to continue? Y or N\n")
while confirm.upper() == "Y":
    # menu of user options
    while True:
        try:
            selection = int(input("Would you like to:\n"
                                  "1. Display all state capitals, "
                                  "flowers, and population information\n"
                                  "2. Search for a specific state\n"
                                  "3. Display a Bar graph of the top 5 "
                                  "populated states showing their "
                                  "overall population.\n"
                                  "4. Update the overall state population "
                                  "for a specific state.\n"
                                  "5. Exit program\n"))
            break

        except ValueError:
            print("Would you like to:\n"
                  "1. Display all state capitals, flowers, "
                  "and population information\n"
                  "2. Search for a specific state\n"
                  "3. Display a Bar graph of the top 5 "
                  "populated states showing their "
                  "overall population.\n"
                  "4. Update the overall state population "
                  "for a specific state.\n"
                  "5. Exit program\n")

    while selection:
        # display all state information
        if selection == 1:
            print("***** This is a list of all the state capitals, "
                  "flowers, and population info *****\n")

            # merge all 3 dictionaries
            def merge_dict(capital, population, flower):
                """This method combines the selected dictionaries
                 and displays the data"""
                new_dict = {**flower, **population, **capital}
                for key, value in new_dict.items():
                    print(str([key]) + ': ', 'Capital: ' + str(value) + ', ',
                          'Population: ' + str(population[key]) + ', ',
                          'Flower: ' + flower[key] + '\n')
                return new_dict


            # variable to merge dictionaries and display all data
            merge = merge_dict(capital_list, population_list, flower_list)
            break

        # search for specific state information
        if selection == 2:
            print("***** This allows you to search for a specific state *****\n")

            enter_state = input("Type a state name to search.\n")
            while enter_state:

                # search combined dictionaries and output specific state info
                def search_dict(capital, population, flower):
                    """This method searches the combined dictionaries
                            for the state entered and displays the data"""
                    new_dict = {**flower, **population, **capital}
                    for key, value in new_dict.items():
                        if key == enter_state.upper():
                            print(str([key]) + ': ', 'Capital: ' + str(value) + ', ',
                                  'Population: ' + str(population[key]) + ', ',
                                  'Flower: ' + flower[key] + '\n')
                    return new_dict


                # variable to search combined dictionaries for state info and display
                state_data = search_dict(capital_list, population_list, flower_list)

                # prompt user to view picture of state flower
                if state_data.get(enter_state.upper()):
                    view = input("Would you like to see an image of the flower?\n")

                    # display state flower picture
                    if view.upper() == "Y":
                        if enter_state.upper() == 'AL':
                            Camellia.show()
                        if enter_state.upper() == 'AK':
                            Forget_Me_Not.show()
                        if enter_state.upper() == 'AZ':
                            Saguaro_Cactus_Blossom.show()
                        if enter_state.upper() == 'AR':
                            Apple_Blossom.show()
                        if enter_state.upper() == 'CA':
                            California_Poppy.show()
                        if enter_state.upper() == 'CO':
                            Rocky_Mountain_Columbine.show()
                        if enter_state.upper() == 'CT':
                            C_Mountain_laurel.show()
                        if enter_state.upper() == 'DE':
                            Peach_Blossom.show()
                        if enter_state.upper() == 'FL':
                            Orange_Blossom.show()
                        if enter_state.upper() == 'GA':
                            Cherokee_Rose.show()
                        if enter_state.upper() == 'HI':
                            Pua_Aloalo.show()
                        if enter_state.upper() == 'ID':
                            Syringa.show()
                        if enter_state.upper() == 'IL':
                            I_Violet.show()
                        if enter_state.upper() == 'IN':
                            Peony.show()
                        if enter_state.upper() == 'IA':
                            Wild_Rose.show()
                        if enter_state.upper() == 'KS':
                            Sunflower.show()
                        if enter_state.upper() == 'KY':
                            K_Goldenrod.show()
                        if enter_state.upper() == 'LA':
                            Louisiana_Iris.show()
                        if enter_state.upper() == 'ME':
                            White_Pine_Cone_and_Tasse.show()
                        if enter_state.upper() == 'MD':
                            Black_Eyed_Susan.show()
                        if enter_state.upper() == 'MA':
                            Mayflower.show()
                        if enter_state.upper() == 'MI':
                            Dwarf_Lake_Iris.show()
                        if enter_state.upper() == 'MN':
                            Pink_and_White_Ladys_Slipper.show()
                        if enter_state.upper() == 'MS':
                            Magnolia.show()
                        if enter_state.upper() == 'MO':
                            White_Hawthorn_Blossom.show()
                        if enter_state.upper() == 'MT':
                            Bitterroot.show()
                        if enter_state.upper() == 'NE':
                            Goldenrod.show()
                        if enter_state.upper() == 'NV':
                            Sagebrush.show()
                        if enter_state.upper() == 'NH':
                            Purple_lilac.show()
                        if enter_state.upper() == 'NJ':
                            Violet.show()
                        if enter_state.upper() == 'NM':
                            Yucca.show()
                        if enter_state.upper() == 'NY':
                            Rose.show()
                        if enter_state.upper() == 'NC':
                            Dogwood.show()
                        if enter_state.upper() == 'ND':
                            Wild_Prairie_Rose.show()
                        if enter_state.upper() == 'OH':
                            Red_Carnation.show()
                        if enter_state.upper() == 'OK':
                            Mistletoe.show()
                        if enter_state.upper() == 'OR':
                            Oregon_Grape.show()
                        if enter_state.upper() == 'PA':
                            Mountain_Laurel.show()
                        if enter_state.upper() == 'RI':
                            R_Violet.show()
                        if enter_state.upper() == 'SC':
                            Yellow_Jessamine.show()
                        if enter_state.upper() == 'SD':
                            American_Pasque.show()
                        if enter_state.upper() == 'TN':
                            Iris.show()
                        if enter_state.upper() == 'TX':
                            Bluebonnet.show()
                        if enter_state.upper() == 'UT':
                            Sego_lily.show()
                        if enter_state.upper() == 'VT':
                            Red_Clover.show()
                        if enter_state.upper() == 'VA':
                            American_Dogwood.show()
                        if enter_state.upper() == 'WA':
                            Coast_Rhododendron.show()
                        if enter_state.upper() == 'WV':
                            Rhododendron.show()
                        if enter_state.upper() == 'WI':
                            Wood_Violet.show()
                        if enter_state.upper() == 'WY':
                            Indian_Paintbrush.show()

                    # if user declines to see picture
                    else:
                        break

                # if state entered is not found
                else:
                    print(enter_state.upper() + " not found in list")
                    enter_state = input("Type the 2 letter abbreviation for state to search.\n")
            print("")
            break

        # display bar graph of top 5 populated states
        if selection == 3:
            print("***** This will display a bar graph of the 5 most populated states *****\n")
            pop_values = list(population_list.values())
            pop_states = list(population_list.keys())
            pop_values, pop_states = zip(*sorted(zip(pop_values, pop_states)))

            # formats population range display to cover the range given by
            x = np.arange(5)

            # assign state name to x-graph text
            plt.xticks(x, (pop_states[pop_values.index(pop_values[49])],
                           pop_states[pop_values.index(pop_values[48])],
                           pop_states[pop_values.index(pop_values[47])],
                           pop_states[pop_values.index(pop_values[46])],
                           pop_states[pop_values.index(pop_values[45])]))

            # format population number to multiple for ease of view on graph
            populations = [(pop_values[49] * .000001), (pop_values[48] * .000001),
                           (pop_values[47] * .000001),
                           (pop_values[46] * .000001), (pop_values[45] * .000001)]

            # assign values to x/y axis of graph
            plt.bar(x, populations)

            plt.ylabel('Population in millions')
            plt.title('States with the 5 largest populations')
            plt.show()
            break

            # update population for a specific state
        if selection == 4:
            print("***** This will update the population for a specific state *****\n")
            pick_state = input("Enter the 2 letter abbreviation of the "
                               "state would you like to update\n")

            # iterate dict to get selected state population and display value
            def search_pop(capital, population, flower):
                """This method combines the 3 dictionaries
                and displays the combined data"""
                new_dict = {**flower, **population, **capital}
                for key in new_dict.keys():
                    if key == pick_state.upper():
                        print(str([key]) + ': ', 'Population: ' + str(population[key]) + '\n')
                return new_dict


            while pick_state:
                # variable to search dictionary for entered state 'pick_state_
                search_state = search_pop(capital_list, population_list, flower_list)

                if search_state.get(pick_state.upper()):
                    try:
                        pop = int(input("What is the new population "
                                        "number you would like to update\n"))
                    except ValueError:
                        print('Please enter a number value')
                        pop = int(input("What is the new population "
                                        "number you would like to update\n"))

                    # changes population of entered state to entered value 'pop',
                    # then displays new value
                    def change_pop(state):
                        """This method overrides the numerical value of
                                the population in the selected state"""
                        population_list[state] = pop
                        display = search_pop(capital_list, population_list, flower_list)
                        return display


                    # variable to take in state and apply change_pop method
                    print("The new population of " + pick_state.upper() + ':')
                    new_pop = change_pop(pick_state.upper())
                    proceed = input('Press enter to continue')
                    break

                # if state entered is not found
                else:
                    print(pick_state.upper() + " not found in list")
                    pick_state = input("Type the 2 letter abbreviation for state to search.\n")

            # exit program
        if selection == 5:
            print("***** Thank you for using the Python State's Capital "
                  "and Flower List Application *****\n")
            input('Press enter to exit')
            sys.exit()

        else:
            try:
                selection = int(input("Would you like to:\n"
                                      "1. Display all state capitals, flowers, "
                                      "and population information\n"
                                      "2. Search for a specific state\n"
                                      "3. Display a Bar graph of the top 5 "
                                      "populated states showing their "
                                      "overall population.\n"
                                      "4. Update the overall state population "
                                      "for a specific state.\n"
                                      "5. Exit program\n"))
                break

            except ValueError:
                print("Would you like to:\n"
                      "1. Display all state capitals, flowers, and population information\n"
                      "2. Search for a specific state\n"
                      "3. Display a Bar graph of the top 5 populated states showing their "
                      "overall population.\n"
                      "4. Update the overall state population for a specific state.\n"
                      "5. Exit program\n")
