# s3-cost-analysis

## STEPS
1. Use the RA role to get access keys via auth and then run the crawling using the `bucket_list()` function for the following buckets:
   * r-f-d
   * long-term storage bucket (with filter: `early*/`)
2. After that, use the code in `main.py` to process the Pandas dataframe and calculate the cost, make sure to modify the column names to align them with the actual dataframe, and then finally produce:
   * The accumulated cost year-over-year for the years 2021, 2022, 2023, 2024 (YTD)
   * The accumulated cost for each month
   * Total storage volume per year in TB

## Note
* This calculation is a rough estimate that does not take into the effect of Intelligent-Tiering solutions, we're only using the basic pricing tiers, therefore the estimation would be inflated (the actual cost would be less than these numbers)
* Reuse this code for further processing use cases

## File
1. `simulation.ipynb`
   * Contains code on how to create a simulated dataframe that contains some columns
   * `file_path`, `file_size`, `file_timestamp`
2. `main.py`
   * With all the relevant functions that helps analyze and plot the data
   * ```
     file_path = "s3_inventory.csv"
     main(file_path)
     ```
