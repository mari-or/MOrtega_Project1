import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub


# download dataset
path = kagglehub.dataset_download("ridhopandhu/honkai-star-rail-character-data")

print("Path to dataset files:", path)


# find csv file
csv_file = "hsr_character-data.csv"
file_path = os.path.join(path, csv_file)

# read csv file 
df = pd.read_csv(file_path)

# basic output test
# print(df)



# gemini helped with filtering out only characters of nihility for plot 1
# Filter the DataFrame to only include characters with the Path of "The Nihility"
nihility_df = df[df['path'] == 'nihility'].copy()
# Select relevant columns for plotting from the filtered DataFrame
stats_df = nihility_df[['character', 'atk_1', 'def_1', 'hp_1']]
# Melt the DataFrame to long format for easier plotting
stats_long = stats_df.melt(id_vars='character', value_vars=['atk_1', 'def_1', 'hp_1'], var_name='Stat_Type', value_name='Stat_Value')


# plot 1: bar plot comparing all base stats of nihility characters

plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=stats_long,
    x='character',
    y='Stat_Value',
    hue='Stat_Type',
    palette='icefire'
)

plt.title('Comparison of ATK, DEF, and HP Stats for Nihility Characters in HSR')
plt.xlabel('Character')
plt.ylabel('Stat Value')
plt.tight_layout()
plt.savefig('nil_character_all_stats_comparison.png')
plt.show()



# plot 2: histogram of ATK distribution

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='atk_1', bins=15, kde=True, color='red')
plt.title('Distribution of Character Attack (ATK) Stats in HSR')
plt.xlabel('ATK')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('atk_distribution.png')
plt.show()

# plot 3: bar plot comparing path with combat type

plt.figure(figsize=(10, 6))
ax = sns.countplot(
    data=df,
    x='path',
    hue='combat_type',
    palette='Spectral'
)
plt.title('Distribution of Combat Types Across Different Paths in HSR')
plt.xlabel('Path')
plt.ylabel('Number of Characters')
plt.tight_layout()
plt.savefig('path_combat_type_comparison.png')
plt.show()


# plot 4: box plot displaying base atk distribution across paths

plt.figure(figsize=(10, 6))
sns.boxplot(x='combat_type', y='atk_1', data=df, palette='icefire')
plt.title('Character ATK Distribution by Combat Type in HSR')
plt.xlabel('Combat Type')
plt.ylabel('ATK')
plt.tight_layout()
plt.savefig('atk_by_combat_type_boxplot.png')
plt.show()


# plot 5: scatter plot visualizing atk and def of characters, including rarity and path
# gemini assisted with changing hue and style, now it looks pretty :')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='atk_20', y='def_20', data=df, hue='rarity', style='path', s=100)
plt.title('ATK vs. DEF Stats (Colored by Rarity, Styled by Path) in HSR')
plt.xlabel('ATK')
plt.ylabel('DEF')
plt.tight_layout()
plt.savefig('atk_vs_def_scatterplot.png')
plt.show()


