def unistats(df):
    import pandas as pd
    import numpy as np
    from scipy.stats import kurtosis, skew
    from matplotlib import pyplot as plt
    
    output = "\033[1m{:10}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}\033[0m".format('', 'Count', 'Unique', 'Type', 'Min', 'Max', '25%', '50%', '75%', 'Mean', 'Median', 'Mode', 'Std', 'Skew', 'Kurt') + "\n"
    
    for col in df.columns:
        name = col
        count = df[col].count()
        unique = df[col].nunique()
        dtype = str(df[col].dtype)
        
        if df[col].dtype != 'object':
            min = round(df[col].min(), 2)
            max = round(df[col].max(), 2)
            quar_1 = np.quantile(df[col], .25)
            quar_2 = np.quantile(df[col], .50)
            quar_3 = np.quantile(df[col], .75)
            mean = round(df[col].mean(), 2)
            median = round(df[col].median(), 2)
            mode = round(df[col].mode().values[0], 2)
            std = round(df[col].std(), 2)
            skew = round(df[col].skew(), 2)
            kurt = round(df[col].kurt(), 2)
            
            plt.hist(df[col])
            plt.title(col)
            plt.ylabel('count')
            
            textstr= 'count:         ' + str(count) + '\n'
            textstr = 'unique values:' + str(unique) + '\n'
            textstr = 'min:          ' + str(min) + '\n'
            textstr = 'max:          ' + str(max) + '\n'
            textstr = 'quar_1:       ' + str(quar_1) + '\n'
            textstr = 'quar_2:       ' + str(quar_2) + '\n'
            textstr = 'quar_3:       ' + str(quar_3) + '\n'
            textstr = 'mean:         ' + str(mean) + '\n'
            textstr = 'median:       ' + str(median) + '\n'
            textstr = 'mode:         ' + str(mode) + '\n'
            textstr = 'std:          ' + str(std) + '\n'
            textstr = 'skewness:     ' + str(skew) + '\n'
            textstr = 'kurtosis:     ' + str(kurt) + '\n'
            
            
            plt.text(1, 0.1, textstr, fontsize=12, transform=plt.gcf().transFigure)
            plt.show()
            
        else:
            min = 'NaN'
            max = 'NaN'
            quar_1 = 'NaN'
            quar_2 = 'NaN'
            quar_3 = 'NaN'
            mean = 'NaN'
            median = 'NaN'
            mode = 'NaN'
            std = 'NaN'
            skew = 'NaN'
            kurt = 'NaN'
        output += "\033[1m{:<10}\033[0m{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format(name, count, unique, dtype, str(min), str(max), str(quar_1), str(quar_2), str(quar_3), str(mean), str(median), str(mode), str(std), str(skew), str(kurt)) + "\n"
        
        print('\n')
        print(output)
