# Узнать какая максимальная households в зоне минимального значения population

df[df['population']==df['population'].min()]['households'].agg(['max'])