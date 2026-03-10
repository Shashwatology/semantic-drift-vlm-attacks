def compute_sdr(df, group_cols=["background", "alpha"]):
    """
    Computes Semantic Drift Rate (SDR).
    
    Args:
        df (pandas.DataFrame): Results table dataframe.
        group_cols (list): Columns to group by when calculating the mean drift.
        
    Returns:
        pandas.Series: The mean drift per group.
    """
    return df.groupby(group_cols)["drift"].mean()

def compute_dr(df):
    """
    Computes Detection Rate (DR).
    """
    true_drifts = df[df["drift"] == 1]
    if len(true_drifts) == 0:
        return 0.0
    return true_drifts["sev_flag"].mean()

def compute_fpr(df):
    """
    Computes False Positive Rate (FPR).
    """
    no_drifts = df[df["drift"] == 0]
    if len(no_drifts) == 0:
        return 0.0
    return no_drifts["sev_flag"].mean()
