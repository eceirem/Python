main_year = 2000
input_year = int(input())
animal_years_list = ["ejderha","yilan","at", "koyun", "maymun","horoz"
                    , "kopek", "domuz", "fare", "okuz", "kaplan", "tavsan"]

if input_year < main_year:
    animal_year = (main_year - input_year) % 12
# burada tersten gideceğiz. 1 çıktığında listede bir adım geri demek bu da tavşan oluyor
    print(animal_years_list[-animal_year])
else:
    animal_year = (input_year - main_year) % 12
    print(animal_years_list[animal_year])