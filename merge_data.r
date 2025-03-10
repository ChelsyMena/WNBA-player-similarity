# Load necessary libraries
library(dplyr)

script_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
data_directory <- file.path(script_dir, 'data')

# Read all CSV files in the directory and combine them into a single data frame
file_list <- list.files(path = data_directory, pattern = "*.csv", full.names = TRUE)
dfs <- lapply(file_list, function(file) {
  df <- read.csv(file)
  df$Season <- gsub(".csv", "", basename(file))
  return(df)
})
combined_df <- bind_rows(dfs)

# print(combined_df)

# Save the combined data frame to a CSV file
output_file_path <- file.path(data_directory, "per_100_r.csv")
write.csv(combined_df, file = output_file_path, row.names = FALSE)