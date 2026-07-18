"""
Data loading utilities for the NASA C-MAPSS turbofan degradation dataset.
"""
import pandas as pd

COLUMN_NAMES = (
    ["unit_number", "time_in_cycles"]
    + [f"operational_setting_{i}" for i in range(1, 4)]
    + [f"sensor_{i}" for i in range(1, 22)]
)


def load_cmapss(train_path: str, test_path: str, rul_path: str):
    """
    Load the C-MAPSS train/test/RUL files for a given FD subset.

    Parameters
    ----------
    train_path : path to train_FD00X.txt
    test_path : path to test_FD00X.txt
    rul_path : path to RUL_FD00X.txt

    Returns
    -------
    train_df, test_df, rul_df : pandas DataFrames
    """
    train_df = pd.read_csv(train_path, sep=r"\s+", header=None, names=COLUMN_NAMES)
    test_df = pd.read_csv(test_path, sep=r"\s+", header=None, names=COLUMN_NAMES)
    rul_df = pd.read_csv(rul_path, sep=r"\s+", header=None, names=["RUL"])
    return train_df, test_df, rul_df


def add_rul_labels(train_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a RUL (remaining useful life) column to the training data.
    For training data, RUL at each timestep = (max cycle for that unit) - (current cycle).
    """
    max_cycles = train_df.groupby("unit_number")["time_in_cycles"].max().reset_index()
    max_cycles.columns = ["unit_number", "max_cycle"]
    df = train_df.merge(max_cycles, on="unit_number", how="left")
    df["RUL"] = df["max_cycle"] - df["time_in_cycles"]
    df.drop(columns=["max_cycle"], inplace=True)
    return df


if __name__ == "__main__":
    # Example usage once data/train_FD001.txt etc. are downloaded:
    train, test, rul = load_cmapss(
        "../data/train_FD001.txt",
        "../data/test_FD001.txt",
        "../data/RUL_FD001.txt",
    )
    train = add_rul_labels(train)
    print(train.head())
    print(f"\nUnits: {train['unit_number'].nunique()}, Rows: {len(train)}")
