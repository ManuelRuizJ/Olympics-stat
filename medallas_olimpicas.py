import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataframe
df = pd.read_csv("./data/olympics_dataset.csv")
""" 
print(df.head())
print(df.info())
print(df.describe())
"""

# Aplicar filtro
df_medals = df[df['Medal'] != 'No medal']
# Orden perzonalizado
medal_orden = ['Silver', 'Gold', 'Bronze']
# Crear grafico con orden dado
plt.figure(figsize=(10, 6))
ax = sns.countplot(x='Medal', data=df_medals, order=medal_orden, palette='viridis')
# Etiquetas de conteos
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x = p.get_x() + width / 2
    y = height
    ax.text(x, y, f'{height}', ha='center', va='center')
# Mostar conteos
plt.title('Conteo de Medallas Olímpicas')
plt.xlabel('Tipo de Medalla')
plt.ylabel('Número de Medallas')
# Pasar a formato png
plt.savefig('number_medalls.png', format='png')
plt.show()
