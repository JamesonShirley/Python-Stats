def bivstats(df, label, roundto=4):
    output_df = pd.DataFrame(columns=['Effect', 'Stat', 'p-value'])
    for col in df.columns:
        if col != label:
            if not is_object_dtype(df[label]) and not is_object_dtype(df[col]):
                effect, stat, p = pearson_r_analysis(df, col, label)
            elif not is_object_dtype(df[label]) and is_object_dtype(df[col]):
                groups = df[col].unique()
                # If the data is all unique, an anova analysis will not work
                # Because each of the arrays passed into the f_oneway function will be of length 1
                # So we will use a chi square as backup
                if len(groups) == len(df[col]):
                    effect, stat,  p = chi_square_analysis(df, col, label)
                else:
                    effect, stat, p = anova_analysis(df, col, label, groups)
            else:
                effect, stat, p = chi_square_analysis(df,  col, label)
            output_df.loc[col] = [effect, stat, p]
    output_df.index.name = "Feature"
    output_df = output_df.sort_values('p-value')
    output_df = output_df.round(roundto)
    return output_df
