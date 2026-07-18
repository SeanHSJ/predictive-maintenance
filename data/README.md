# Data

The NASA C-MAPSS dataset isn't bundled in this repo (keep raw data out of git — it's good practice recruiters notice).

## How to get it
1. Go to the NASA Prognostics Center of Excellence data repository:
   https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
2. Find "Turbofan Engine Degradation Simulation Data Set" and download the zip (often called `CMAPSSData.zip` or similar; also mirrored on Kaggle — search "NASA C-MAPSS" if the NASA link is unavailable)
3. Extract into this `data/` folder. You should see files like:
   - `train_FD001.txt`
   - `test_FD001.txt`
   - `RUL_FD001.txt`
   (FD001 is the simplest subset — start there. FD002-FD004 add more operating conditions/fault modes if you want to extend the project later.)

## Format note
Files are space-delimited, no header row. Columns are:
`unit_number, time_in_cycles, operational_setting_1-3, sensor_1-21`

Add a `.gitignore` entry for `data/*.txt` so raw data isn't committed to GitHub — only the processed/summary outputs should be.
