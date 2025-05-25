import nfl_data_py as nfl
import pandas as pd
import os
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

# Set the output directory change this before running
output_dir = Your directory here

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define a function to clean and save dataframes
def clean_and_save(df, filename):
    """
    Cleans the dataframe using nfl.clean_nfl_data() and saves it to a CSV file.

    Args:
        df (pd.DataFrame): The dataframe to clean and save.
        filename (str): The name of the CSV file to save to.
    """
    cleaned_df = nfl.clean_nfl_data(df)
    output_path = os.path.join(output_dir, filename)
    cleaned_df.to_csv(output_path, index=False)

# Change the years variable to the year or years you want the data for
# 1. Play-by-play data
years = [2024]
pbp_cols = nfl.see_pbp_cols()  # Get all columns
if isinstance(pbp_cols, pd.Index):
    pbp_cols = pbp_cols.tolist()
pbp_data = nfl.import_pbp_data(years, columns=pbp_cols)
clean_and_save(pbp_data, "pbp_data_2024.csv")

# 2. Weekly data
weekly_cols = nfl.see_weekly_cols()  # Get all columns
if isinstance(weekly_cols, pd.Index):
    weekly_cols = weekly_cols.tolist()
weekly_data = nfl.import_weekly_data(years, columns=weekly_cols)
clean_and_save(weekly_data, "weekly_data_2024.csv")

# 3. Seasonal data
seasonal_data = nfl.import_seasonal_data(years, s_type='ALL')
clean_and_save(seasonal_data, "seasonal_data_2024_all.csv")

seasonal_data_reg = nfl.import_seasonal_data(years, s_type='REG')
clean_and_save(seasonal_data_reg, "seasonal_data_2024_reg.csv")

seasonal_data_post = nfl.import_seasonal_data(years, s_type='POST')
clean_and_save(seasonal_data_post, "seasonal_data_2024_post.csv")

# 4. Additional data imports
roster_cols = None  # Get all columns
seasonal_rosters = nfl.import_seasonal_rosters(years, columns=roster_cols)
clean_and_save(seasonal_rosters, "seasonal_rosters_2024.csv")

weekly_rosters = nfl.import_weekly_rosters(years, columns=roster_cols)
clean_and_save(weekly_rosters, "weekly_rosters_2024.csv")

win_totals = nfl.import_win_totals(years)
clean_and_save(win_totals, "win_totals_2024.csv")

sc_lines = nfl.import_sc_lines(years)
clean_and_save(sc_lines, "sc_lines_2024.csv")

officials = nfl.import_officials(years)
clean_and_save(officials, "officials_2024.csv")

draft_picks = nfl.import_draft_picks(years)
clean_and_save(draft_picks, "draft_picks_2024.csv")

draft_values = nfl.import_draft_values()
clean_and_save(draft_values, "draft_values.csv")  # No year parameter

team_desc = nfl.import_team_desc()
clean_and_save(team_desc, "team_desc.csv")  # No year parameter

schedules = nfl.import_schedules(years)
clean_and_save(schedules, "schedules_2024.csv")

combine_data = nfl.import_combine_data(years, positions=None) # Get all positions
clean_and_save(combine_data, "combine_data_2024_all.csv")

ids_data = nfl.import_ids(columns=None, ids=None) #get all ids and columns
clean_and_save(ids_data, "ids_data.csv")

# 5. NGS data
ngs_passing = nfl.import_ngs_data(stat_type='passing', years=years)
clean_and_save(ngs_passing, "ngs_passing_2024.csv")

ngs_rushing = nfl.import_ngs_data(stat_type='rushing', years=years)
clean_and_save(ngs_rushing, "ngs_rushing_2024.csv")

ngs_receiving = nfl.import_ngs_data(stat_type='receiving', years=years)
clean_and_save(ngs_receiving, "ngs_receiving_2024.csv")

depth_charts = nfl.import_depth_charts(years)
clean_and_save(depth_charts, "depth_charts_2024.csv")

injuries = nfl.import_injuries(years)
clean_and_save(injuries, "injuries_2024.csv")

qbr_nfl = nfl.import_qbr(years, level='nfl', frequency='season')
clean_and_save(qbr_nfl, "qbr_nfl_2024.csv")

qbr_college = nfl.import_qbr(years, level='college', frequency='season')
clean_and_save(qbr_college, "qbr_college_2024.csv")

qbr_nfl_weekly = nfl.import_qbr(years, level='nfl', frequency='weekly')
clean_and_save(qbr_nfl_weekly, "qbr_nfl_weekly_2024.csv")

qbr_college_weekly = nfl.import_qbr(years, level='college', frequency='weekly')
clean_and_save(qbr_college_weekly, "qbr_college_weekly_2024.csv")

# 6. PFR data
pfr_passing = nfl.import_seasonal_pfr(s_type='pass', years=years)
clean_and_save(pfr_passing, "pfr_seasonal_passing_2024.csv")

pfr_receiving = nfl.import_seasonal_pfr(s_type='rec', years=years)
clean_and_save(pfr_receiving, "pfr_seasonal_receiving_2024.csv")

pfr_rushing = nfl.import_seasonal_pfr(s_type='rush', years=years)
clean_and_save(pfr_rushing, "pfr_seasonal_rushing_2024.csv")

pfr_weekly_passing = nfl.import_weekly_pfr(s_type='pass', years=years)
clean_and_save(pfr_weekly_passing, "pfr_weekly_passing_2024.csv")

pfr_weekly_receiving = nfl.import_weekly_pfr(s_type='rec', years=years)
clean_and_save(pfr_weekly_receiving, "pfr_weekly_receiving_2024.csv")

pfr_weekly_rushing = nfl.import_weekly_pfr(s_type='rush', years=years)
clean_and_save(pfr_weekly_rushing, "pfr_weekly_rushing_2024.csv")

snap_counts = nfl.import_snap_counts(years)
clean_and_save(snap_counts, "snap_counts_2024.csv")

ftn_data = nfl.import_ftn_data(years)
clean_and_save(ftn_data, "ftn_data_2024.csv")

print("All data extraction and saving complete!")
