def pearsonchisquare(feature_list, label_list, mincount=5, roundto=4):
    flag = False
    if is_numeric_dtype(feature_list):
        crosstab_df = pd.DataFrame(pd.crosstab(feature_list, label_list))
        for c in crosstab_df:
            if crosstab_df[c].min() < mincount:
                flag = True
                break
    if flag:
        q1 = np.quantile(feature_list, .10)
        q2 = np.quantile(feature_list, .20)
        q3 = np.quantile(feature_list, .30)
        q4 = np.quantile(feature_list, .40)
        q5 = np.quantile(feature_list, .50)
        q6 = np.quantile(feature_list, .60)
        q7 = np.quantile(feature_list, .70)
        q8 = np.quantile(feature_list, .80)
        q9 = np.quantile(feature_list, .90)

        bucket_list = pd.DataFrame(columns=['cutoffs'])
        i = 0
        for v in feature_list:
            if v < q1:
                bucket_list.loc[i] = q1
            elif v >= q1 and v < q2:
                bucket_list.loc[i] = q2
            elif v >= q2 and v < q3:
                bucket_list.loc[i] = q3
            elif v >= q3 and v < q4:
                bucket_list.loc[i] = q4
            elif v >= q4 and v < q5:
                bucket_list.loc[i] = q5
            elif v >= q5 and v < q6:
                bucket_list.loc[i] = q6
            elif v >= q6 and v < q7:
                bucket_list.loc[i] = q7
            elif v >= q7 and v < q8:
                bucket_list.loc[i] = q8
            elif v >= q8 and v < q9:
                bucket_list.loc[i] = q9
            else:
                bucket_list.loc[i] = feature_list.max()
            i += 1
        contingency_table = pd.crosstab(bucket_list['cutoffs'], label_list)
    else:
        contingency_table = pd.crosstab(feature_list, label_list)
    stat, p, dof, expected = stats.chi2_contingency(contingency_table)
    return [round(stat, roundto), round(p, roundto)]
