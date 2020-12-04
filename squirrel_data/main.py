import pandas as pd

data = pd.read_csv("squirrel_data.csv")

columns = data.columns

fur_colors = data['Primary Fur Color']

fur_color_count = fur_colors.value_counts()

final_dict = {
    'Fur Color': fur_color_count.index.tolist(),
    'Count': fur_color_count.values.tolist()
}

final_data = pd.DataFrame(final_dict)

final_data.to_csv("squirrel_count.csv")